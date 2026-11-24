"""Assemble/check the nine canonical prose chapters; no legacy bullet gate."""
import argparse
import hashlib
import json
import re
import tempfile
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
HEADER = """# La sécurité n’est pas un concours de slides

*Manuscrit en prose — introduction, sept chapitres et conclusion.*

[Carte des preuves](research/carte-preuves-prose.md) · [Bilan éditorial et contrôles](progress/bilan-final-prose.md)

---

"""

def run(assemble=False):
    files = [ROOT / f"chapters/{i:02}.md" for i in range(9)]
    texts = [p.read_text() for p in files]
    assert sorted((ROOT / 'chapters').glob('*.md')) == files
    # These chapters contain no relative Markdown links. Fail rather than silently
    # assembling a future chapter whose links require relocation.
    assert not any(re.search(r'\]\((?!https?://|#)', t) for t in texts)
    expected = HEADER + '\n\n---\n\n'.join(t.rstrip() for t in texts) + '\n'
    manuscript = ROOT / 'manuscrit-complet.md'
    if assemble:
        manuscript.write_text(expected)
    assert manuscript.read_text() == expected, 'Assembly differs from canonical chapters'
    counts = {}
    markers = []
    for p, text in zip(files, texts):
        assert len(re.findall(r'^# ', text, re.M)) == 1
        assert not re.search(r'^\s*(?:[-*+] |\d+\. )', text, re.M), p
        assert not re.search(r'\b(?:TODO|TBD)\b|Ici, placer', text)
        body = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        body = re.sub(r'^#+ .*$', '', body, flags=re.M)
        counts[p.name] = len(body.split())
        markers.extend(re.findall(r'<!-- preuve: (\S+)', text))
    mapping = (ROOT / 'research/carte-preuves-prose.md').read_text()
    mapped = re.findall(r'^\| ((?:D|P)\d+|C-[\w-]+) \|', mapping, re.M)
    assert set(markers) == set(mapped)
    assert len(mapped) == len(set(mapped))
    # Validate local Markdown targets and fragments in all project Markdown,
    # including historical reviews. External pages are deliberately not fetched.
    links = 0
    historical_link_issues = []
    for p in ROOT.rglob('*.md'):
        for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\s]+)\)', p.read_text()):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target):
                continue
            path, _, anchor = unquote(target).partition('#')
            q = (p.parent / path).resolve() if path else p
            if not q.exists() and 'reviews' in p.relative_to(ROOT).parts:
                historical_link_issues.append({'file': str(p.relative_to(ROOT)), 'target': target})
                continue
            assert q.exists(), (p, target)
            if anchor and q.suffix == '.md':
                text = q.read_text()
                anchors = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text))
                for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
                    title = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
                    anchors.add(title)
                assert anchor in anchors, (p, target)
            links += 1
    ledger = json.loads((ROOT / 'research/prose-ledger.json').read_text())
    assert isinstance(ledger['sources'], list)
    assert {s['id'] for s in ledger['sources']} == {1, 2, 3}
    assert all(s.get('quotes') for s in ledger['sources'])
    result = {'canonical_chapters': 9, 'main_chapters': 7,
              'exact_assembly': True, 'words_body_whitespace': counts,
              'total_body_words_whitespace': sum(counts.values()),
              'count_method': 'Whitespace tokens, excluding chapter headings and multiline HTML comments',
              'evidence_marker_occurrences': len(markers), 'distinct_evidence_markers': len(mapped),
              'local_links_checked': links,
              'historical_review_link_issues_preserved': historical_link_issues,
              'manuscript_sha256': hashlib.sha256(expected.encode()).hexdigest(),
              'model': 'gpt-6-astra', 'independent_review_of_prose': False,
              'external_sources_refetched_in_finalization': False}
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--assemble', action='store_true')
    args = parser.parse_args()
    print(json.dumps(run(args.assemble), ensure_ascii=False, indent=2))
