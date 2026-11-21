# Revue de fond — ce qu’un CISO senior ne trouve pas encore

**Fait** = dans le dossier. **Déd.** = inférence. **Reco** = à écrire. **Préf.** = choix du reviewer, pas un résultat.

Le dossier tient déjà l’anti-slides. Le risque n’est plus la naïveté : c’est une hygiène décisionnelle que le lecteur cible pratique déjà. Manquent le portefeuille corrélé, le coût d’attendre, la preuve qui expire, l’économie de transition, la décision perdue, le legacy non remplaçable, le fournisseur plus fort que l’acheteur.

## 1 — Board
- **Objection.** « Options, incertitude, pas d’immunité » est le discours board déjà tenu. La fiche compare encore un projet à la fois. **Déd.** Trois résiduels « acceptables » sur identité, sauvegarde et infogéreur sont souvent *un* scénario.
- **Approfondissement.** Covariance : même IdP, même région, même MSSP, même exclusion d’assurance, même personne rare. Le board n’achète pas une tolérance ; il achète une corrélation qu’on ne lui montre pas.
- **Dilemme.** Diversifier vers une indépendance que personne n’exploitera, ou assumer une corrélation opérable et moins chère. Décision : parfois *recommander* la concentration, et nommer le scénario unique qu’elle crée — pas financer trois logos pour la slide d’indépendance.
- **Outil.** Fiche de covariance : pour les quelques scénarios de perte déjà retenus, une colonne « défaillance partagée » à travers les contrôles financés. Colonne vide = arbitrage incomplet. Silence du board = option déjà en vigueur, nommée.

## 2 — Standards
- **Objection.** Droit / guide / clause : nécessaire et déjà fait. Pousser 24 h / 72 h / un mois, c’est le séminaire que le livre doit éviter. « Préparer la notification avant l’incident » est trop évident.
- **Approfondissement.** Biais et expiration. Une preuve capturable pour l’audit n’est pas un contrôle vivant. Une preuve de quatorze mois sous une autre architecture d’identité est une archive. **Fait** : trois niveaux de preuve ; pas de règle quand le niveau 3 redevient faux.
- **Dilemme.** Alerte précoce possiblement excessive versus notification tardive. Si l’attente d’une qualification complète dépasse le plafond du régime *déjà qualifié applicable*, on envoie l’alerte incomplète et on corrige. Attendre pour ne pas se tromper est une décision, pas de la prudence.
- **Outil.** Demi-vie : pour chaque contrôle, conditions d’invalidation (identité, périmètre, propriétaire, config). Pas un score. **Reco** : ne pas rouvrir l’opposabilité française.

## 3 — Investissements
- **Objection.** « Le sunk cost ne justifie pas le renouvellement » est juste et trop connu. Le piège : « remplacer » est souvent faux, parce que détections, preuves et playbooks vivent dans le schéma du fournisseur.
- **Approfondissement.** Legacy : l’actif n’est pas le produit, c’est le chemin d’exception non documenté. Le changer de logo sans le chemin recrée la dette. Cash de licence faible peut cacher journaux et API ; cash élevé peut être le seul moyen de ne pas consumer l’unique équipe de migration.
- **Dilemme.** Renouveler ce qu’on n’achèterait plus, parce que la sortie détruit une piste de preuve ou une attestation non reprise. Décision : payer le renouvellement *et* une preuve de sortie bornée — ou cesser d’appeler « remplacer » une option.
- **Outil.** Vérité de sortie, une page : ce qui casse au jour 1 du non-renouvellement (détection, logs, attestation, compétence). Page blanche = otage, pas arbitrage. Coût irrécupérable ≠ coût de transition encore évitable.

## 4 — Veille
- **Objection.** Trois files et « la démo n’est pas l’essai » : catéchisme. Le lecteur veut la règle quand l’information achetée par l’essai vaut moins que le dommage non annulable.
- **Approfondissement.** Attendre une date cryptographique prophétique est déjà écarté ; l’autre erreur est d’attendre alors que des données sensibles sont déjà collectables. Un pilote tenu par l’ingénieur du fournisseur expire quand il part. Plusieurs explorations sur le même lac et le même IdP ne sont pas de la veille : c’est de la corrélation.
- **Dilemme.** Agent borné avec résidu irréversible — **Fait**, une divulgation ne s’annule pas — versus refus qui laisse l’ombre métier sans coupure. Si l’usage est déjà politiquement acquis, sponsoriser le pilote étroit peut être le moindre mal. La prudence qui ne dit que non crée le pire système.
- **Outil.** Ticket d’irréversibilité avant essai : actions non défaisables, propriétaire, arrêt qui ne prétend pas les annuler. Plafonner la valeur d’information par ce ticket. Plafond dépassé au design = bibliothèque seulement, pas d’essai.

## 5 — Budget
- **Objection.** Trois budgets et liste d’arrêts : le chapitre le plus fort, encore trop poli. La capacité rare n’est souvent pas dans l’équipe sécu. Sans accord écrit du propriétaire externe, le plan est une fiction.
- **Approfondissement.** L’austérité concentre. Couper cinq petits contrôles peut faire porter tout le résiduel par un IdP, un backup ou un MDR. Payer le MDR en supprimant le seul contradicteur interne : **Déd.** on achète un récit, pas une couverture.
- **Dilemme.** Violer un standard interne historique pour tenir le plancher légal, et le dire comme désaccord imposé. Décision : publier les services qui perdent la couverture. Adoucir la liste pour rester « partenaire », c’est le problème du CISO.
- **Outil.** Grand livre : chaque engagement a un détenteur hors sécurité qui a accepté la charge. Pas d’acceptation = hors plan. Après arrêts, une ligne « défaillance unique désormais dominante ». Si elle empire, la coupe est rejetée même si le cash baisse.

