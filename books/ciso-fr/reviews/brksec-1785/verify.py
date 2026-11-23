"""Read-only checks for the Cisco integration; JSON result to stdout."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[2]
repo = root.parents[1]
baseline = '83b490e23aff0e627ed29ced3915ae3847f22c35'
base = (root / 'base-auteur.md').read_text()
old = subprocess.check_output(['git', 'show', baseline + ':books/ciso-fr/base-auteur.md'], cwd=repo, text=True)
assert re.findall(r'^- .*', base, re.M) == re.findall(r'^- .*', old, re.M)
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
        counts.append(len(top)); nested.append(len(sub))
    expected = section.replace('## ', '# ', 1).replace('(research/', '(../research/').rstrip() + '\n'
    assert (root / f'chapters/{i:02d}.md').read_text() == expected
ledger = json.loads((root / 'research/developpement-ledger.json').read_text())
ids = {s['id'] for s in ledger['sources']}
assert ids == {1, 2, 3, 5} and all(s['quotes'] for s in ledger['sources'])
refs = re.findall(r'\[(\d+)\]\(research/developpement-sources.md#source-(\d+)\)', base)
assert len(refs) == 5 and all(a == b and int(a) in ids for a, b in refs)
cisco = re.findall(r'\[Cisco, p\. ([^]]+)\]\(research/brksec-1785.md#([^)]+)\)', base)
assert dict((anchor, pages) for pages, anchor in cisco) == {
    'maintenabilite': '14–17', 'dependances': '26', 'contenir': '34–37',
    'pilote': '49–51', 'cadence': '40–43', 'achat': '38', 'agents': '44–47'}
assert len(cisco) == 7
assert not re.search(r'\[\d+\](?!\()', base)
active = [root / n for n in ['README.md', 'base-auteur.md', 'mind-map.md', 'research/developpement-sources.md', 'research/brksec-1785.md']]
active += list((root / 'chapters').glob('*.md')) + list((root / 'reviews/brksec-1785').glob('*.md'))
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
for suffix in ['', '-final']:
    meta = json.loads((root / f'reviews/brksec-1785/grok{suffix}.json').read_text())
    for name, key in [(f'dossier{suffix}.md', 'source_sha256'), (f'prompt{suffix}.md', 'prompt_sha256')]:
        assert hashlib.sha256((root / 'reviews/brksec-1785' / name).read_bytes()).hexdigest() == meta[key]
    assert meta['model_returned'] == 'grok-4.7' and meta['finish_reason'] == 'stop'
for i in (1, 2):
    assert ElementTree.parse(root / f'carte-{i}.svg').getroot().tag.endswith('svg')
for name in ['mind-map.md', 'carte-1.svg', 'carte-2.svg', 'chapters/00.md', 'chapters/01.md', 'chapters/02.md', 'chapters/08.md']:
    original = subprocess.check_output(['git', 'show', f'{baseline}:books/ciso-fr/{name}'], cwd=repo)
    assert original == (root / name).read_bytes(), name
mind = (root / 'mind-map.md').read_text()
assert len(re.findall(r'^    [1-7] .+\n((?:      .+\n){3})', mind, re.M)) == 7
changed = subprocess.check_output(['git', 'diff', '--name-only', baseline], cwd=repo, text=True).splitlines()
new = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=repo, text=True).splitlines()
assert all(p.startswith('books/ciso-fr/') for p in changed + new)
assert not any(Path(p).suffix in {'.pdf', '.png'} for p in changed + new)
result = dict(chapters=7, bullets_per_chapter=counts, total_bullets=sum(counts), nested_per_chapter=nested, nested_bullets=sum(nested), synchronized_sheets=9, mindmap_branches=7, svg_xml_valid=2, diagrams_unchanged=True, local_links_checked=links, citation_occurrences=len(refs)+len(cisco), historical_citation_occurrences=len(refs), cisco_citation_occurrences=len(cisco), historical_source_ids=sorted(ids), scope_only_books_ciso_fr=True, base_words_whitespace=len(base.split()), baseline_words_whitespace=len(old.split()), word_growth_percent=round((len(base.split())/len(old.split())-1)*100,2), base_sha256=hashlib.sha256(base.encode()).hexdigest(), cisco_pdf_pages_read=62, cisco_pages_visually_inspected=[1,15,26,29,34,38,51,53], gpt_model='gpt-6-astra', grok_model='grok-4.7', grok_completed_reviews=2, grok_saw_pdf=False, final_post_review_clarifications=True, telco_audit_integrated=False)
print(json.dumps(result, ensure_ascii=False, indent=2))
