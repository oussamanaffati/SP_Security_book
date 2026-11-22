# Auto-critique GPT — version développée

## Identité et périmètre

Modèle exact déclaré par le runtime : **gpt-6-astra**, fournisseur **openai-codex**. Rédaction et auto-critique réalisées par le même modèle : ce document n’est pas une revue indépendante. Aucun appel Grok effectué par ce sous-agent ; la confrontation Grok et la publication sont confiées au parent.

Version évaluée : `base-auteur.md`, SHA-256 `f69689016385bed24dbb68ff5da791bdb26ca986e8198cf47b28c6eaca74e221`.

La base d’origine a été lue en entier. Les sept titres et les vingt et un intitulés d’axes sont conservés. La demande récente de développement autorise les sous-puces : le plafond ancien sans sous-listes n’a pas été appliqué.

## Résultat éditorial

Le document apporte désormais des mécanismes exploitables, pas seulement des slogans : reprise du service versus possession des copies ; validité d’une preuve après changement ; travail ajouté par l’automatisation ; coût futur de sortie ; différence entre acceptation du risque et exécution. Les consignes « Ici, … » désignent un passage à développer avec son contenu, plutôt qu’un emplacement vide.

Trois ancrages empiriques distincts : British Library, Cloudflare, statistique DBIR 2025. La British Library revient brièvement sur un autre mécanisme au chapitre 7, sans raconter à nouveau toute l’attaque. Une quatrième source primaire, ENISA, fonde la distinction juridique du chapitre 2. Les chapitres budget et achats privilégient le raisonnement plutôt que des chiffres décoratifs.

Les contrepoints rendent les choix moins automatiques : réparer avant de jeter, rester temporairement sans sanctuariser le fournisseur, laisser gagner un leader, ne pas vendre toute heure libérée comme un poste supprimé, ne pas inventer un droit d’arrêt dans l’urgence.

## Faiblesses restantes

- Structure encore très régulière : chaque axe reçoit trois sous-puces. C’est lisible pour l’auteur, mais la prose finale devra varier les rythmes et ne pas conserver partout « développer / ici / contrepoint ».
- Proximité volontaire des chapitres 3 et 5 : le premier juge la capacité et la sortie, le second leur financement et le travail disponible. Cette frontière doit rester visible lors de la rédaction pour éviter de raconter deux fois la migration.
- Le chapitre 6 manque d’un cas public d’achat documenté. Il fournit néanmoins des scènes argumentatives précises : critère éliminatoire, choix contraint, export techniquement inutilisable. Ces éléments sont des propositions de développement, pas des cas vécus.
- Les formulations sont compatibles avec une voix directe de CISO, mais aucune prose personnelle nouvelle d’Oussama n’a été fournie. Impossible de certifier son idiolecte ; ne pas présenter ce résultat comme ses souvenirs ou sa voix authentifiée.
- Ironie limitée et quelques formules seulement : choix intentionnel pour donner davantage de fond. L’auteur pourra durcir le ton sans changer les preuves.

## Corrections apportées pendant l’auto-critique

1. Gardé la distinction trafic / plan de contrôle dans le cas Cloudflare : éviter de raconter une panne totale de son réseau.
2. Borné le chiffre DBIR à son corpus et à sa période ; refusé l’inférence en probabilité locale. Retenu un énoncé textuel sur l’ensemble des violations plutôt qu’un recalcul à partir d’une figure au périmètre différent.
3. Écarté l’attribution factuelle à Gartner après le blocage HTTP 403 ; conservé l’axe comme recommandation d’achat, sans prétendre à une nouvelle vérification de sa FAQ.
4. Distingue explicitement exposition hors délégation, obligation non satisfaite et désaccord légitime ; l’urgence ne crée pas de pouvoir universel.
5. Raccourci légèrement le chapitre 6 pour rester dans la cible de longueur sans supprimer son argument.

## Contrôles exécutés

Comptage par séparation aux titres `##`, avec mots séparés par espaces, titres compris :

| Chapitre | Mots | Puces principales | Sous-puces |
|---|---:|---:|---:|
| 1 | 324 | 3 | 9 |
| 2 | 334 | 3 | 9 |
| 3 | 329 | 3 | 9 |
| 4 | 338 | 3 | 9 |
| 5 | 333 | 3 | 9 |
| 6 | 347 | 3 | 9 |
| 7 | 339 | 3 | 9 |

**21 puces principales**, trois par chapitre ; chaque axe a trois sous-puces, donc dans la plage autorisée de deux à quatre. Titres comparés automatiquement avec ceux de la base. Aucun montant, dialogue ou souvenir personnel inventé. Introduction et conclusion courtes, aucun nouveau cadre méthodologique ajouté.

Validation `sources.py verify --strict --evidence` sur une copie d’audit avec liste de sources rendue depuis un ledger filtré : **citations OK** ; quatre sources citées, quatre avec extraits attachés. Les extraits ont été contrôlés automatiquement contre les textes récupérés. Le taux brut de fragments cités est faible parce que l’essentiel du texte est du conseil éditorial ; il ne faut pas le présenter comme un score d’exactitude. Lecture manuelle des affirmations publiques effectuée en complément.

## Limites documentaires et livraison

Le DBIR est volontairement l’édition historique 2025, pas un état annoncé comme actuel du marché. Les cas British Library et Cloudflare sont des récits primaires des organisations concernées, pas des corroborations indépendantes. L’extraction Cloudflare n’est pas complète ; seuls les passages introductifs et d’architecture effectivement lus portent les affirmations utilisées. Le guide ENISA ne vaut pas analyse complète du droit national.

Les sources et pièces brutes sont dans ce dossier de travail. Publier uniquement les fichiers éditoriaux sélectionnés, pas les PDF ou textes intégraux récupérés. Aucun fichier du dépôt `/data/SP_Security_book` modifié ; aucun commit ni push. Le parent doit encore réaliser sa revue finale et la passe Grok demandée avant d’annoncer une validation à deux modèles.
