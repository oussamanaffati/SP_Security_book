# La sécurité n’est pas un concours de slides

**Sept chapitres. Trois axes chacun, développés en trois sous-puces par axe. Oussama écrit la prose.**

[Lire la base complète](base-auteur.md) · [Neuf fiches séparées](chapters/) · [Mind map Mermaid](mind-map.md)

[Carte des sept chapitres](carte-1.svg) · [Trajectoire de conclusion](carte-2.svg)

Board, standards, investissements, veille, budget, Gartner et achats, gouvernance : 21 axes et 63 sous-puces. Chaque axe apporte un mécanisme, une contradiction ou une indication concrète de développement. Introduction et conclusion restent brèves. Aucun souvenir personnel, dialogue ou montant inventé. Les cartes gardent les mêmes trois axes ; elles ne reproduisent pas les développements.

## Avis confrontés

[Auto-critique GPT](reviews/brksec-1785/gpt.md) · [Contre-revue Grok finale](reviews/brksec-1785/grok-final.md) · [Arbitrages et limites](reviews/brksec-1785/journal.md)

Modèles : `gpt-6-astra` (runtime déclaré, auto-critique) et `grok-4.7` (API, modèle retourné sur deux passes). Le [dossier final transmis](reviews/brksec-1785/dossier-final.md) est conservé à l’identique ; trois précisions post-revue sont identifiées dans le journal, sans prétendre à une nouvelle validation Grok. Grok a examiné la base, la carte et les notes de preuves, pas le PDF intégral ni des sources web. Les [revues de développement antérieures](reviews/developpement/journal.md) restent historiques.

## Preuves au bon endroit

Les références de la base et des fiches pointent vers le **[registre de développement](research/developpement-sources.md)** et son [ledger](research/developpement-ledger.json), distincts des anciens numéros. British Library : reprise au chapitre 1 et canal de crise au chapitre 7. Cloudflare : dépendances au chapitre 3. ENISA : portée du guide au chapitre 2. DBIR 2025 : statistique bornée au chapitre 4. La [lecture critique de BRKSEC-1785](research/brksec-1785.md) ajoute sept idées aux chapitres 3–7 : maintenabilité, dépendance du plan de contrôle, confinement temporaire, constats vérifiables, capacité récurrente de changement, limites des roadmaps et pouvoirs des agents IT. Leurs références « Cisco, p. … » utilisent les pages PDF exactes. Annonces fournisseur et interprétations auteur restent séparées ; aucun chiffre Cisco non recoupé n’est repris. Les chapitres 1–2 et les trois axes de chaque chapitre sont conservés.

Cas historiques, pas une sélection de dernière actualité. Quatre sources primaires récupérées lors du développement précédent ; le PDF Cisco est la seule nouvelle source de cette passe, lu sur ses 62 pages. Limites d’extraction et d’inférence documentées. La page Gartner bloquée n’est pas une source nouvellement vérifiée. La recherche et le fact-check telco sont une passe distincte, non encore intégrée ici. Ni les avis de modèles ni le contrôle des citations ne valent certification factuelle ou juridique.

[Repères historiques](research/reperes-documentaires.md) · [Ancien registre préservé](research/ledger-final.json) · [Annexe juridique préservée](annexe-juridique.md) · [Vérifications actuelles](verification.json) · [Script de contrôle actuel](reviews/brksec-1785/verify.py)

Les anciennes revues et le vérificateur `reviews/concis/verify.py` documentent uniquement la version concise antérieure, sans sous-puces. Le vérificateur `reviews/developpement/verify.py` appartient à la passe de développement précédente ; `reviews/brksec-1785/verify.py` définit les contrôles actifs. La carte et ses SVG sont inchangés : les nouveaux exemples approfondissent les mêmes trois axes. Le livre anglais est inchangé. La [version concise](https://github.com/oussamanaffati/SP_Security_book/tree/2a9760d/books/ciso-fr) reste dans l’historique.
