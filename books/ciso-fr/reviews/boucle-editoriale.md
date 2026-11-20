# Boucle éditoriale — passage du manuscrit à une base auteur

## Contrat corrigé

- L’auteur rédige le livre ; le livrable de l’assistant est une base en bullets et une mind map.
- Suppression des scènes, dialogues, personnages et budgets inventés ; pas de mentions répétées de fiction à substituer aux scènes supprimées.
- Les sept situations sont conservées, chacune associée à une décision distincte.
- La contrainte précédente de longueur des scènes n’est plus applicable.

## Critiques et corrections réelles

| Passe | Document envoyé | Résultat et suite |
|---|---|---|
| `grok-v1` | Ancien manuscrit complet | Répétitions entre chapitres, narration trop conciliante, roadmap artificiellement chiffrée, cadrage juridique fragile. Réponse arrêtée par la limite de sortie : ne pas la présenter comme revue complète des sept fiches proposées. Reconstruction en base auteur. |
| `grok-v2` | Nouvelle base et mind map | Structure validée ; bibliographie absente du dossier envoyé et champ NIS 2 insuffisamment explicite. Bibliographie ajoutée, champ et droit national distingués. |
| `grok-v3` | Base corrigée, sources et cartes | Reprise du schéma de report/financement et de ses contraintes ; précision de l’attribution des sources et des notifications. |
| `grok-v4` | Version corrigée complète | Contradiction supplémentaire sur la carte ; plusieurs objections aux sources ne tenaient pas compte de leurs extraits réels. Corrections de carte, ajout de questions auteur, séparation des attributions Anthropic. |
| `grok-v5` | Document complet et extraits justificatifs | Retrait des objections non fondées sur CISA/libre et dérogation NIS 2. Objection pertinente : délai général de notification à 72 h devait conserver « sans retard injustifié ». Correction faite. |
| `grok-final` | Ensemble corrigé et article 23(1)-(4) | Clarifier clauses contractuelles négociables/non négociables ; rendre l’arbitrage technique du chapitre board explicite ; resserrer la phrase CISA sur les journaux. Corrections faites. Une tentative HTTP 503 a précédé la réponse obtenue, sans résultat inventé. |
| `grok-closure` | Ensemble final complet et preuves | Vérification de clôture des points précédents : aucun problème bloquant identifié dans le dossier. |

## Décisions retenues

- **Narration → structure :** auteur libre de sa voix ; chaque chapitre donne une question, des arguments contradictoires, un outil distinct et des pistes à documenter.
- **Doublons :** board = arbitrage stratégique ; gouvernance = autorité d’action. Investissements = coûts futurs de l’existant ; Gartner = sélection et engagements fournisseur. Budget = faisabilité du portefeuille.
- **Roadmap :** suppression des 60 jours-personnes et du calendrier trimestriel arbitraire ; dépendances et portes de décision conditionnelles, avec reports et réexamens.
- **NIS 2 :** lecture directe de la directive et du règlement d’exécution sur EUR-Lex. Délais reliés au champ, distinction alerte précoce/notification, dérogation services de confiance, absence de conclusion non établie sur le droit français.
- **Innovation :** pas seulement les agents ; trois files de veille, alternatives simples, contre-exemples au rejet réflexe de la nouveauté.
- **Gouvernance :** identités non humaines, contrôle des sessions/jetons/actions en cours, reprise avec chemin d’administration de confiance.
- **Cartes :** rendu réel de deux diagrammes Mermaid en SVG ; report avec revue datée, maintien, décisions habilitées et contraintes non négociables.

## Objections de Grok non adoptées automatiquement

- **CISA et logiciel libre :** l’extrait lu parle bien de diligence continue. Conservation comme recommandation attribuée, pas obligation juridique ; Grok a ensuite retiré son objection avec la preuve.
- **Services de confiance / NIS 2 :** la dérogation au point b de l’article 23(4) figure dans le texte consulté. Conservation et explicitation ; pas suppression parce que le relecteur n’avait pas ouvert la source.
- **Sources non consécutives :** identifiants historiques conservés ; contrôles de résolution réussis. Les trous ne prouvent pas une référence orpheline.
- **Méthode Gartner prétendument structurellement défavorable aux petites équipes :** proposition non reprise faute de preuve sur un rapport et une pondération précis.
- **Diagramme exhaustif :** plusieurs suggestions utiles intégrées, sans présenter une carte de raisonnement comme une procédure de crise complète.

## Vérifications et limites

- Modèle de rédaction/révision : `gpt-6-astra` ; modèle xAI effectivement retourné : `grok-4.7`.
- Sept réponses de revue enregistrées ; hachages des dossiers envoyés et statut de fin dans les JSON associés.
- Le dossier final envoyé contient exactement la base auteur et la mind map publiées, suivies des pièces de vérification ; hachages consignés dans `verification.json`.
- Sources historiques vérifiées lors du premier jet ; les textes européens ont été récupérés et relus pendant cette refonte. Pas de prétention à une nouvelle vérification de toutes les autres pages.
- Relecture Grok = contradiction sur dossier ; pas recherche web indépendante, certification technique ou avis juridique.
- Auto-critique : structure nettement plus distincte et exploitable ; dossier NIS 2 plus dense que les autres. L’auteur devra choisir ses exemples réels et son niveau de détail. Ne pas transformer les pistes d’exemples en anecdotes prétendument vécues.
- Référence de contrôle final : `grok-closure.md`. Aucun score de qualité automatique n’est utilisé comme preuve.
