# Journal — lecture et intégration BRKSEC-1785

23 novembre 2026. Périmètre : `books/ciso-fr` seulement. État initial propre, branche `main`, HEAD et référence distante vérifiée : `83b490e23aff0e627ed29ced3915ae3847f22c35`.

## Lecture et sélection

PDF exact fourni par l’auteur téléchargé ; 62 pages extraites et lues, huit rendus inspectés. Les outils PDF étaient absents : installation de PyMuPDF, puis utilisation explicite de l’interpréteur qui le possède, sans modifier le dépôt. Le champ auteur technique du fichier n’a pas remplacé les deux intervenants de couverture. Numéros physiques PDF explicités, notamment parce que la page 53 affiche le numéro 58.

Sept idées retenues dans les chapitres 3–7 ; chapitres 1–2, titres des axes, introduction et conclusion inchangés. Neuf fiches synchronisées ; seules les cinq fiches concernées changent. Mind map et SVG conservés parce que les axes ne changent pas ; validation XML, pas nouveau rendu prétendu. Les PDF et extractions ne sont pas redistribués.

## Confrontation réelle

Auto-critique : `gpt-6-astra`, modèle déclaré par le runtime. Deux appels API indépendants au rédacteur : modèle demandé et retourné `grok-4.7`, fin `stop`. Les fichiers JSON conservent empreintes et usages ; dossiers et prompts complets sont archivés, sans troncature volontaire. Grok reçoit la base entière, la carte, la note Cisco et le registre historique, pas le PDF complet. Il n’effectue aucune recherche web dans ces appels.

### Première revue : décisions

1. **Attribution : adoptée.** Chaque référence Cisco est placée sur l’énoncé fournisseur, avant le prolongement auteur. Priorité Internet puis métier rétablie ; « agents d’opérations IT » évite l’ambiguïté d’exploitation offensive. L’extrait de p. 35 décrit bien un chemin d’exploitation spécifique, mais la base préfère une paraphrase plus simple.
2. **Plages de pages : adoptée.** Plan commun p. 26, feuille de route p. 38, protection p. 34–37 ; les autres plages restent utiles pour une idée combinée et sont détaillées dans la note source.
3. **Panne et cadence : partiellement adoptée.** Plan de contrôle harmonisé et « pas panne démontrée » explicité. Pas de changement du titre modal « peuvent tomber ensemble » : le texte distingue déjà cas mono-fournisseur et recherche de dépendances entre contrats. Rejet de la lecture qui limiterait p. 43 aux seules opérations internes Cisco : le corps de la slide énumère les versions NOS et les divulgations aux clients. Il reste une annonce, pas un calendrier constaté.
4. **Urgence et Gartner : partiellement adoptée.** Le critère de décision sans attendre un achat est remis en tête. DBIR conservé avec population et limites, sans prétendre choisir une mesure locale à partir du pourcentage. Le titre Gartner n’est pas une attribution factuelle ; aucune assertion Gartner non vérifiée ajoutée.
5. **Conclusion et carte : non retenue.** La reprise est un choix conditionnel délibéré de conclusion, pas une synthèse exhaustive ; le retrait après preuve est compatible avec la trajectoire préexistante. Cette intégration ne justifie pas une réécriture globale.
6. **Formules trop “slides” : préférence reconnue.** Les formules proposées sont déjà facultatives et explicitement éditoriales. Ne pas les multiplier ; ne pas prétendre qu’elles sont de l’auteur.

### Seconde revue et précisions finales

La [contre-revue finale](grok-final.md) ne relève pas de défaut bloquant. Trois précisions adoptées ensuite, sans troisième appel : « constats vérifiables » sans guillemets de citation ; les trois centres Cloudflare explicitement rattachés au plan de contrôle et à l’analytique ; critère Cisco de retrait complété par impossibilité de corriger ou mettre à niveau et précautions infrastructures critiques/OT. Elles ne changent ni argument ni décision ; vérification GPT contre les preuves, pas validation Grok de la version publiée. Les dossiers envoyés restent immuables.

## Véracité : ce qui n’est pas certifié

Les chiffres du PDF sur délai d’exploitation, parc vieillissant, top vulnérabilités et temps de correction sont omis faute de recoupement original dans cette passe. Les diagrammes ne prouvent pas des taux de protection. Les promesses de produits et de modèle ne deviennent pas des performances observées. Les cas historiques restent dans les limites de leur registre, sans nouvel audit externe.

Une recherche telco distincte a été confiée en parallèle puis signalée disponible en fin de boucle. Elle n’est ni consommée ni intégrée ici : son intégration ferait une nouvelle passe de sources, de citations et de revue. Le parent conserve le suivi de `telco-verification` et ses propositions. Ce commit n’est pas présenté comme le fact-check telco des cinq dernières années. Pas de notification externe séparée dans cette sous-tâche ; compte rendu au parent.

## Vérifications et publication

Le [vérificateur actif](verify.py) contrôle les comptes, les neuf fiches, les liens/ancres locaux, les citations Cisco, les empreintes des deux revues, le périmètre et les SVG inchangés. Les comptes et l’empreinte de la base finale sont dans [verification.json](../../verification.json). Les sources brutes restent hors dépôt. Publication autorisée sur `main` ; la confirmation SHA distant et égalité octet par octet de tous les fichiers modifiés sera rapportée après lecture distante effective, pas déduite de ce journal prépublication.