## 6 — Fournisseurs
- **Objection.** « Ne pas acheter le coin supérieur droit » est le titre le plus prévisible du genre. **Fait** : la FAQ est déjà un point de départ, pas un mandat. Une hygiène de grille fait décrocher.
- **Approfondissement.** Accord-cadre, remise conditionnée à la suite, refus du protocole d’essai, sortie non négociable ce cycle. La preuve locale perd contre le cash groupe. Pérennité peut battre la fonction ; le dossier ne dit pas quoi faire quand on ne peut pas refuser.
- **Dilemme.** Pire adéquation dans un contrat non sortable cette année, ou spécialiste qu’on ne saura pas opérer. Décision : prendre le fournisseur puissant *et* l’artefact qui préserve un futur non (export exploitable, admin de reprise hors de son tenant, copie des journaux). Pas d’indépendance d’affichage.
- **Outil.** Carte de pouvoir avant toute pondération : qui peut encore dire non, ce qui est signé, quelle remise meurt hors suite. Si personne ne peut écarter le favori, on n’ouvre pas la matrice ; on négocie mode dégradé et sortie. **Préf.** : une phrase sur le quadrant, pas une méthode.

## 7 — Gouvernance
- **Objection.** Avis, autorisation, acceptation : juste, bientôt évident. Mou : la décision imposée, et le CISO qui perd.
- **Approfondissement.** Deux actes, une seule signature aujourd’hui. Devoir applicable ou sécurité des personnes : pas d’exécution, escalade, trace. Désaccord d’appétit : l’autorité tranche, on exécute, on date l’hypothèse qui renverserait, on ne relance pas chaque semaine. Les exceptions sont l’architecture ; les faire expirer au changement matériel (flux, agent, sous-traitant), pas seulement au calendrier.
- **Dilemme.** Double signature sans horloge : sécurise, ou attaque la disponibilité depuis la fonction risque. Toute validation sans réponse a une conservatoire pré-autorisée ou un suppléant. Centraliser l’irréversible ; déléguer le réversible même si le CISO « signerait mieux ».
- **Outil.** Bordereau contrarié, deux cases : « contraire à un devoir applicable » / « au-delà de la tolérance approuvée ». Case 1 : pas d’exécution. Case 2 : exécution sous autorité nommée + revue datée. Ajouter au jeu d’exercice le cas « le métier passe outre ».

## Le CISO comme problème
- **Preuve.** Exiger une preuve locale complète pendant une exposition active : attendre coûte plus que l’information. La décision provisoire de l’introduction doit valoir *contre* les fiches du CISO.
- **Outils.** Si cinq états et protocoles retardent la révocation d’un jeton, l’outil est le contrôle fictif.
- **Indépendance.** Outsider choisi pour l’affichage, assurance injoignable en incident, veto sans suppléant : indépendance non opérable = risque en plus.
- **Prudence.** Ticket, revue d’exception et double signature comme frein universel. Sans horloge ni issue par défaut, c’est de l’évitement. **Reco** : chaque frein a un délai et une issue si le délai tombe.

## Trois angles manquants
1. **Portefeuille corrélé** comme entrée de roadmap, pas comme tension en bas de mind map. Sinon A/B/C/D échouent ensemble.
2. **Asymétrie de pouvoir** (hyperscaler, IdP, assureur, accord groupe) au même rang que le droit — pas seulement une technique du ch. 6.
3. **Le CISO perdant** : recommandation rejetée, exploitation quand même sûre, hypothèse de révision écrite avant la réunion. La conclusion sous-écrit encore la victoire.

Pas de chapitre 8. Covariance en 1 et en roadmap ; pouvoir en 6 et dans la sortie du 3 ; défaite en 7 et dans la dernière fiche auteur.

## Couper
- Minutage NIS 2 et variante prestataires de confiance : garder la conséquence, renvoyer à [14].
- « Inversion » répétée sept fois : un patron en introduction ; une inversion seulement là où la décision change (3, 5, 7).
- Commentaire du flowchart : le schéma suffit. Le narrer recrée l’ordre universel que le dossier refuse.
- Allonger Gartner ou la littérature d’évals d’agents : les réserves actuelles sont le bon dosage.
- **Préf.** : ne pas ajouter d’ironie ; en couper deux si le fond nouveau entre.

## Cinq priorités de refonte
1. Covariance des dépendances : entrée manquante de la roadmap et de la fiche board.
2. Coût d’attendre et irréversibilité comme critères (1, 4, 7), pas comme morales.
3. Retourner le ch. 6 : de l’anti-quadrant vers l’acheteur plus faible que le fournisseur.
4. Séparer devoir et appétit ; outiller la défaite du CISO.
5. Faire expirer preuves et pilotes ; raccourcir le droit déjà qualifié. Le fond libéré va au legacy et à la transition.

## Deux conseils à ne pas ajouter
1. Pas de maturité, de RACI enrichi, ni de risque monétisé « pour la finance ». ROI mesurable oui, ROI inventé non — une formule sans données locales est un concours de slides inverse.
2. Pas de chapitre menaces 2026 ni de traité des agents. **Fait** : l’ENISA cadre des familles, pas une probabilité locale. L’agent reste un cas du ch. 4, sous l’autorité du ch. 7.

**Préf. de fermeture.** Le livre devient distinctif quand une recommandation dit : concentrez, renouvellez l’otage, envoyez l’alerte incomplète, publiez l’arrêt, signez avec le fournisseur trop fort, exécutez après avoir perdu — et la condition qui ferait changer d’avis est écrite avant la réunion, pas après l’incident.