# Bilan final — refonte OUSS en prose

Finalisation du 24 novembre 2026. Modèle : `gpt-6-astra`. Ce bilan remplace les états de livraison des anciennes versions en puces. Le contrat initial est conservé dans [l’audit préalable](audit-global-prose.md) ; sa réservation de publication au parent décrivait la répartition de travail initiale, pas une interdiction de la publication finale autorisée.

## Travail livré

Les neuf textes déjà écrits et commités jusqu’à `da1ce2b` ont été relus dans leur ordre, sans recommencer la rédaction. La passe d’ensemble n’a pas identifié de défaut matériel justifiant une nouvelle réécriture. Les récurrences de reprise, preuve et délégation servent des décisions distinctes ; elles ne sont pas supprimées mécaniquement. La finalisation rend le manuscrit principal, assemble les neuf composants, achève leur navigation documentaire et remplace le contrôle actif des puces par celui de la prose.

| Texte | Développement concret conservé et vérifié à la relecture |
|---|---|
| Introduction | Position constructeur sans anecdote ; distinction menace, obligation et offre ; passage du connecteur à la capacité réelle. |
| Conseil | Chaîne de reprise plutôt que seule copie ; British Library ; corpus ENISA borné ; valeur d’information et acceptation dans les délégations. |
| Standards | Applicabilité avant achat ; procédure, retrait effectif des droits et preuve de fonctionnement ; retest après changement pertinent. |
| Investissements | Maintenabilité et coûts futurs ; sémantique des règles ; séparation contrôle/données ; consolidation défendable sans indépendance fictive. |
| Veille | CVSS de base distinct du risque ; composant actif, chemins d’accès et préconditions ; DBIR borné ; pilote pouvant réellement perdre. |
| Budget | Coexistence et capacité de transition ; retour arrière distinct de remise en charge avec FCC/AT&T ; trésorerie, charge et capacité non interchangeables. |
| Gartner et achats | Favori éliminable ; exigences indispensables ; disponibilité sur version/matériel ; export réutilisable et coût de réversibilité. |
| Gouvernance | Avis, acceptation et exécution séparés ; arrêt de l’agent distinct des secrets, sessions et files ; exécution après désaccord légitime. |
| Conclusion | Situation explicitement hypothétique ; reprise prioritaire, migration préparée, automatisation différée sauf effet démontré ; prix et conditions d’inversion. |

## Deux passes et auto-critique OUSS

La première passe suit l’argument, la voix et les frontières entre chapitres. Les forces sont les mécanismes concrets, la contradiction prise au sérieux et les choix qui peuvent changer avec les faits. La voix est directe, technique et conversationnelle ; l’ironie vise les raisonnements faciles, pas les équipes. Le constructeur n’est ni procureur universel des fournisseurs ni porte-parole commercial. Aucun vécu privé n’a été ajouté.

Limites : cette voix reste une approximation éditoriale, pas une validation personnelle d’Oussama. Les formulations conditionnelles et les questions peuvent donner par endroits une cadence régulière ; elles expriment ici des limites techniques utiles, sans justifier une nouvelle passe cosmétique. Ce livre court privilégie la démonstration à la narration. La conclusion réemploie volontairement la reprise pour rassembler les arbitrages, sans prétendre imposer une priorité universelle. Aucun score de détecteur d’IA ni seuil stylistique artificiel.

La seconde passe confronte les assertions documentaires aux cartes et extraits conservés, puis contrôle l’assemblage, les marqueurs, les liens et les comptages. Les distinctions sensibles restent présentes : panne non confondue avec attaque, disponibilité avec confidentialité, guide avec droit, annonce avec fonction testée, score avec risque local, budget refusé avec risque accepté. Les revues Grok héritées n’ont pas examiné la nouvelle prose. Aucun nouvel appel de modèle externe n’a été nécessaire.

## Vérifications et limites

Le script [verify-prose.py](verify-prose.py) vérifie les neuf fichiers 00–08, leur ordre, un titre par texte, l’absence de listes et de marqueurs de rédaction inachevée, l’égalité exacte de l’assemblage, la correspondance des marqueurs de preuve et les liens Markdown locaux avec leurs ancres dans le projet français. Il ne réapplique aucun plafond historique de trois puces. Les commentaires HTML de preuves sont conservés conformément au contrat d’assemblage exact ; ils sont invisibles dans le rendu Markdown.

Le vérificateur `sources.py verify --strict --evidence` est exécuté avec le véritable format du registre complémentaire (`sources` est une liste d’objets avec `id` et `quotes`). La carte contient trois références complémentaires. Ses citations dans un tableau ne donnent pas une couverture de prose mesurable : le contrôle direct annonce 0 % de couverture sur ses fragments narratifs. Ce n’est ni une erreur de correspondance, ni une preuve que toutes les phrases du livre sont sourcées. Un audit temporaire des paragraphes portant P1–P3 contrôle séparément leurs citations et le bloc Sources généré ; il n’ajoute pas de bibliographie au manuscrit.

Aucune source externe n’a été récupérée de nouveau pendant cette finalisation. Les réserves de troncature, de divergence interne ENISA et de transposition française figurent dans [incertitudes-prose.md](incertitudes-prose.md). Les produits et la procédure de révocation restent à tester dans les environnements concernés. Pas de certification juridique, pas de relecture indépendante de la nouvelle prose, pas de PDF produit ou inspecté. Toutes les recherches et anciennes revues sont conservées ; les corps tiers restent hors publication.

## Comptages définitifs

Comptage par séparation des espaces, titres de chapitres et commentaires HTML exclus ; pas de cible de longueur imposée.

| Texte | Mots |
|---|---:|
| Introduction | 876 |
| 1 — Conseil | 1 257 |
| 2 — Standards | 1 270 |
| 3 — Investissements | 1 259 |
| 4 — Veille | 1 311 |
| 5 — Budget | 1 341 |
| 6 — Gartner et achats | 1 207 |
| 7 — Gouvernance | 1 360 |
| Conclusion | 969 |
| **Total** | **10 850** |

Contrôles exécutés : neuf composants, assemblage exact, 15 occurrences de preuve pour 14 marqueurs distincts, 103 liens locaux valides. Quatre occurrences de liens relatifs sont cassées dans l’ancien instantané `reviews/concis/dossier.md` (trois cibles distinctes). Cet input historique de revue est préservé à l’identique ; ces liens ne servent pas à naviguer dans la livraison active. Le script les signale séparément et échoue sur une cible manquante hors des revues historiques.

L’audit temporaire P1–P3 a bien contrôlé trois paragraphes cités avec `--strict --evidence` : résultat `citations OK`, trois sources munies d’extraits. Sa couverture heuristique est de 25 % (3 fragments cités sur 12), car le marqueur porte un paragraphe documentaire, non chaque phrase. Aucun seuil de couverture globale ni vérification automatique d’implication sémantique n’est revendiqué.

Les comptages et résultats mécaniques définitifs sont consignés dans [verification-prose.json](verification-prose.json). Le contrôle Git porte uniquement sur `books/ciso-fr`. L’état de publication est établi après le commit par lecture du SHA distant et comparaison des blobs de tous les fichiers modifiés depuis le dernier état publié, puis communiqué avec le lien de lecture ; ce bilan ne prétend pas anticiper le succès du push.
