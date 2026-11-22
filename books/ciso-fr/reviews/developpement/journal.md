# Développement — confrontation et arbitrages

## Périmètre et provenance

La demande récente autorise le développement des trois axes de chaque chapitre : trois sous-puces par axe, pas de nouvelle architecture. Livre anglais, annexe juridique et ledger historique préservés. Cartes inchangées : les axes sont inchangés.

GPT : `gpt-6-astra`, rédaction et auto-critique, pas une revue indépendante. Son rapport archivé décrit la version avant confrontation, SHA-256 `f69689016385bed24dbb68ff5da791bdb26ca986e8198cf47b28c6eaca74e221`. Ses indications de publication à venir sont historiques.

Grok : premier appel interrompu par ReadTimeout après 420 secondes, sans avis. Une nouvelle tentative réelle a réussi : modèle demandé et retourné `grok-4.7`, `finish_reason=stop`. Dossier complet, sans troncature locale. [Métadonnées](grok.json), [dossier exact](dossier.md), [instruction exacte](prompt.md). Aucune recherche web par Grok. Ses réserves portent sur le dossier, pas sur une nouvelle lecture des PDF.

## Disposition des observations

- **Cloudflare — adopté.** Explicité qu’il s’agit d’une panne partielle chez un fournisseur, non d’une panne multi-fournisseurs. Le transfert aux dépendances entre contrats est un raisonnement séparé. Réseau et sécurité maintenus ; plan de contrôle et analytique touchés. Le désaccord de Grok améliore le branchement du cas sans démontrer que le fait original était faux.
- **British Library — adopté en partie.** « Messagerie » devient « courrier électronique », plus fidèle à `email`. Copies, équipe Gold et date restent : ils figurent dans le corps récupéré, même si les extraits courts fournis au contradicteur ne les reproduisent pas intégralement. Refus de confondre absence dans l’extrait et absence dans la source. Aucune recommandation générale de WhatsApp ni déduction d’un pouvoir d’arrêt.
- **DBIR — clarification adoptée.** Corpus global explicité : 22 052 incidents, dont 12 195 violations confirmées. Le texte précédent disait « comprend », pas « est constitué de » : il n’excluait pas les incidents, mais la précision lève l’ambiguïté. 20 % reste borné aux violations analysées ; aucune probabilité locale ni dernier millésime revendiqué.
- **ENISA — précision maintenue.** Le guide est non contraignant, non la directive. L’invitation à consulter les autorités figure dans le corps récupéré ; la paraphrase n’est pas présentée comme citation littérale.
- **Incitation personnelle du CISO — non ajoutée.** Piste valable pour la prose future, mais aucun cas ne l’étaye ici et elle ajouterait un procès d’intention au raisonnement sur les coûts futurs. Les contraintes légitimes sont déjà présentes.
- **Achats — correction finale GPT.** Une exigence indispensable ne devient pas facultative parce que le favori échoue. Sa révision exige l’autorité habilitée et doit rester permise par le droit et les engagements applicables. Cette clarification répond aussi au contrôle du parent ; elle n’a pas été renvoyée à Grok.

## Contrôle final GPT

La base finale aide à écrire : cas placés, mécanismes, limites et choix opposables. Sa régularité reste visible et ne doit pas être copiée telle quelle en prose. Chapitre 3 : capacité et sortie ; chapitre 5 : coexistence financière et charge ; chapitre 6 : contrainte d’achat et réversibilité. Aucun cas d’achat inventé pour masquer l’absence de source. Voix directe de CISO, sans prétendre authentifier la voix personnelle d’Oussama. Pas de score de qualité artificiel.

Les corrections sont des clarifications ciblées, pas une nouvelle thèse. La version finale n’a pas reçu de seconde revue Grok. SHA-256 final de la base : `ad6df0e075a7c28c95e1eb396774199c18a6703293f0d209554841a879eb4d29`.

## Vérification et publication

Le [contrôle actuel](../../verification.json) remplace les anciens comptes sans sous-puces. Le script contrôle les neuf fiches, les trois axes et leurs trois développements, les liens locaux actifs et les ancres de citation, les empreintes du dossier et du prompt, les cartes et le périmètre français. Audit séparé `sources.py verify --strict --evidence` avec ledger filtré : identifiants et extraits, non certification sémantique. Lecture des limites et des affirmations effectuée en complément. Pages intégrales et PDF exclus de la publication. Notification externe laissée au parent ; aucune notification envoyée par ce sous-agent.
