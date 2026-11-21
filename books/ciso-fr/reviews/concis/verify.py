"""Validate the concise author base; run from any directory."""
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
counts = []
for i, section in enumerate(sections):
    assert not re.search(r'^[ \t]+[-*+][ \t]|^[ \t]*\d+[.)][ \t]', section, re.M)
    count = len(re.findall(r'^- ', section, re.M))
    assert count == (3 if 1 <= i <= 7 else 0), (i, count)
    expected = section.replace('## ', '# ', 1).replace('(annexe-juridique.md)', '(../annexe-juridique.md)').replace('(research/', '(../research/')
    assert (root / f'chapters/{i:02d}.md').read_text() == expected.rstrip() + '\n'
    if 1 <= i <= 7:
        assert section.startswith(f'## {i} — ')
        counts.append(count)
changed = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], cwd=repo, text=True).splitlines()
new = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=repo, text=True).splitlines()
paths = sorted(set(changed + new))
assert all(p.startswith('books/ciso-fr/') for p in paths), paths
checked_links = 0
for rel in paths:
    path = repo / rel
    if path.suffix != '.md':
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', '#')):
            continue
        # Immutable review dossier embeds root-relative manuscript links.
        link_base = root if path.name == 'dossier.md' else path.parent
        assert (link_base / target.split('#')[0]).exists(), (rel, target)
        checked_links += 1
for i in (1, 2):
    assert ElementTree.parse(root / f'carte-{i}.svg').getroot().tag.endswith('svg')
mind = (root / 'mind-map.md').read_text()
branches = re.findall(r'^    [1-7] .+\n((?:      .+\n){3})', mind, re.M)
assert len(branches) == 7
result = {'chapters': 7, 'bullets_per_chapter': counts, 'total_bullets': sum(counts), 'nested_bullets': 0, 'synchronized_sheets': 9, 'mindmap_branches': len(branches), 'svg_xml_valid': 2, 'local_links_checked': checked_links, 'scope_only_books_ciso_fr': True, 'base_words_whitespace': len(base.split()), 'base_sha256': hashlib.sha256(base.encode()).hexdigest(), 'external_sources_refetched': False}
print(json.dumps(result, ensure_ascii=False, indent=2))
