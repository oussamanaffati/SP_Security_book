"""Validate the developed French author base; read-only, JSON to stdout."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[2]
repo = root.parents[1]
base = (root / 'base-auteur.md').read_text()
sections = re.split(r'(?=^## )', base, flags=re.M)[1:]
assert len(sections) == 9
counts, nested = [], []
for i, section in enumerate(sections):
    top = re.findall(r'^- ', section, re.M)
    sub = re.findall(r'^  - ', section, re.M)
    assert len(top) == (3 if 1 <= i <= 7 else 0)
    assert len(sub) == (9 if 1 <= i <= 7 else 0)
    if 1 <= i <= 7:
        assert section.startswith(f'## {i} — ')
        axes = re.split(r'(?=^- )', section, flags=re.M)[1:]
        assert all(len(re.findall(r'^  - ', a, re.M)) == 3 for a in axes)
        counts.append(len(top))
        nested.append(len(sub))
    expected = section.replace('## ', '# ', 1).replace('(research/', '(../research/').rstrip() + '\n'
    assert (root / f'chapters/{i:02d}.md').read_text() == expected
ledger = json.loads((root / 'research/developpement-ledger.json').read_text())
ids = {s['id'] for s in ledger['sources']}
assert ids == {1, 2, 3, 5}
assert all(s['quotes'] for s in ledger['sources'])
refs = re.findall(r'\[(\d+)\]\(research/developpement-sources.md#source-(\d+)\)', base)
assert len(refs) == 5 and all(a == b and int(a) in ids for a, b in refs)
assert not re.search(r'\[\d+\](?!\()', base)
active = [root / 'README.md', root / 'base-auteur.md', root / 'mind-map.md', root / 'research/developpement-sources.md']
active += list((root / 'chapters').glob('*.md')) + list((root / 'reviews/developpement').glob('*.md'))
links = 0
for path in active:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://')):
            continue
        file, _, anchor = target.partition('#')
        dest = (path.parent / file) if file else path
        assert dest.exists(), (path, target)
        if anchor:
            assert f'id="{anchor}"' in dest.read_text(), (path, target)
        links += 1
meta = json.loads((root / 'reviews/developpement/grok.json').read_text())
for name, key in [('dossier.md', 'source_sha256'), ('prompt.md', 'prompt_sha256')]:
    assert hashlib.sha256((root / 'reviews/developpement' / name).read_bytes()).hexdigest() == meta[key]
assert meta['model_returned'] == 'grok-4.7' and meta['finish_reason'] == 'stop'
for i in (1, 2):
    assert ElementTree.parse(root / f'carte-{i}.svg').getroot().tag.endswith('svg')
mind = (root / 'mind-map.md').read_text()
assert len(re.findall(r'^    [1-7] .+\n((?:      .+\n){3})', mind, re.M)) == 7
changed = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=repo, text=True).splitlines()
new = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=repo, text=True).splitlines()
assert all(p.startswith('books/ciso-fr/') for p in changed + new)
result = dict(chapters=7, bullets_per_chapter=counts, total_bullets=sum(counts), nested_per_chapter=nested, nested_bullets=sum(nested), synchronized_sheets=9, mindmap_branches=7, svg_xml_valid=2, local_links_checked=links, citation_occurrences=len(refs), source_ids=sorted(ids), scope_only_books_ciso_fr=True, base_words_whitespace=len(base.split()), base_sha256=hashlib.sha256(base.encode()).hexdigest(), source_bodies_retrieved_during_development=True, grok_model=meta['model_returned'], final_post_review_clarifications=True)
print(json.dumps(result, ensure_ascii=False, indent=2))
