# Votre risque n’a pas lu le Magic Quadrant

## Petit manuel de lucidité pour CISOs : menaces réelles, innovation utile et budgets qui ne se multiplient pas en réunion

**Premier jet intégral — Français — Recherche arrêtée au 20 novembre 2026**

### Note au lecteur

- Les scènes d’ouverture sont des **fictions pédagogiques**. Leurs personnages, dialogues, entreprises et données internes sont inventés pour mettre un arbitrage à l’épreuve. Ce ne sont ni des témoignages clients ni des incidents reconstitués.
- Les faits publics sont présentés séparément, avec des références. Un rapport décrit son échantillon et sa période d’observation, pas la probabilité d’incident de votre entreprise.
- Les recommandations et outils de décision sont les propositions de ce livre, pas des exigences réglementaires supplémentaires. Vous en avez probablement assez.
- Le chapitre réglementaire ne remplace pas une analyse juridique de votre périmètre, de votre pays et des textes applicables à la date de décision.
- CISO et RSSI désignent ici la fonction de direction de la sécurité. Son périmètre d’autorité varie selon les organisations ; ce livre ne suppose pas qu’elle possède tous les budgets, toutes les infrastructures et une réserve secrète de développeurs.

## Sommaire

- **Introduction — La sécurité ne manque pas de solutions. Elle manque parfois de questions.**
- **Chapitre 1 — Le CISO challengé par le board.** Décider plutôt que rassurer à tout prix.
- **Chapitre 2 — Le CISO bouffé par les standards.** Rendre la conformité utile sans lui donner les clés de la stratégie.
- **Chapitre 3 — Le CISO qui veut trop valoriser ses investissements.** Distinguer ce qui a été acheté de ce qui protège.
- **Chapitre 4 — Le CISO perdu dans la veille techno.** Transformer l’innovation en hypothèses testables.
- **Chapitre 5 — Le CISO qui n’a pas d’argent.** Choisir ce qui ne sera pas fait, sans appeler cela une optimisation.
- **Chapitre 6 — Le CISO qui se protège avec le Gartner en haut à droite.** Utiliser un classement sans lui déléguer son jugement.
- **Chapitre 7 — Le CISO qui décide de tout et de rien.** Distribuer les décisions sans distribuer l’irresponsabilité.
- **Conclusion — Une roadmap, pas une collection de bonnes intentions.** Passer des sept situations à quatre chantiers défendables.

# Introduction — La sécurité ne manque pas de solutions. Elle manque parfois de questions.

Vous entrez dans une réunion avec un problème de sécurité. Vous en sortez avec un comité, une démonstration et la promesse d’une plateforme unifiée. Le problème, qui n’avait pas été invité à la démonstration, continue tranquillement sa carrière.

Personne n’a nécessairement mal travaillé. Le fournisseur a présenté son offre. Les achats ont négocié. L’architecture a vérifié la compatibilité. Le CISO a défendu son budget. Le directeur financier a obtenu une remise. Tout le monde a rempli sa mission. Il reste à découvrir si l’entreprise est mieux protégée.

C’est le sujet de ce livre.

Pas la dénonciation des vendeurs, qui vendent, activité finalement assez cohérente avec leur intitulé de poste. Pas le procès des analystes, des normes ou de l’intelligence artificielle. Pas davantage une invitation à revenir au pare-feu de notre jeunesse, qui aurait tout compris avant les autres.

Le problème commence lorsque nous confondons trois choses : **ce qui menace l’entreprise, ce qui rassure son organisation et ce que le marché sait lui vendre**. Ces ensembles se recoupent. Ils ne sont pas identiques.

Un investissement peut rendre la sécurité plus visible sans la rendre plus efficace. Une exigence de conformité peut corriger un véritable angle mort. Une technologie très médiatisée peut être exactement ce qu’il nous faut. Et un contrôle parfaitement banal peut être mal adapté à notre métier. La lucidité ne consiste donc pas à détester la nouveauté. Elle consiste à lui demander de travailler.

### Les attaquants ne sont pas tenus de respecter notre plan stratégique

L’ENISA souligne, dans sa présentation du panorama 2026, la persistance des rançongiciels, de l’ingénierie sociale et de l’exploitation de vulnérabilités, ainsi que le rôle des dépendances numériques dans la propagation des incidents. Cette édition analyse des événements observés pendant l’année 2025 : le millésime du rapport n’est pas celui de toutes ses observations.[1]

La même source décrit le double rôle de l’IA : un outil facilitant certaines activités malveillantes et une source d’exposition supplémentaire lorsqu’elle entre dans les environnements des entreprises.[1]

Ces deux constats tiennent ensemble. Il n’est pas nécessaire de choisir entre « tout a changé » et « rien n’a changé ». Une nouvelle capacité peut accélérer un vieux mécanisme, ouvrir une nouvelle possibilité ou déplacer le coût d’une attaque. Il faut déterminer laquelle de ces évolutions modifie nos décisions.

Un compte prestataire trop puissant ne devient pas moins dangereux parce que son abus est conventionnel. Un agent logiciel capable d’agir sur la production ne devient pas inoffensif parce qu’il porte le mot « copilote ». Inversement, une nouveauté anxiogène ne mérite pas automatiquement une ligne budgétaire.

Notre unité de travail sera donc le **scénario de perte** : une activité importante, un mécanisme d’échec plausible, des conséquences et des moyens de prévention, de limitation ou de reprise. Pas le nom d’une catégorie de produits.

### Sept situations, une seule question

Les personnages des chapitres suivants ne sont pas des incompétents. Ils essaient de faire fonctionner une entreprise avec des contraintes contradictoires.

- Le board demande une certitude que personne ne peut honnêtement fournir.
- Les obligations demandent des preuves, et les preuves finissent par occuper ceux qui doivent faire fonctionner les contrôles.
- Les investissements passés deviennent des arguments pour les investissements suivants.
- La veille produit plus de pistes qu’une équipe ne peut en évaluer.
- Le budget impose des renoncements que les présentations préfèrent appeler des synergies.
- Les classements apportent une caution commode lorsque la décision est difficile à défendre.
- Le CISO, voulant éviter les angles morts, finit par devenir le point de passage de chaque décision.

Le fil rouge sera toujours le même : **quelle décision améliore réellement la situation, avec quelles preuves et au prix de quel renoncement ?**

Le renoncement compte. Un projet ne consomme pas seulement de l’argent. Il mobilise les gens qui pourraient en mener un autre. L’intégration d’une plateforme peut prendre le temps prévu pour tester la reprise. Une collecte de journaux sans exploitation peut occuper le budget d’un contrôle d’accès. Une réunion peut empêcher une autre réunion, ce qui constitue parfois son principal bénéfice.

### Ce livre ne promet pas une formule magique

Vous n’y trouverez pas un score universel transformant des incertitudes en vérité à deux décimales. Vous trouverez des questions à poser, des contradictions à rendre visibles et des critères d’arrêt. Un pilote qui conduit à ne pas acheter peut être un excellent pilote. Un renouvellement bien justifié peut être plus innovant qu’une migration sans raison.

Chaque chapitre commence par une scène fictive suffisamment détaillée pour montrer les intérêts en présence. L’analyse distingue ensuite les erreurs de raisonnement des contraintes légitimes. Les recommandations précisent ce qu’il faut décider, qui doit le porter et quelle preuve peut faire changer d’avis. Une fiche finale permet de réutiliser le raisonnement sans relire tout le chapitre avant le prochain comité.

L’objectif n’est pas de vous apprendre à gagner toutes les discussions. Un CISO qui gagne toutes les discussions risque surtout de les avoir organisées sans les bonnes personnes.

L’objectif est de vous aider à construire une sécurité **explicable, exploitable et révisable**. Explicable au dirigeant qui doit arbitrer. Exploitable par les équipes qui devront vivre avec. Révisable lorsque les faits changent.

Vous pouvez garder vos tableaux de bord. Nous allons simplement leur demander de répondre à une question.

---

# 1. Le CISO challengé par le board

## Mise en situation

*La scène qui suit est entièrement fictive. L’entreprise, ses personnes, ses chiffres et ses décisions sont inventés pour explorer un arbitrage, pas pour raconter un incident réel.*

À huit heures cinquante, Nora relit sa présentation dans le couloir. Elle dirige la sécurité de Méridienne Pièces, un distributeur industriel qui promet des livraisons rapides à des ateliers rarement patients. Son dossier compte trente diapositives. La dernière contient une demande budgétaire. Les vingt-neuf précédentes constituent, dans son esprit, un chemin pédagogique. Dans celui du directeur financier, elles risquent de constituer un tunnel.

Le conseil a prévu vingt minutes. Nora a répété pendant quarante. Elle connaît déjà la première question : sommes-nous protégés ? Elle a préparé une réponse sur la maturité, les menaces et les investissements. Ce matin, pourtant, le président change légèrement de formulation.

— Si nous approuvons votre programme, qu’est-ce que nous pourrons faire que nous ne pouvons pas faire aujourd’hui ?

Nora affiche son graphique. Plusieurs courbes montent. Une administratrice rapproche ses lunettes.

— Ce sont des progrès techniques, reprend le président. Je vous demande ce que cela change pour l’entreprise.

Le directeur général intervient. Méridienne doit ouvrir un portail permettant aux clients de consulter les stocks et de commander directement. Le lancement commercial précède un salon professionnel. Trois grands comptes attendent une démonstration. La sécurité demande une revue des accès et un exercice de restauration. L’équipe du portail affirme ne pas pouvoir tout terminer avant le salon.

— Est-ce que vous bloquez le lancement ? demande le directeur général.

Voilà. En quelques secondes, la responsable d’un risque collectif est devenue propriétaire présumée du bouton rouge. Nora regarde Éric, le directeur des opérations. Il surveille son téléphone. Elle lui avait demandé combien de temps les dépôts pourraient préparer les commandes sans le système central. Il avait répondu que ses équipes étaient débrouillardes. C’était rassurant, mais difficile à chronométrer.

— Je recommande de ne pas ouvrir immédiatement toutes les fonctions, dit-elle. La consultation des stocks peut être séparée de la prise de commande. Le deuxième service dépend de comptes techniques dont nous n’avons pas terminé la revue.

— Nous avons pourtant acheté une solution de gestion des identités, répond le directeur financier.

— Oui. Nous n’avons pas encore attribué tous les comptes à des responsables ni supprimé les exceptions historiques.

— Donc nous avons payé sans être protégés ?

Nora hésite. Elle pourrait défendre son bilan, expliquer les changements de périmètre et rappeler les postes non remplacés. Tout serait exact. Rien ne répondrait à la question posée. Elle ferme le graphique et ouvre une page presque vide.

— Nous avons acheté une capacité. Nous n’avons pas fini de l’exploiter. Aujourd’hui, je vous propose de choisir entre trois trajectoires, pas entre la sécurité et le commerce.

La première conserve la date et réduit le périmètre : consultation seulement, puis commandes après vérification. La deuxième conserve le périmètre mais décale le lancement. La troisième conserve les deux, avec une exposition supplémentaire et un dispositif de surveillance temporaire qui ne remplace pas la correction. Nora recommande la première. Elle précise que certaines obligations ne pourraient pas être écartées par un vote ; son arbitrage porte ici sur des options qu’il reste à valider avec le juridique.

Éric pose enfin son téléphone.

— Avec la consultation seule, les commandes continuent de passer par nos équipes. On absorbe le volume habituel, mais pas la campagne promotionnelle.

— Alors le coût du périmètre réduit dépend aussi de la campagne, répond Nora. Je ne peux pas le calculer seule.

La directrice commerciale intervient. Elle peut limiter l’annonce aux clients pilotes. Elle n’aime pas cette option, mais préfère une démonstration réduite à une promesse immédiatement démentie. Pour la première fois depuis le début de la séance, la discussion ne porte plus sur le nombre d’alertes.

Le directeur financier revient au budget.

— Et votre plateforme de détection augmentée ?

— Je propose de reporter l’achat, dit Nora. Finançons d’abord les accès et la reprise. Nous mesurerons ensuite ce qu’une nouvelle plateforme doit améliorer.

— Vous demandez de ne pas acheter ?

— De choisir. Une licence ne libère pas les personnes qui doivent la configurer.

L’administratrice chargée du comité d’audit demande ce que prouvera l’exercice. Nora décrit une commande fictive, son traitement dans un environnement de reprise et la vérification du résultat par les opérations. Restaurer un serveur ne suffira pas : il faudra retrouver un service utilisable, avec des données cohérentes et une équipe capable de travailler.

— Et si l’essai échoue ?

— Nous aurons une information désagréable avant d’en avoir une urgente.

Éric demande qui organisera le test. Nora propose une responsabilité partagée mais pas diffuse : l’informatique restaure, les opérations valident, la sécurité observe les conditions et les écarts. Le directeur général désigne un responsable de coordination. Une date est inscrite. Cette petite ligne dans le compte rendu semble moins spectaculaire que la plateforme ; elle engage davantage de monde.

Reste la question du président.

— Après tout cela, pourrez-vous nous dire que nous sommes en sécurité ?

— Je pourrai vous dire ce qui a été testé, sur quel périmètre, et ce qui reste inconnu. Je ne pourrai pas garantir qu’aucun incident ne surviendra.

— Ce n’est pas très vendeur.

— Non. Mais cela vous permettra de décider sans acheter une certitude que personne ne possède.

Le conseil ne tranche pas tous les détails techniques. Il demande à la direction de mettre en œuvre le lancement réduit, dans le cadre de ses délégations, et de revenir si le test révèle une incapacité majeure. Le compte rendu distingue la décision, ses hypothèses et la condition de réexamen. Nora sort sans feu vert universel. Elle repart avec des responsabilités, une priorité financée et une promesse commerciale plus modeste. Sa présentation aura servi pendant six diapositives. Les autres attendront une occasion moins utile.

## Ce qui se passe vraiment

Le conseil ne manque pas nécessairement de culture cyber lorsqu’il demande « combien cela rapporte ». Il cherche parfois, maladroitement, à comparer des emplois concurrents de ressources limitées. Le CISO échoue s’il répond seulement par une liste de menaces ; le conseil échoue s’il exige une certitude financière impossible à produire. Entre les deux, il existe un travail sérieux : rendre les options comparables sans effacer leurs inconnues.

Le NIST présente son Cybersecurity Framework comme un moyen de comprendre et d’améliorer la gestion du risque cyber ; son centre de ressources propose notamment des profils pour structurer cette démarche.[6] Cela n’en fait ni une recette budgétaire ni une assurance contre l’incident. Un référentiel fournit un langage ; la direction doit encore expliquer quel service elle protège, pour quelle conséquence redoutée et avec quelle tolérance à l’interruption.

L’incident public de Marks & Spencer donne une mesure de cette traduction économique. Le 21 mai 2025, le *Guardian* rapporte que l’entreprise estime alors à 300 millions de livres l’impact sur ses profits et prévoit des perturbations de son activité en ligne jusqu’en juillet.[7] Il s’agit d’une estimation annoncée à cette date, pas d’un coût final certifié. L’article rapporte également un objectif de réduction de l’impact par l’assurance, les économies et d’autres actions.[7] Confondre dommage brut, indemnisation espérée et perte nette serait déjà une mauvaise conversation financière.

Ce cas ne démontre pas qu’un équipement précis aurait empêché l’attaque, ni qu’une entreprise différente doit dépenser une fraction de cette somme. Il rappelle plutôt que le risque se matérialise dans des ventes interrompues, des opérations désorganisées et des choix de reprise. Transformer le malheur d’un distributeur en devis universel serait une forme particulièrement pressée de conseil.

La quantification reste utile. Une fourchette de pertes, construite avec les finances et les métiers, vaut mieux qu’un adjectif rouge foncé. Mais une probabilité fragile multipliée par un impact fragile ne devient pas robuste grâce à deux décimales. Il faut montrer les hypothèses, distinguer les observations des estimations et tester ce qui ferait changer la décision. Le retour sur investissement peut être défendable pour supprimer une dépense ou économiser du travail mesuré. Il devient plus incertain lorsqu’on prétend chiffrer exactement les catastrophes qui n’auront pas eu lieu.

Autre concession nécessaire : le conseil ne peut pas examiner chaque compte technique. Il doit recevoir une synthèse. La simplification n’est pas le problème ; l’effacement du périmètre l’est. Un indicateur vert peut être honnête s’il signifie « objectif atteint sur les services testés ». Il devient trompeur s’il suggère « entreprise sûre ».

Enfin, « le board » n’est pas un rôle juridique universel. Selon la structure et les délégations, supervision, arbitrage et exécution se répartissent différemment. Le CISO doit faire préciser ces responsabilités plutôt que distribuer des signatures de décharge. Une acceptation interne du risque n’autorise pas, à elle seule, à ignorer une obligation applicable.

## Les erreurs classiques

- **Vendre une immunité.** Promettre l’absence d’incident rend chaque événement incompatible avec le discours précédent.
- **Faire porter le risque au messager.** Le CISO conseille et alerte ; il ne possède pas automatiquement les décisions commerciales ou les moyens de production.
- **Comparer seulement les prix d’achat.** L’intégration, les personnes, la maintenance et la sortie du contrat comptent aussi.
- **Utiliser un incident célèbre comme calculateur.** Une perte publique éclaire un scénario ; elle ne fournit pas la probabilité locale.
- **Accepter sans échéance.** Une exception sans responsable ni date devient une architecture officieuse.

## Faire autrement

**Préparer une décision, pas une visite du centre de supervision.** Pour chaque sujet soumis à la direction, le CISO rédige une page avec le service concerné, le scénario, les faits observés, les inconnues et les options. Le responsable métier valide les conséquences opérationnelles ; les finances challengent les ordres de grandeur. L'autorité compétente tranche dans ses délégations.

**Financer une capacité démontrable.** Le DSI chiffre les ressources complètes, pas seulement les licences. Les opérations définissent le résultat attendu : traiter une commande après restauration, révoquer effectivement un accès ou maintenir un fonctionnement dégradé. La preuve est un résultat daté et reproductible, accompagné de ses limites. Le CISO explicite le risque résiduel au lieu d’annoncer une réduction magique.

**Organiser le renoncement.** Pour tout nouvel investissement important, présenter ce qui sera arrêté, retardé ou moins bien couvert. Un achat peut rester pertinent malgré une efficacité imparfaite : délai réglementaire, besoin client ou manque de personnel peuvent justifier une solution transitoire. La décision doit alors nommer cette contrainte et prévoir sa révision, pas transformer le provisoire en stratégie éternelle.

**Revenir après l’arbitrage.** Le secrétariat de l’instance conserve la décision et ses hypothèses ; un responsable opérationnel suit l’exécution. Au rendez-vous suivant, on compare résultat et attente. Si le test invalide l’hypothèse de reprise, le sujet remonte sans attendre le cycle budgétaire. C’est cette boucle, plus que le nombre de diapositives, qui rend la supervision utile.

## La fiche à emporter

**Une décision cyber présentable en sept cases**

- [ ] **Service :** quelle activité doit continuer, et pour quels utilisateurs ?
- [ ] **Scénario :** quel événement crédible empêcherait ce résultat ?
- [ ] **Connaissance :** quels faits avons-nous, et que supposons-nous encore ?
- [ ] **Options :** agir, réduire le périmètre, différer ; avec quels coûts complets ?
- [ ] **Limites :** quelles obligations ne peuvent pas être écartées et quel risque subsiste ?
- [ ] **Responsabilités :** qui décide, qui réalise, qui vérifie indépendamment du déclarant ?
- [ ] **Réexamen :** quelle date, quelle preuve et quel événement imposent de rouvrir le dossier ?

Si la dernière case est vide, vous n’avez pas une décision durable. Vous avez une préférence du jour, enregistrée dans un compte rendu.

---

# 2. Le CISO bouffé par les standards — NIS 2 et autres

## Mise en situation

*Cette scène est entièrement fictive. Sillage Santé, ses équipes et ses échanges sont inventés. Elle ne décrit ni un audit réel ni la situation réglementaire d’une entreprise existante.*

Lundi matin, Amel reçoit trois demandes de preuves avant même son premier café. Le commercial veut répondre au questionnaire d’un client. Le responsable qualité prépare un audit de certification. La direction juridique demande un état de préparation à NIS 2. Les trois messages comportent le mot urgent. Aucun ne précise ce qu’il serait acceptable de reporter. Chez Sillage Santé, éditeur de logiciels pour des établissements de soins, l’urgence est devenue un format documentaire.

Amel dirige la sécurité avec une petite équipe. Elle ouvre les pièces jointes. Dans le premier tableau, il faut décrire la politique de contrôle des accès. Dans le deuxième, démontrer la revue des habilitations. Dans le troisième, présenter la gouvernance des identités. Les questions se ressemblent suffisamment pour encourager le copier-coller, mais pas assez pour garantir une réponse juste. C’est une excellente configuration pour travailler deux fois et se tromper trois.

Laurent, responsable qualité, réclame une politique actualisée.

— Tu as déjà celle du mois dernier, répond Amel.

— Avec l’ancien logo. Et deux versions circulent : laquelle fait foi ?

Il marque un point. La semaine précédente, une procédure de départ périmée avait fait oublier un service de partage de fichiers. La maîtrise documentaire n’était pas seulement du folklore.

Le directeur commercial entre à son tour.

— Notre client demande si tous les accès sont revus chaque trimestre. Je peux répondre oui ?

— Non, répond Amel. Les accès privilégiés du service principal le sont. Pour les outils internes, nous avons encore des écarts.

— Il n’y a qu’une case oui ou non.

— Alors nous joignons une précision. Une case étroite ne rend pas une affirmation large plus exacte.

Il soupire. La signature du contrat est proche. Une réponse nuancée peut provoquer des questions, donc un délai. Amel ne méprise pas ce problème. Elle propose d’appeler le client avec lui pour comprendre si la demande concerne le service vendu ou toute l’entreprise. Le périmètre pourrait résoudre une partie du désaccord, sans repeindre les écarts.

À dix heures, la réunion NIS 2 commence. Une consultante présente un tableau de correspondances. Chaque ligne relie une exigence à un document. Beaucoup de cellules sont vertes. Le directeur général, Marc, paraît soulagé.

— Si je comprends bien, notre certification nous met presque à niveau ?

— Elle fournit des éléments réutilisables, répond Amel. Elle ne démontre pas automatiquement que toutes les obligations applicables sont satisfaites. Il faut vérifier le périmètre, les textes et ce que chaque preuve établit vraiment.

Inès, la juriste, confirme. Elle demande de distinguer le texte européen, les dispositions françaises effectivement applicables et les documents de préparation. Le tableau mélange pour l’instant des exigences, des recommandations et des demandes contractuelles. Tout est utile à connaître ; tout n’a pas le même statut.

La consultante acquiesce.

— On peut ajouter une colonne.

— Ajoutons surtout une règle, dit Inès. Aucune échéance présentée comme obligatoire sans sa base juridique et son périmètre.

Marc demande qui doit signer. Le mot flotte un instant dans la salle comme une solution universelle. Amel explique qu’une signature de direction peut approuver une politique ; elle ne prouve pas que les équipes l’appliquent. Inès ajoute qu’il faut identifier les responsabilités selon les textes et l’organisation, pas simplement demander au conseil de tout parapher pour faire sérieux.

Laurent propose un essai. Ils prennent une seule ligne : suppression des accès lors d’un départ. La politique existe. La procédure aussi. Le tableau indique conforme. Amel demande un exemple récent, choisi dans les départs enregistrés par les ressources humaines. Un ticket montre la fermeture du compte principal. Un autre confirme la récupération du matériel. Le compte d’un outil secondaire, lui, apparaît toujours actif.

— Donc la preuve n’est pas bonne ? demande Marc.

— Elle est excellente, répond Laurent. Elle prouve que notre conclusion était trop large.

La phrase détend la salle. Personne n’a envie de découvrir cet écart, mais il devient difficile de défendre la cellule verte. Amel fait modifier la ligne : dispositif partiellement appliqué, correction à réaliser, vérification à reprendre. Le responsable informatique reçoit l’action. Les ressources humaines doivent améliorer l’information transmise lors du départ. La sécurité ne récupère pas, par gravité, toutes les tâches qui embarrassent les autres.

Une preuve réutilisable doit conserver son périmètre. Les écarts spécifiques restent visibles. Le commercial demande une version communicable, sans données personnelles ni détails techniques inutiles.

— Et nous allons acheter une plateforme pour cela ? demande Marc.

— Peut-être plus tard, répond Amel. Aujourd’hui, nous ne sommes pas d’accord sur les propriétaires des contrôles. Une plateforme classerait très bien notre désaccord.

Ils commencent avec les accès, les sauvegardes et les incidents. Chaque responsable doit fournir une preuve produite par le travail réel, pas fabriquer une pièce uniquement pour la prochaine visite. Laurent garde la responsabilité du calendrier d’audit. Inès tient le registre d’applicabilité. Amel vérifie la cohérence technique et les risques non couverts.

En fin de réunion, le tableau a perdu plusieurs cases vertes. Il contient aussi moins de doublons, trois responsables clairement désignés et une liste courte de décisions. Marc observe que le taux de conformité vient de baisser en une heure.

— Le niveau de connaissance vient d’augmenter, répond Amel. Maintenant, nous pouvons améliorer le reste.

Son café est froid. Pour une fois, le dossier est un peu moins décoratif.

## Ce qui se passe vraiment

La documentation rend les pratiques vérifiables et moins dépendantes des personnes présentes. Elle n’est pas l’ennemie. Le problème commence lorsqu’on optimise le dossier plutôt que le fonctionnement qu’il doit décrire.

Le théâtre de la preuve confond trois choses : une règle existe, un mécanisme est installé, ce mécanisme fonctionne. Une politique de sauvegarde soutient la première proposition ; une configuration, la deuxième ; un test de restauration exploitable, la troisième. Aucune ne remplace automatiquement les autres.

### NIS 2 : séparer le droit, sa mise en œuvre et l’accompagnement

La prudence juridique n’est pas une note de bas de page. Lors de la consultation du 20 novembre 2026, le portail de l’ANSSI indique que la transposition française de NIS 2 est en cours, dans l’attente de l’ensemble des textes de transposition.[4] Il présente également le Référentiel Cyber France comme une version de travail susceptible d’ajustements liés aux discussions parlementaires et aux travaux réglementaires.[4] Ce constat décrit la page consultée ; il ne remplace pas une vérification juridique à la date d’une décision.

Il serait donc trompeur de présenter indistinctement toutes les lignes de ce document comme des obligations françaises définitives et immédiatement opposables. Il serait tout aussi peu raisonnable d’en déduire qu’il faut attendre pour savoir restaurer ses services. Le calendrier juridique et le calendrier des améliorations opérationnelles ne sont pas obligés de se tenir mutuellement en otage.

L’ANSSI précise que certaines entités numériques relèvent d’un règlement d’exécution européen spécifique plutôt que du socle national de mesures présenté sur son portail.[4] De son côté, l’ENISA explique, dans sa publication du 26 juin 2025, que son guide accompagne le règlement d’exécution 2024/2690 pour des catégories déterminées, notamment les fournisseurs cloud et les prestataires de services gérés.[3] Elle précise que ce guide n’est pas juridiquement contraignant et ne remplace pas les cadres nationaux.[3] Un document utile n’acquiert pas une portée universelle parce que son titre contient NIS 2.

Cette distinction vaut également pour les responsabilités et les notifications. Ne traduisez pas automatiquement « direction » par « conseil d’administration », ni « incident » par « toute alerte ». Le juridique doit préciser les organes concernés, la qualification de l’incident, le fait déclencheur, le destinataire et les délais de chaque régime applicable. L’ANSSI évoque, pour NIS 2, les incidents ayant un impact important et des rapports sur l’évolution de la situation.[4] Une fiche générique avec un chronomètre, sans ces conditions, donne surtout l’heure de la prochaine confusion.

### Mutualiser sans déclarer une équivalence imaginaire

L’ENISA accompagne son guide de correspondances avec des standards et référentiels.[3] C’est une base de travail, pas une permission de déclarer toutes les exigences satisfaites dès qu’un contrôle voisin existe. Deux textes peuvent traiter des accès tout en exigeant des populations, des modalités de validation ou des preuves différentes.

La bonne mutualisation porte sur le travail réel : un inventaire fiable, une revue exécutée, une décision approuvée. La mauvaise mutualisation gomme les différences pour faire tenir plusieurs obligations dans une case. Inversement, reconstruire le même inventaire pour chaque audit gaspille une ressource qui pourrait servir à vérifier son exactitude.

Un auditeur peut légitimement refuser une preuve ancienne, incomplète ou hors périmètre. Démontrer la correspondance et accepter un complément ciblé reste nécessaire. La sobriété documentaire vise le minimum suffisant pour travailler, contrôler et rendre compte honnêtement.

## Les erreurs classiques

- **Mettre tout au même niveau.** Une loi, un règlement, un guide, une certification et un engagement contractuel n’ont pas le même statut.
- **Transformer une correspondance en équivalence.** Un contrôle proche ne couvre pas nécessairement toute l’exigence.
- **Mesurer seulement les cases vertes.** Un périmètre réduit peut améliorer le score sans améliorer le service.
- **Produire les preuves la veille.** Les captures tardives racontent souvent la préparation de l’audit, pas le fonctionnement courant.
- **Acheter avant de répartir les rôles.** Un outil de conformité ne décide pas qui corrige un compte oublié.
- **Confondre partage et divulgation.** Une preuve utile à l’auditeur peut contenir des informations inadaptées à un questionnaire commercial.

## Faire autrement

**Créer un registre d’applicabilité.** Le juridique en est responsable, avec les métiers et le CISO. Pour chaque texte ou engagement : entité, service, juridiction, version, statut, date pertinente et justification. Une incertitude demeure visible jusqu’à résolution. La preuve attendue est une analyse datée, validée et reliée aux textes, pas une intuition dans un diaporama.

**Organiser un catalogue de contrôles.** Chaque contrôle reçoit un propriétaire opérationnel, un objectif et une méthode de vérification. La qualité ou la conformité relie les exigences à ces contrôles. Le CISO examine la pertinence technique. Les correspondances partielles restent partielles ; les compléments ont leur propre action et leur responsable.

**Faire produire la preuve par l’activité.** Un départ déclenche des tâches traçables ; une restauration conserve son résultat ; une revue d’accès enregistre les décisions et leur exécution. Le responsable du contrôle définit la fréquence adaptée et les événements imposant une nouvelle vérification. L’audit échantillonne et challenge. Les pièces mentionnent toujours le périmètre, la date et les limites.

**Arbitrer le coût documentaire.** Le responsable conformité mesure le temps consacré aux demandes répétées. Avec les achats et les métiers, il propose des réponses réutilisables et des modalités de partage sécurisé. Les exigences non négociables restent couvertes. Les demandes contractuelles supplémentaires font l’objet d’une discussion explicite : valeur du contrat, coût de production, confidentialité et charge récurrente.

## La fiche à emporter

**Une preuve, plusieurs usages, aucune magie**

Pour chaque élément conservé, vérifier :

- [ ] **Objet :** quelle affirmation précise cette pièce permet-elle de soutenir ?
- [ ] **Origine :** qui l’a produite, à quelle date et dans quel processus ?
- [ ] **Périmètre :** quels systèmes, personnes, services et périodes couvre-t-elle ?
- [ ] **Qualité :** prouve-t-elle l’intention, la mise en place ou le fonctionnement ?
- [ ] **Correspondances :** quelles exigences couvre-t-elle totalement ou seulement en partie ?
- [ ] **Écarts :** qui corrige, pour quand, et qui vérifiera le résultat ?
- [ ] **Diffusion :** qui peut la voir, sous quelle forme et pendant combien de temps ?

**Question de clôture :** si cette pièce disparaissait demain, perdrions-nous une connaissance opérationnelle, une démonstration nécessaire, ou seulement une décoration ? Ne jetez pas les deux premières. Cessez de collectionner la troisième.

---

# Chapitre 3 — Le CISO qui veut trop valoriser ses investissements

## Mise en situation

*Le scénario suivant est entièrement fictif. Les personnages, l’entreprise et les résultats décrits sont inventés pour éclairer un arbitrage, pas pour documenter un incident réel.*

Marc, directeur de la sécurité d’un groupe de distribution, reconnaît sa propre présentation avant même que la directrice financière ouvre le dossier. Il l’avait défendue dix-huit mois plus tôt : plateforme unifiée, visibilité accrue, automatisation des réponses. Les mots étaient justes. Les intentions aussi. Aujourd’hui, le renouvellement arrive avec une hausse de tarif et plusieurs modules supplémentaires. Le commercial appelle cela une optimisation du périmètre. Sophie, la directrice financière, appelle cela une dépense supplémentaire. Les deux expressions tiennent sur la même facture.

— Avant de parler du prix, dit-elle, qu’est-ce que nous perdrions en ne renouvelant pas tout ?

Marc affiche le nombre d’équipements sous licence, le volume de journaux collectés et les alertes traitées. Les courbes montent. Il a même retiré les animations, preuve incontestable de sobriété budgétaire.

— Nous avons beaucoup mieux couvert le groupe.

— Couvert comment ? demande Sophie. Contractuellement, techniquement, ou réellement quand quelqu’un essaie de nous attaquer ?

Il aurait préféré une question sur la remise.

Lina, responsable des opérations de sécurité, intervient avec précaution. Les postes administratifs sont bien raccordés. Plusieurs serveurs logistiques le sont moins régulièrement. Les équipements acquis avec une filiale apparaissent dans l’inventaire, mais leur télémétrie ne remonte pas encore. Une règle de détection importante a été désactivée parce qu’elle saturait la file des analystes. Rien de scandaleux : des chantiers connus, des dépendances et des semaines trop courtes. Simplement, le graphique de Marc ne montre aucune de ces nuances.

— Les licences sont disponibles, précise-t-il. C’est déjà un investissement fait.

Lina ne relève pas immédiatement. Elle sait ce que cette phrase protège. Marc a obtenu le budget, choisi le fournisseur et porté la migration devant le comité exécutif. Remettre le périmètre en question ressemble, pour lui, à remettre sa décision en question. Et personne n’aime découvrir que son meilleur argument de l’année précédente est devenu une contrainte de l’année suivante.

Sophie propose de revenir le vendredi avec trois scénarios : maintenir, réduire, remplacer. Elle ne demande pas de supprimer la sécurité. Elle veut savoir pourquoi la prochaine dépense est préférable aux autres usages possibles du budget. Marc entend néanmoins : prouvez que vous n’avez pas acheté trop cher. Il sort de la réunion avec l’envie parfaitement humaine de préparer sa défense plutôt que l’arbitrage demandé.

Dans l’après-midi, le fournisseur propose une séance de valorisation. Un consultant présente les fonctionnalités encore inutilisées et suggère un programme d’activation. Marc prend des notes. Lina pose une question sur le temps nécessaire pour maintenir les nouvelles règles et traiter leurs alertes. La réponse évoque un accompagnement initial. Elle insiste sur l’exploitation après le départ du consultant. Un silence poli s’installe, ce moment particulier où tout le monde regarde la même case vide sans vouloir la nommer.

— Activer davantage ne veut pas forcément dire protéger davantage, dit-elle ensuite à Marc.

— Nous ne pouvons pas expliquer que nous avons acheté des fonctions dont nous ne nous servons pas.

— Nous pouvons expliquer lesquelles sont utiles. Ce serait déjà mieux que de les mettre toutes en production pour justifier la commande.

Ils organisent une vérification sur un périmètre autorisé, sans toucher aux opérations réelles. L’exercice reproduit l’usage anormal d’un compte de test et une tentative d’accès à un partage sensible. Une première alerte arrive rapidement. Une seconde ne se déclenche pas : le journal attendu n’est pas collecté sur le serveur choisi. Une troisième arrive dans une file que personne ne consulte pendant l’exercice. La plateforme fonctionne sur une partie du parcours. La chaîne de réponse, elle, comporte des trous.

Marc regarde les résultats avec irritation, puis avec soulagement. Ils disposent enfin d’autre chose qu’une impression. Le produit n’est ni miraculeux ni inutile. Certains scénarios sont correctement traités ; d’autres n’ont jamais été validés. Il demande à Lina de séparer les défauts du produit, les défauts de configuration et les capacités que l’équipe ne peut pas exploiter avec ses ressources actuelles. Cette distinction évite de transformer une revue budgétaire en procès du fournisseur ou des analystes.

Le lendemain, les achats arrivent avec une solution séduisante : regrouper deux contrats dans une offre plus large. L’économie annoncée semble régler le problème. Le responsable infrastructure refroidit légèrement l’enthousiasme. Les deux services partageraient désormais le même système d’administration et une partie du mécanisme d’authentification. Il demande comment accéder aux consoles si ce mécanisme tombe. Personne n’a encore testé ce chemin. La consolidation reste une option ; elle vient simplement de perdre son statut de bonne idée automatique.

Marc reprend sa présentation. Il supprime une estimation de pertes évitées qui reposait sur trop d’hypothèses pour supporter ses décimales. À la place, il décrit les scénarios jugés prioritaires, les preuves disponibles et les limites. Il conserve un service dont la rentabilité financière n’est pas démontrable, parce qu’il fournit une capacité de confinement nécessaire sur les systèmes critiques. Il propose de réduire un module peu exploité et de financer la collecte manquante ainsi qu’un exercice de reprise.

Le vendredi, Sophie s’arrête sur la première page.

— Donc vous nous proposez de ne pas rentabiliser tout ce que nous avons acheté ?

— Je vous propose de ne pas dépenser davantage uniquement pour donner raison à une dépense passée.

Elle lui demande ce qui restera exposé. Il répond sans diapositive supplémentaire : certains serveurs, pendant le raccordement ; un délai de réponse nocturne ; une dépendance fournisseur encore insuffisamment testée. Chaque limite a un responsable et une échéance. Le comité accepte le scénario réduit sous réserve des tests. Marc n’a pas sauvé toutes ses licences. Il a retrouvé une décision qu’il peut défendre sans demander à son équipe de jouer dans la publicité du produit.

## Ce qui se passe vraiment

Le piège n’est pas d’avoir acheté un outil imparfait. C’est de prendre le coût déjà engagé pour une raison de continuer. Ce coût irrécupérable appartient au bilan du passé. La décision actuelle doit comparer les dépenses futures, les résultats attendus, les risques du changement et ceux du maintien. Une pénalité de sortie future compte ; l’envie de ne pas perdre la face ne constitue pas un bénéfice de sécurité.

Il faut surtout distinguer cinq états : acheté, déployé, alimenté, exploité, éprouvé. Une licence prouve un droit d’usage. Un agent installé prouve une présence. Une alerte dans la console prouve une détection dans certaines conditions. Aucun de ces éléments ne démontre, seul, que la bonne personne saura contenir le scénario redouté à temps.

Cela ne signifie pas que les plateformes seraient une imposture. Dans sa publication du 27 mai 2025, la CISA présente avec ses partenaires des guides consacrés au déploiement des plateformes de gestion des événements de sécurité et d’orchestration de la réponse ; elle distingue notamment la conduite exécutive, la mise en œuvre opérationnelle et la priorité des journaux à collecter.[10] La contradiction est féconde : ces technologies peuvent améliorer détection et réponse, mais leur intérêt suppose précisément le travail que la seule acquisition ne réalise pas. Cette publication annonce des recommandations ; elle ne mesure pas le rendement de votre installation.

Même prudence avec le retour sur investissement. L’absence d’un incident ne permet pas de savoir combien de pertes un contrôle a évité. Cela n’autorise ni un chiffre décoratif ni l’abandon d’un risque réel. On peut documenter un scénario, une exposition, un impact plausible et une capacité testée sans prétendre calculer un rendement exact. Une obligation applicable ou une capacité de survie peut justifier une dépense dont le rendement financier reste incertain.

### Un incident public, distinct de la fiction

Le 18 novembre 2025, Cloudflare a subi une panne majeure. Selon son compte rendu, elle ne provenait pas d’une attaque : une modification des permissions d’une base a conduit à produire des entrées dupliquées dans un fichier utilisé par son système de gestion des robots, puis à propager un fichier dépassant une limite du logiciel.[9] Le fournisseur décrit des effets sur plusieurs services, dont des défaillances d’authentification et des erreurs de distribution du trafic.[9]

Ce retour public ne démontre ni qu’il faudrait quitter Cloudflare ni que toute consolidation serait dangereuse. Il montre une dépendance technique et sa propagation, pas le rendement des contrats clients. La leçon que j’en tire est plus précise : évaluer le fonctionnement dégradé d’une architecture aussi sérieusement que ses fonctionnalités nominales. Un fournisseur unique peut simplifier l’exploitation ; plusieurs fournisseurs peuvent aussi partager une dépendance cachée. Compter les logos ne suffit dans aucun des deux sens.

## Les erreurs classiques

- **Faire du taux d’utilisation une cible de sécurité.** Activer une fonction uniquement parce qu’elle est payée ajoute potentiellement du bruit et du travail sans traiter un scénario prioritaire.
- **Confondre silence et efficacité.** Peu d’alertes peut signifier peu d’attaques, mais aussi une collecte absente. Beaucoup d’alertes peut signifier une bonne visibilité ou une mauvaise sélection.
- **Exiger un rendement exact pour tout.** Cette exigence favorise les gains faciles à raconter et pénalise les capacités nécessaires, mais difficiles à valoriser : restauration, investigation, confinement.
- **Consolider sur le seul prix facial.** La migration, l’exploitation, les dépendances communes et les modalités de sortie changent l’arbitrage. Refuser toute consolidation par principe serait tout aussi paresseux.
- **Défendre une personne à travers un produit.** Si revoir un contrat devient un aveu personnel d’incompétence, l’organisation apprend à préserver les mauvaises décisions.

## Faire autrement

Commencez par trois scénarios métier, pas par la liste des modules. Le responsable métier précise ce qui ne doit pas être interrompu ou divulgué. L’équipe sécurité décrit le chemin d’attaque pertinent. L’exploitation indique ce qu’elle peut effectivement maintenir. Pour chaque scénario, conservez une preuve datée : simulation autorisée, journal attendu, alerte reçue, décision prise, action exécutée et résultat constaté. Notez aussi les périmètres non testés.

Construisez ensuite quatre options : maintenir, corriger l’existant, réduire, remplacer. Pour chacune, estimez les coûts futurs complets, y compris les personnes, la formation, les interruptions et la sortie. Présentez des fourchettes lorsque les données manquent. Une migration n’est pas gratuite parce qu’elle figure dans la colonne « économies ».

Attribuez les décisions correctement. Le CISO recommande et explicite l’incertitude. Le propriétaire du service accepte le risque résiduel selon la gouvernance prévue. Les achats vérifient les engagements contractuels. L’exploitation valide la faisabilité du fonctionnement dégradé. La finance challenge les hypothèses économiques sans inventer la probabilité d’une catastrophe à la place des équipes.

Avant un renouvellement, demandez un jalon de preuve plutôt qu’un programme vague d’adoption : rétablir une collecte précise, démontrer une réponse sur le périmètre critique, tester l’accès d’urgence indépendant. Si la preuve échoue, réviser le périmètre ou financer la correction. Si elle réussit, conserver l’outil peut être la décision la plus sobre. Le but n’est pas de changer pour afficher son courage ; c’est de choisir à nouveau avec les informations disponibles.

## La fiche à emporter

**Une page par investissement à renouveler :**

- **Décision et date :** que faut-il réellement engager maintenant ?
- **Scénario :** quel dommage métier cette capacité doit-elle réduire ?
- **Couverture :** quels actifs, identités et horaires sont éprouvés, absents ou inconnus ?
- **Preuve :** dernier test, résultat, limite et personne capable de le reproduire.
- **Coût futur :** contrat, exploitation, correction, transition et sortie.
- **Alternative :** conserver, améliorer, réduire ou remplacer ; pourquoi écarter les autres ?
- **Dépendance :** que perd-on ensemble, et comment agit-on pendant la panne ?
- **Responsabilité :** qui accepte le risque restant et quand le réexamine-t-on ?

**Question de contrôle :** si ce produit n’était pas déjà chez nous, choisirions-nous aujourd’hui cette dépense supplémentaire pour ce résultat prouvé ? Un « non » n’impose pas une rupture immédiate. Il impose une explication meilleure que « nous avons déjà payé ».

---

# Chapitre 4 — Le CISO perdu dans la veille techno

## Mise en situation

*Cette mise en situation est entièrement fictive. Elle ne rapporte ni une expérimentation réelle ni des résultats attribuables à un fournisseur.*

À sept heures quarante, Nadia a enregistré quatre articles : la fin du centre opérationnel traditionnel, les attaques autonomes, une solution providentielle et une analyse technique. La dernière attendra. Cette directrice de la sécurité d’un groupe de services commence sa journée en retard sur le futur.

Son équipe alimente trois canaux de veille. Les architectes disposent du leur. La direction de l’innovation diffuse une lettre hebdomadaire. Les fournisseurs proposent des réunions de synthèse, autrement dit des informations qui connaissent déjà le bon de commande auquel elles aimeraient aboutir. Tout cela contient des choses utiles. Le problème n’est pas leur existence. C’est que personne ne sait quelle décision ce flux doit permettre de prendre, ni quelle information autoriserait enfin à cesser de chercher.

À neuf heures, le directeur général lui transfère une démonstration d’agent capable d’enquêter sur une alerte, d’enrichir le dossier et de désactiver un compte. Son message tient en une phrase : « Où en sommes-nous ? » Nadia envisage une réponse sur la maturité du marché, puis l’efface. Elle ne sait pas si la question signifie acheter, tester, rassurer le conseil ou simplement comprendre la vidéo. Elle appelle le directeur général.

— Nous voulons réduire le temps perdu par les analystes, précise-t-il. Pas annoncer que nous avons une intelligence artificielle.

— Dans ce cas, je vous proposerai une expérience sur une tâche précise, avec une comparaison et une limite de dépense.

La conversation dure moins longtemps que la démonstration.

Nadia réunit Hugo, responsable du centre opérationnel, et Salomé, ingénieure chargée des automatisations. Hugo décrit le vrai irritant : retrouver le contexte d’un compte entre plusieurs consoles avant de décider si une alerte mérite une investigation. Salomé propose d’abord un connecteur classique. Nadia demande ce qu’un agent apporterait de plus. Il pourrait rapprocher des éléments dispersés et préparer une synthèse adaptée à des dossiers incomplets. Peut-être. Le mot reste sur le tableau ; personne ne cherche à le remplacer immédiatement par « transformation ».

Ils définissent un premier périmètre : consulter une copie filtrée de dossiers historiques, restituer les éléments pertinents et citer leur provenance. Aucun accès aux messageries personnelles. Aucun droit de désactiver un compte. Aucune capacité d’envoyer une information vers un destinataire librement choisi. Le fournisseur accepte ce cadre, mais souligne que la démonstration serait plus spectaculaire avec des actions automatiques. Hugo répond qu’une synthèse exacte ferait déjà un très bon spectacle pour son équipe.

La première séance se passe bien. L’agent retrouve des connexions inhabituelles et rapproche des événements que l’analyste aurait dû consulter séparément. Nadia se surprend à sourire. Il y a une utilité possible, pas seulement une nouvelle console à expliquer. Puis Salomé présente un dossier moins propre : deux personnes portent le même nom, un journal arrive en retard et une note contient une conclusion devenue fausse après une vérification ultérieure. La synthèse est fluide. Elle assemble pourtant les mauvaises pièces.

— Nous avons testé sa capacité à raconter quelque chose de cohérent, dit Salomé. Il faut maintenant tester sa capacité à ne pas conclure quand le dossier ne permet pas de conclure.

Hugo ajoute un cas banal que la démonstration n’avait pas montré : l’alerte est légitime, l’utilisateur travaille exceptionnellement depuis un autre site, et aucune action ne doit être prise. Un outil qui sait toujours trouver un coupable ne leur fera pas forcément gagner du temps.

Au second passage, ils introduisent dans un document de test une instruction hostile demandant à l’agent d’ignorer sa mission. Ce document ne contient aucune donnée réelle. Nadia veut savoir non seulement ce que l’agent répond, mais quelles opérations il tente. La barrière technique bloque une action non autorisée. C’est une bonne nouvelle pour le contrôle d’accès, pas une preuve que le modèle est devenu insensible à la manipulation. Salomé inscrit les deux constats séparément. Cette précision évite de féliciter le mauvais mécanisme.

Le bilan du vendredi n’est ni un triomphe ni un enterrement. Les dossiers simples sont préparés plus vite. Les dossiers ambigus exigent encore une relecture attentive, parfois une reconstruction complète. L’équipe mesure le temps total jusqu’à une décision correcte, pas seulement la vitesse de génération du texte. Elle compare aussi avec le connecteur proposé initialement. Sur une partie des tâches, l’automatisation classique reste plus prévisible ; sur une autre, l’assistant apporte une aide que le connecteur ne fournit pas.

Nadia décide de poursuivre en assistance limitée. Elle refuse l’extension immédiate aux actions de confinement, mais fixe les conditions d’un réexamen : des résultats reproductibles, des permissions séparées, une validation humaine montrant exactement la cible et l’effet attendu, et un retour arrière testé. Hugo accepte d’être responsable du pilote à condition de disposer du temps nécessaire. Sans cela, le projet aurait simplement déplacé du travail vers une équipe déjà occupée, sous le nom plus séduisant d’innovation.

Le lundi suivant, Nadia réorganise la veille. Un canal traite les menaces nécessitant une action rapide. Un autre alimente quelques décisions identifiées : améliorer la qualification des alertes, réduire une dépendance, préparer un renouvellement. Le reste va dans une réserve consultée à date fixe. Chaque sujet actif possède un responsable, une question et une condition de clôture. Elle conserve des lectures exploratoires ; elle cesse seulement de les présenter comme des projets en attente.

À sept heures quarante, le lendemain, une nouvelle annonce promet de réinventer toute la sécurité. Nadia l’enregistre avec une phrase : « À revoir si cette capacité répond à notre test sur les dossiers ambigus. » Elle n’a pas cessé de suivre l’innovation. Elle lui a donné une adresse où se présenter et une raison de sonner.

## Ce qui se passe vraiment

Une veille peut être excellente comme bibliothèque et médiocre comme instrument de décision. La confusion vient de la mesure implicite : combien d’informations avons-nous captées ? La mesure utile est différente : quelle décision avons-nous prise, modifiée ou différée grâce à une information suffisamment fiable ? Lire davantage ne compense pas l’absence d’une question.

Séparez les temporalités : une vulnérabilité exploitée sur un composant exposé ne doit pas attendre la revue mensuelle des innovations. Une démonstration commerciale ne mérite pas le traitement d’une crise.

L’agent d’IA rend cette discipline particulièrement importante. Il ne produit pas seulement un texte : il peut consulter des ressources et déclencher des opérations. La frontière de sécurité passe donc par les données accessibles, les outils disponibles, leurs paramètres et les autorisations effectives. Ma recommandation est de traiter toute nouvelle capacité d’action comme une modification du périmètre de confiance, pas comme une simple amélioration de l’interface.

Les retours techniques donnent des arguments pour essayer, mais aussi pour résister aux raccourcis. Dans son article du 11 septembre 2025 sur les outils destinés aux agents, Anthropic recommande des tâches d’évaluation réalistes, des résultats vérifiables et des outils clairement délimités ; l’équipe rapporte également l’usage de jeux de test conservés à part pour limiter le surajustement.[11] Cela soutient une démarche d’expérimentation ciblée, pas la promesse d’un agent universel immédiatement fiable.

Le retour publié le 9 janvier 2026 précise qu’une évaluation doit distinguer le discours de l’agent de l’état réellement obtenu dans l’environnement. Il recommande plusieurs essais, des cas où un comportement doit se produire et d’autres où il doit être évité, ainsi que l’examen des traces.[13] La distinction est essentielle : « le compte est désactivé » n’est pas une preuve de désactivation ; une action exécutée n’est pas forcément une action autorisée.

Ces deux publications viennent du même concepteur de modèles. Elles constituent des retours primaires utiles, non une validation indépendante de performance dans votre entreprise. Leur intérêt est méthodologique. Elles invitent à construire les preuves qui manquent au discours commercial, plutôt qu’à choisir entre enthousiasme inconditionnel et rejet de l’IA.

## Les erreurs classiques

- **Confondre visibilité médiatique et pertinence.** Une technologie omniprésente peut ne résoudre aucun de vos problèmes prioritaires. Une amélioration discrète de collecte peut, elle, changer une investigation.
- **Évaluer uniquement les réussites montrables.** Les cas ambigus, les refus justifiés, les permissions manquantes et les données obsolètes doivent faire partie de l’essai.
- **Attribuer tous les gains au modèle.** Une meilleure intégration ou une procédure clarifiée peut expliquer le progrès. Comparer avec une solution simple évite de payer une sophistication inutile.
- **Appeler supervision un bouton de confirmation.** Une personne qui ne voit ni la cible, ni les conséquences, ni les éléments justificatifs ne contrôle pas réellement l’action.
- **Installer un pilote sans fin.** Sans échéance, budget, responsable et condition de sortie, l’expérience devient un service de production qui refuse de dire son nom.
- **Dire non à la catégorie entière.** Refuser toute IA dispense de tests, mais aussi de bénéfices possibles. Le refus utile porte sur un usage et des conditions précises.

## Faire autrement

Organisez la veille autour d’un petit portefeuille de décisions. Pour chaque sujet : une question, un propriétaire, une date de décision et la preuve susceptible de changer l’avis initial. « Suivre les agents » est trop large. « Déterminer si une assistance réduit le temps de qualification sans augmenter les erreurs critiques » peut devenir un protocole. Un sujet sans conséquence identifiable reste une lecture exploratoire, pas une ligne automatique de la feuille de route.

Classez les sources : annonce pour la promesse, documentation pour les contraintes, retour public pour les échecs, essai local pour l’adéquation. Un résultat publié ne garantit pas sa transférabilité.

Pour un agent, confiez au responsable métier la définition du résultat acceptable, à l’équipe technique les barrières d’accès et au CISO les critères de risque. Commencez en lecture limitée avec des données autorisées. Séparez consultation et action ; utilisez des identités dédiées, des permissions minimales et des destinations contrôlées. Une consigne donnée au modèle ne remplace pas une interdiction appliquée par le système.

Construisez les tests avant de négocier le déploiement. Conservez des dossiers représentatifs non utilisés pour régler le système. Répétez les essais et inspectez les opérations réellement effectuées. Incluez les documents hostiles, les indisponibilités d’outils, les erreurs d’identité, les refus nécessaires et les actions partielles. Mesurez la qualité finale, les erreurs graves, le temps humain de vérification et le coût complet. Définissez les seuils avec le métier ; ne copiez pas ceux d’une démonstration.

Prévoyez enfin trois issues : déployer un périmètre limité, prolonger pour répondre à une incertitude précise, arrêter. Refusez conditionnellement la production si les droits ne peuvent pas être réduits, les actions auditées ou les données récupérées. Fixez une date de réexamen si une amélioration peut lever le blocage. Testez aussi la sortie : révocation des accès, export des éléments nécessaires, suppression prévue des données et reprise manuelle. L’innovation utile doit pouvoir quitter la pièce sans emporter les clés.

## La fiche à emporter

**La fiche de veille qui débouche sur une décision :**

1. **Question :** quel problème concret voulons-nous résoudre, pour qui ?
2. **Échéance :** quand faut-il décider, et que coûte l’attente ?
3. **Référence :** comment la tâche est-elle accomplie aujourd’hui ?
4. **Promesse et preuve :** qu’affirme le fournisseur, qu’avons-nous réellement vérifié ?
5. **Expérience :** données autorisées, cas difficiles, essais répétés, résultat observable.
6. **Pouvoirs :** que peut lire, modifier, transmettre ou supprimer le système ?
7. **Seuils :** gains attendus, erreurs inacceptables, charge maximale de supervision.
8. **Issue :** adopter, différer sous conditions ou arrêter ; responsable et prochaine date.
9. **Sortie :** accès révoqués, données traitées, service repris, preuve conservée.

**Règle de réunion :** terminer une revue de veille par une décision explicite, y compris « aucune action, réexamen si telle condition change ». Une pile d’articles sauvegardés n’est pas une feuille de route. Une hypothèse testée, même rejetée, peut en devenir une.

---

# 5. Le CISO qui n’a pas d’argent

## Mise en situation

*Fiction pédagogique : cette entreprise, ses personnages et les échanges qui suivent sont inventés. Les montants et délais servent uniquement à rendre les arbitrages concrets.*

Nadia arrive avec un budget intitulé « Socle indispensable ». Elle a déjà retiré deux projets, reporté une certification et renoncé au remplacement de son analyste parti au printemps. Dans la salle, Marc, directeur financier, ouvre un tableau différent : celui des commandes perdues. Il ne lui demande pas de protéger moins bien l’entreprise. Il lui demande de dépenser moins. La distinction est sincère ; elle ne crée pourtant aucune heure supplémentaire dans la semaine.

« Il manque combien pour rester au niveau actuel ? » demande Marc. Nadia hésite. Le niveau actuel repose sur des soirées non comptées, une administratrice qui connaît seule le système de sauvegarde et un prestataire appelé quand quelqu’un décroche encore. Elle pourrait annoncer la différence entre deux colonnes. Elle préfère dire : « Avant de parler du niveau actuel, il faut expliquer comment il tient. » Le responsable informatique, Julien, pose enfin son téléphone.

Nadia affiche la liste des tâches récurrentes. Les demandes d’accès, les correctifs, les questionnaires clients, les alertes, les exercices, les renouvellements. Aucun grand programme de transformation. « Qui fait tout cela ? » demande Marc. « Nous, plus les équipes informatiques. Mais certaines choses sont seulement réputées faites. » Elle montre le contrôle mensuel des restaurations. La dernière preuve complète remonte à plusieurs mois. Les sauvegardes tournent ; la capacité à reprendre le service reste partiellement inconnue.

Julien précise qu’il ne manque pas de bonne volonté. Le test mobilise son équipe, une personne du métier et un environnement disponible. Chaque tentative a perdu contre une urgence commerciale. « Donc il nous faut un meilleur outil », conclut Marc, sans provocation. « Peut-être. Mais celui que nous avons sait déjà restaurer. Il nous manque surtout une décision sur ce que nous interrompons pour vérifier. » Le budget commence à ressembler à un problème d’agenda collectif.

La responsable commerciale, Sarah, propose d’externaliser. Un fournisseur lui a présenté une surveillance permanente pour un abonnement qu’elle juge raisonnable. Nadia ne balaie pas l’idée. Elle demande qui autorisera le prestataire à isoler un poste, qui répondra pendant la nuit et quelles applications seront effectivement surveillées. Sarah cherche ces éléments dans la brochure. Elle trouve une photographie de salle opérationnelle. Les écrans sont nombreux, les personnes attentives ; aucune ne connaît leur application de prise de commandes.

« On peut acheter de la surveillance sans acheter la décision qui suit », explique Nadia. « Cela peut nous aider, mais il faut garder quelqu’un capable de qualifier l’impact et d’agir. » Marc demande si le service serait donc inutile. « Non. Je demande seulement que son prix comprenne notre part du travail. Sinon nous économisons sur le devis et nous payons ailleurs, généralement avec les mêmes personnes. » Julien acquiesce, sans enthousiasme particulier : il s’est reconnu dans la phrase.

Un administrateur a aussi proposé une solution libre pour remplacer leur outil de collecte. Nadia l’invite à présenter son essai. Le prototype fonctionne, les recherches sont rapides, les tableaux lisibles. Il annonce fièrement qu’il n’y a pas de licence à acheter. « Très bien », répond Nadia. « Maintenant, montre-nous comment tu le mets à jour quand tu es absent. » Il reconnaît que la documentation reste à écrire. Personne ne rit. Le problème n’est pas son travail ; c’est l’idée qu’il puisse le soutenir seul indéfiniment.

Ils inscrivent au tableau les tâches nécessaires : hébergement, stockage, mises à jour, adaptation des connecteurs, gestion des accès, sauvegarde, transmission. Certaines existent aussi avec le produit commercial. D’autres changent de responsable. Marc voit enfin une comparaison exploitable. « Nous pouvons choisir le libre, mais pas voter pour une communauté imaginaire qui ferait notre exploitation. » Nadia sourit. C’est probablement la première phrase de la réunion qui pourrait survivre intacte au compte rendu.

Elle revient aux risques. Une compromission des comptes administrateurs pourrait arrêter plusieurs activités. Une panne du portail commercial gênerait les ventes, mais une procédure manuelle existe. Un questionnaire client incomplet menace un contrat précis. Tout mérite une attention ; tout ne mérite pas la même priorité cette semaine. Sarah demande que le contrat soit traité. Nadia accepte, à condition de nommer l’activité déplacée. « Nous ne reportons pas la gravité. Nous reportons du travail, avec ses conséquences. »

La discussion devient moins agréable, donc plus utile. Ils décident de supprimer un rapport mensuel que personne ne lit et de regrouper les preuves demandées par les clients. Le projet de nouvelle plateforme est suspendu. L’exercice de restauration reçoit une plage réservée, validée par le métier. Les comptes privilégiés passent avant l’extension de la collecte de journaux. Une petite prestation de surveillance sera étudiée, mais sur un périmètre explicite, avec un test d’escalade avant engagement durable.

Marc demande ce qui restera découvert. Nadia nomme deux services anciens, mal inventoriés, dont la remise à niveau attendra. Elle décrit les conséquences possibles, les restrictions temporaires et ce qui déclenchera une révision. « Tu nous fais signer une décharge ? » demande Sarah. « Non. Je vous demande de décider avec moi, puis de tenir la décision. Si nous acceptons un risque aujourd’hui, nous devons aussi savoir quand cette acceptation cesse d’être raisonnable. »

Avant de partir, Julien demande si son équipe devra récupérer le retard le week-end. Marc répond non, puis regarde Nadia pour confirmer. Elle ajoute cette limite au document : la capacité retenue exclut les heures supplémentaires permanentes. Le budget n’a pas miraculeusement augmenté. Il manque encore des moyens et quelques décisions feront mal. Mais ils ont cessé de présenter l’épuisement comme une ressource gratuite. Pour la première fois, le plan décrit ce que l’entreprise peut vraiment faire, et ce qu’elle choisit de ne pas faire.

## Ce qui se passe vraiment

Le manque d’argent n’est pas une faute professionnelle. Il peut traduire une contrainte économique réelle, une mauvaise allocation, ou les deux. Le rôle du CISO n’est pas de rendre les contraintes indolores : il consiste à exposer les conséquences et à construire un plan exécutable. Une couverture incomplète mais connue vaut mieux qu’une couverture annoncée dont personne ne peut assurer l’exploitation.

L’ENISA rappelle en septembre 2026 la persistance des rançongiciels, de l’ingénierie sociale et de l’exploitation de vulnérabilités, tout en soulignant les dépendances numériques. Son panorama porte sur des événements de 2025, pas sur un échantillon prédictif de votre entreprise.[1] Il ne dicte donc pas votre budget. Il fournit des scénarios à confronter à vos accès exposés, à vos services indispensables et aux conséquences d’une interruption. L’actualité de l’intelligence artificielle ne rend pas ces chemins d’attaque obsolètes.

Le coût pertinent est celui d’une capacité tenue dans la durée : acquisition, intégration, exploitation, formation, remplacement des personnes, réaction et sortie. Cette grille est une proposition de pilotage, pas une formule financière universelle. La même dépense peut être raisonnable pour une équipe disposant des compétences nécessaires et ruineuse pour une autre qui doit les acheter en urgence.

Sur le logiciel libre, un texte de fondation de la CISA, publié en juillet 2024, rappelle que l’utilisateur doit continuer à évaluer les projets dont il dépend ; l’usage direct ne crée pas à lui seul une relation acheteur-fournisseur.[17] Le code britannique de sécurité des logiciels, actualisé en janvier 2026, distingue également les responsabilités des clients et celles des éditeurs commerciaux ; il insiste sur la maintenance et la communication du niveau de support.[18] Le libre n’est donc ni une économie fictive ni une gratuité opérationnelle. C’est un choix de répartition du travail et de dépendance.

Externaliser déplace certaines tâches, pas toutes les conséquences. Le code britannique de gouvernance de 2025 demande aux dirigeants de s’assurer de l’allocation des ressources et de l’évaluation proportionnée des fournisseurs.[16] Cette recommandation britannique n’est pas présentée ici comme une obligation juridique française. Elle soutient une règle de gestion simple : l’entreprise doit conserver la capacité de comprendre le service acheté, d’exercer ses droits et de décider quand il échoue.

## Les erreurs classiques

**Réduire les lignes plutôt que les engagements.** Une baisse uniforme préserve parfois les activités les moins utiles et fragilise les fonctions vitales. Il faut distinguer ce qui peut cesser, ralentir ou changer de mode de réalisation.

**Compter les produits, oublier les personnes.** Une licence inutilisée ne constitue pas une capacité. Un poste non remplacé ne disparaît pas du travail restant. Le surengagement transforme une économie visible en dette d’exploitation invisible.

**Promettre une surveillance permanente sans réponse permanente.** Précisez la différence entre réception, analyse, notification et action. Un appel nocturne sans destinataire habilité n’est pas une chaîne de réponse.

**Transformer le risque accepté en culpabilité individuelle.** Faire signer un responsable ne crée ni compétence ni budget. Une acceptation utile comporte un périmètre, des conséquences, une échéance et des conditions de réouverture ; elle n’est pas un moyen de préparer le prochain coupable.

## Faire autrement

Commencez par trois scénarios de pertes compréhensibles par les métiers. Pour chacun, nommez le service, la dépendance, les mesures existantes et la preuve disponible. Distinguez « absent », « présent mais non testé » et « démontré sur ce périmètre ». Cette distinction évite de financer une nouveauté pendant qu’un contrôle acheté reste inutilisable.

Établissez ensuite une capacité réaliste avec les responsables informatiques : temps récurrent, indisponibilités, astreinte soutenable et marge pour les incidents. Présentez deux plans, pas une demande unique : un plan finançable avec risques résiduels, et un palier supplémentaire indiquant exactement ce qu’il améliore. N’inventez pas un retour sur investissement précis lorsque la fréquence des pertes reste inconnue.

Chaque ajout doit avoir sa contrepartie : financement nouveau, activité supprimée ou délai déplacé. Tenez un registre des arrêts avec bénéficiaire consulté, preuve à préserver et signal de reprise. Ne supprimez pas une obligation légale faute d’usage apparent ; faites qualifier le besoin avant de l’éliminer.

Pour un prestataire ou un projet libre, réalisez un essai d’exploitation autant qu’un essai technique. Faites traiter une alerte, appliquer une mise à jour et transmettre le service à une autre personne. Mesurez le temps interne, les accès nécessaires et les limites rencontrées. Une promesse d’automatisation mérite un budget d’essai borné, pas un crédit illimité sur les économies futures.

La feuille de route peut alors rester courte : d’abord vérifier les accès critiques et la reprise ; ensuite supprimer les doublons et stabiliser l’exploitation ; enfin expérimenter une amélioration ciblée. Révisez cet ordre si les preuves locales le justifient. Le bon budget n’est pas le plus austère : c’est celui dont les engagements restent honnêtes.

## La fiche à emporter

Pour chaque dépense ou activité, compléter une fiche commune :

- **Conséquence visée :** quel scénario métier veut-on réduire ?
- **Preuve :** que savons-nous réellement faire aujourd’hui ?
- **Coût complet :** argent, temps interne, exploitation, formation et sortie.
- **Capacité :** qui assure le service, y compris pendant les absences ?
- **Arbitrage :** que cessons-nous ou reportons-nous pour le financer ?
- **Reste à risque :** quels périmètres demeurent insuffisamment couverts ?
- **Autorité :** qui accepte cette situation, dans quelles limites ?
- **Réexamen :** quelle date ou quel événement impose une nouvelle décision ?

Refusez une ligne sans responsable d’exploitation. Refusez aussi un plan qui ne tient qu’en supposant les personnes disponibles en permanence. La contrainte mérite de la précision, pas une leçon de courage.

---

# 6. Le CISO qui se protège avec le Gartner en haut à droite

## Mise en situation

*Fiction pédagogique : les personnes, les fournisseurs et l’entreprise de cette scène sont inventés. Aucun classement réel ni aucun incident particulier n’est représenté.*

Sur la première page du dossier d’achat, Thomas a placé un graphique. Dans le coin supérieur droit, un point entouré en rouge annonce le fournisseur recommandé. Le directeur général reconnaît immédiatement le visuel. La directrice des achats, Élise, demande si l’évaluation technique est terminée. « Nous avons choisi une référence du marché », répond Thomas. Ce n’est pas exactement la question. Mais c’est une réponse confortable, et la réunion a déjà pris du retard.

L’entreprise veut remplacer son dispositif de détection. L’équipe actuelle peine à exploiter plusieurs consoles et les métiers réclament des délais de réponse plus courts. Le fournisseur pressenti propose une plateforme intégrée, avec une assistance fondée sur l’intelligence artificielle et une feuille de route particulièrement bien illustrée. Thomas ne cherche pas seulement un produit. Il cherche un choix défendable devant un comité qui lui demandera, au prochain incident, pourquoi il n’avait pas acheté mieux.

« Quelle difficulté précise cette plateforme résout-elle chez nous ? » demande Aïcha, responsable des opérations. Thomas cite la consolidation, la visibilité et l’automatisation. Elle connaît ces mots ; elle voudrait leur adresse. « Sur l’application de commandes, nous ne recevons toujours pas les événements d’authentification complets. Est-ce que ce produit sait les récupérer ? » Le commercial, invité pour la présentation, explique que le connecteur figure dans les développements prévus. Aïcha inscrit « non disponible » dans son carnet.

Le directeur général s’inquiète de cette formulation. « Ce n’est pas un peu sévère ? Ils sont quand même très bien placés. » Aïcha répond calmement : « Je ne juge pas l’entreprise. Je distingue ce qui existe de ce qui pourrait arriver. » Thomas ressent la remarque comme une critique de son travail. Il a rencontré des analystes, lu des dossiers et comparé des offres. Réduire sa recommandation à une confiance aveugle serait injuste. Il le dit, puis s’arrête avant de hausser le ton.

Élise propose de séparer les questions. La solidité du fournisseur en est une. L’adéquation au système local en est une autre. Le contrat, les coûts et les possibilités de sortie en forment encore d’autres. « Nous pouvons avoir raison sur la première et tort sur les suivantes. » Le commercial approuve. Il propose un essai, avec ses ingénieurs. Thomas se détend : une démonstration réussie pourrait enfin remettre tout le monde d’accord.

Aïcha refuse pourtant de commencer par la démonstration. Elle veut écrire les critères avant de voir le produit fonctionner. Elle choisit un scénario d’accès compromis, un scénario de modification administrative et une panne de transmission des événements. Pour chacun, l’équipe définira ce qu’elle attend, ce qu’elle pourra observer et le temps nécessaire pour comprendre le résultat. « Si nous écrivons le barème après, nous finirons par mesurer ce que l’outil sait montrer. »

Le commercial accepte les scénarios, mais demande des données représentatives et un interlocuteur disponible. Élise fait préciser cette disponibilité. Le pilote consommera du temps de sécurité, d’infrastructure et d’application. Thomas avait prévu une semaine de tests ; Aïcha montre les interventions nécessaires sur plusieurs équipes. Ils réduisent le périmètre plutôt que de prétendre tout couvrir. Le directeur général valide ce délai, à condition que la décision finale ne reparte pas pour un semestre de consultation.

Deux autres options restent sur la liste : un concurrent moins visible et une amélioration du dispositif existant. Thomas préférerait écarter la dernière. Elle donne l’impression de ne rien changer. Aïcha lui rappelle que le problème pourrait venir de la collecte, des responsabilités ou du réglage, et non du produit. Élise insiste : « Sans solution de référence, comment saurons-nous ce que nous achetons vraiment ? » Le maintien de l’existant devient une hypothèse à tester, pas une préférence politique.

Pendant l’essai, la plateforme recommandée réussit deux scénarios et facilite certaines investigations. Elle ne reçoit pas les événements nécessaires pour le troisième. L’assistant produit un résumé utile, puis propose une explication incorrecte que l’analyste doit corriger. Personne ne prononce le mot catastrophe. Ils notent le gain de temps, le temps de vérification et le risque d’accorder trop vite confiance au texte. Le résultat ressemble moins à une publicité, mais davantage à leur prochain quotidien.

Le fournisseur propose un développement spécifique pour le connecteur manquant. Thomas est tenté. Élise demande le prix, le responsable de maintenance et la conséquence d’un retard. La réponse reste ouverte. Ils décident que cette fonction ne comptera pas dans le bénéfice initial. Si elle devient indispensable, son absence empêchera le déploiement sur le périmètre concerné. Le commercial n’apprécie pas cette réserve, mais il peut maintenant négocier quelque chose de concret plutôt qu’une inquiétude générale.

Vient ensuite le test de sortie. Exporter les alertes paraît simple ; reprendre les règles, les annotations et l’historique l’est moins. Un format existe, mais une partie du contexte reste propre à la plateforme. Thomas demande à voir un export réutilisé ailleurs. L’équipe découvre ainsi une tâche de migration qui n’apparaissait dans aucune comparaison commerciale. Ce n’est pas forcément éliminatoire. Il faudra simplement financer la dépendance au lieu de la découvrir à l’échéance du contrat.

Lors du comité final, Thomas conserve le graphique, mais le déplace en annexe. Sa recommandation précise les résultats démontrés, les exclusions, les coûts d’exploitation et les événements qui imposeraient de revenir sur le choix. Le fournisseur réputé reste retenu, pour un périmètre limité et sous conditions. « Donc le classement avait raison ? » demande le directeur général. Thomas répond : « Il nous a aidés à regarder dans la bonne direction. Il n’a pas fait les essais à notre place. » Cette fois, la phrase répond vraiment à la question.

## Ce qui se passe vraiment

Le problème n’est pas Gartner. C’est l’usage d’un avis de marché comme substitut à une décision locale. La FAQ officielle, consultée dans sa copie archivée du 22 octobre 2026, décrit deux axes : capacité d’exécution et complétude de la vision. Elle précise que l’évaluation mobilise jusqu’à quinze critères pondérés et que l’absence d’un fournisseur ne signifie pas qu’il n’est pas viable ou compétitif.[19] Ces critères apportent une information structurée ; ils ne reproduisent pas automatiquement vos contraintes.

La même FAQ présente le Magic Quadrant comme un point de départ, pas comme l’unique outil de sélection, et distingue cette vue de marché des analyses de capacités par cas d’usage.[19] Utiliser sérieusement Gartner implique donc de dépasser l’image. La date de finalisation compte aussi : selon la FAQ, les événements postérieurs ne sont pas intégrés à l’analyse.[19] Une acquisition, une modification de support ou une évolution contractuelle demande une vérification distincte.

Il n’est pas nécessaire d’inventer une accusation de classement acheté pour critiquer un mauvais achat. Gartner affirme que le statut de client d’un fournisseur n’influence ni son inclusion ni sa position.[19] Nous rapportons cette règle déclarée, sans prétendre avoir audité son application. L’argument de ce chapitre ne dépend d’aucune hypothèse de favoritisme : même une analyse indépendante et excellente peut répondre à une autre question que la vôtre.

Le code britannique de sécurité des logiciels, actualisé en janvier 2026, propose des sujets beaucoup plus proches d’un contrat exploitable : développement sécurisé, traitement des vulnérabilités, mises à jour, niveau de support, fin de maintenance et information sur les incidents.[18] Ce code volontaire n’est ni un certificat de qualité universel ni une obligation française. Il offre une base de négociation complémentaire à l’analyse de marché.

Enfin, l’ENISA souligne en 2026 que les dépendances et les attaques touchant les tiers peuvent étendre l’impact des incidents.[1] Acheter une plateforme peut simplifier l’exploitation tout en concentrant les dépendances. Cette tension doit être évaluée, non résolue par principe en faveur du produit intégré ou de l’assemblage de spécialistes.

## Les erreurs classiques

**Confondre fournisseur et fonction.** Une entreprise peut être solide sans fournir le connecteur, la région d’hébergement ou la granularité d’accès dont vous avez besoin. Vérifiez la version, le niveau de licence et le service réellement vendus.

**Évaluer une présentation plutôt qu’une capacité.** Une démonstration choisit ses données et son chemin. Un essai utile inclut les lacunes de collecte, les erreurs, la charge d’administration et les opérations réalisées sans ingénieur commercial à proximité.

**Acheter une feuille de route au prix du disponible.** Une fonction annoncée peut justifier une veille ou une option. Elle ne doit pas porter seule le bénéfice d’un projet dont les dépenses commencent maintenant.

**Se fabriquer un alibi.** « Tout le marché le choisit » n’explique pas pourquoi le choix est adapté. À l’inverse, sélectionner un acteur peu connu pour paraître indépendant ne vaut pas davantage démonstration.

## Faire autrement

Rédigez le besoin avant la liste de fournisseurs : scénario, données nécessaires, contraintes d’exploitation et résultat attendu. Séparez les exigences éliminatoires des préférences. Une absence d’export indispensable ne doit pas être compensée arithmétiquement par une interface agréable.

Construisez une sélection courte avec des options réellement différentes. Incluez une référence : améliorer l’existant, réduire le périmètre ou ne pas acheter maintenant. Les analyses de marché aident à repérer les candidats et à préparer les questions ; elles n’attribuent pas la décision finale.

Figez le protocole d’essai avec les utilisateurs et les achats. Consignez les données disponibles, les droits accordés, les interventions du fournisseur et les résultats attendus. Comparez les options sur les mêmes scénarios. Documentez ce qui n’a pas été testé : une semaine satisfaisante ne prouve ni une année de disponibilité ni la qualité de chaque fonction.

Pour une innovation fondée sur l’IA, mesurez ensemble gain et contrôle : temps épargné, corrections nécessaires, accès aux données, possibilité d’action et retour arrière. Commencez sans autorisation autonome irréversible. Augmentez les droits seulement après des résultats reproductibles sur le périmètre convenu. Une fonction impressionnante mais invérifiable peut rester une expérimentation.

Négociez la sortie avant l’entrée : formats, historique, règles, délais, frais, assistance et suppression des données selon les obligations applicables. Faites un export utilisable. Traitez séparément les engagements contractuels et les intentions commerciales.

Enfin, écrivez les conditions d’invalidation. Coût d’exploitation dépassant la capacité prévue, couverture promise non livrée, changement de traitement des données ou défaut de support peuvent imposer une revue. La feuille de route devient alors : essai borné, décision documentée, déploiement limité, mesure en production, extension ou arrêt. Ce n’est pas moins ambitieux. C’est une ambition capable de reconnaître une erreur avant le renouvellement.

## La fiche à emporter

Avant signature, le dossier doit répondre à huit questions :

- Quel problème local justifie cette dépense ?
- Que nous apprend l’analyse de marché, avec quelle date et quel périmètre ?
- Quelles autres options ont réellement été examinées ?
- Quelles exigences sont éliminatoires ?
- Qu’avons-nous démontré, échoué ou laissé non testé ?
- Qui exploitera la solution, avec quels moyens et quels droits ?
- Comment partir, à quel coût, avec quelles données réutilisables ?
- Quel événement nous obligera à revoir notre recommandation ?

Gardez une colonne « disponible et testé » distincte de « annoncé ». Faites approuver les limites autant que les bénéfices. Le point en haut à droite peut aider à ouvrir le dossier ; il ne devrait jamais suffire à le fermer.

---

# 7. Le CISO qui décide de tout et de rien

## Mise en situation

*Fiction pédagogique : cette scène, ses personnages, ses seuils et ses décisions sont inventés. Elle illustre un problème de gouvernance et ne rapporte pas un incident réel.*

À neuf heures, Karim doit approuver une exception de mot de passe. À neuf heures dix, on lui demande si l’entreprise peut lancer un nouveau service commercial. À neuf heures vingt, une équipe attend sa signature pour ouvrir un flux entre deux applications. Dans les trois messages, la conclusion est identique : « Merci de valider la sécurité. » Karim dirige la sécurité depuis deux ans. Il possède beaucoup de demandes de validation et très peu de définitions du mot valider.

Le lancement commercial concerne une offre qui doit apporter une part importante des revenus du trimestre. Le système de gestion des accès présente une faiblesse connue. Une correction est possible, mais elle retarderait l’ouverture. La directrice commerciale, Claire, demande à Karim de prendre position. Il recommande un lancement limité avec des restrictions temporaires. « Donc tu acceptes le risque ? » demande-t-elle. « Je recommande une option. Je ne dirige pas cette activité et je ne peux pas choisir seul la perte acceptable. »

Claire soupire. Elle pense qu’il se protège derrière une nuance. Karim pense qu’elle lui demande une assurance impossible. Le directeur informatique, Luc, propose un comité exceptionnel. Il existe déjà un comité des risques, un comité des changements et un comité du programme. Aucun ne sait vraiment lequel doit trancher aujourd’hui. Leur organigramme est complet. Le calendrier, lui, commence à manquer de place pour accueillir les conséquences de cette complétude.

Une alerte interrompt la discussion. Un compte technique se comporte de manière inhabituelle sur le service de facturation. L’analyste de permanence demande l’autorisation de le suspendre. Karim veut connaître l’impact. Luc répond que le compte alimente aussi une interface de rapprochement. La documentation ne permet pas de dire si l’arrêt bloquera les factures ou seulement leur contrôle. L’analyste attend. Il n’a pas besoin d’un nouveau tableau de responsabilités ; il a besoin de savoir quelle action il a le droit de prendre.

Karim appelle la directrice générale, Anne. Elle lui demande s’il faut couper. Il explique ce qui est établi, ce qui reste inconnu et les options disponibles. « Tu es notre expert, décide », répond-elle. La phrase ressemble à une marque de confiance. Karim y entend surtout un transfert de responsabilité sans limite explicite. Il peut évaluer une suspicion de compromission. Il ne connaît pas seul les conséquences d’un arrêt de facturation pendant la clôture.

Luc propose une mesure plus ciblée : bloquer temporairement l’accès externe du compte, conserver ses journaux et surveiller les traitements internes. L’analyste confirme qu’il peut l’appliquer rapidement. Karim soutient cette option. Anne autorise la restriction, demande un point rapproché et désigne Luc pour vérifier les impacts métiers avec la finance. L’action part enfin. Elle n’a pas attendu une certitude complète, mais elle repose désormais sur une autorisation, un périmètre et un rendez-vous de réévaluation.

L’alerte se révèle liée à une intervention mal annoncée du prestataire. Les accès restent toutefois trop larges et devront être corrigés. Personne ne célèbre un faux positif : il y avait un défaut réel, même sans attaque confirmée. Anne demande pourquoi l’équipe avait attendu son appel pour restreindre un accès. Karim montre la procédure. Elle prévoit une validation de la sécurité, puis une validation de l’informatique, sans préciser les suppléants ni le traitement d’une absence de réponse.

« Nous avons donc organisé une chaîne dans laquelle chacun peut attendre quelqu’un », résume Anne. Luc nuance : la procédure venait d’un incident précédent où une coupure avait causé des difficultés. Ils avaient ajouté des signatures pour éviter de recommencer. Aucune signature ne précisait pourtant la durée maximale d’attente ni les actions réversibles autorisées. La précaution avait pris la forme d’un ralentissement général, sans garantir que les bonnes personnes seraient présentes au bon moment.

Ils réservent une séance de travail avec les responsables concernés. Karim arrive avec des décisions à prendre, pas avec un nouvel organigramme. Qui peut isoler un poste ? Qui peut suspendre un compte partagé ? Qui décide d’arrêter une activité ? Qui autorise sa reprise ? Qui parle aux clients ? La juriste demande d’ajouter les obligations de notification et leurs délais propres. La directrice de la communication rappelle qu’un message externe engage autre chose que le diagnostic technique.

Pour chaque décision, ils écrivent une autorité, un suppléant et des limites. L’équipe de réponse pourra réaliser certaines restrictions réversibles sans attendre Karim, dans un périmètre préapprouvé. L’arrêt d’un service critique restera une décision de direction, avec une procédure de remplacement si le décideur est injoignable. Les opérations touchant à la sécurité physique suivront leur propre chaîne d’autorité. Ils testent ensuite ces règles sur un scénario où deux dirigeants sont simultanément indisponibles.

Le lancement commercial revient dans la conversation. Claire accepte d’en porter l’arbitrage économique, mais refuse de signer un texte qu’elle ne comprend pas. Karim reformule les conséquences, les restrictions proposées et les preuves manquantes. Anne tranche pour une ouverture limitée, avec une échéance de correction et un arrêt automatique de l’exception si certaines conditions ne sont plus respectées. La décision n’efface pas les réserves de Karim. Elles restent jointes au dossier, sans devenir une déclaration de guerre entre services.

À la réunion suivante du conseil, Anne présente les décisions dépassant les seuils délégués et les retards qui modifient l’exposition. Karim répond aux questions techniques ; il n’est plus chargé de représenter à lui seul la volonté de toute l’entreprise. Dans sa messagerie, plusieurs demandes de validation ont disparu. D’autres sont devenues plus précises. Il conserve le droit d’alerter, de contester et d’escalader. Il perd surtout une fiction : celle d’être responsable de tout parce que son nom figurait à la fin du courriel.

## Ce qui se passe vraiment

Une fonction de sécurité ne devrait pas servir de réceptacle aux décisions que personne ne veut assumer. L’expertise sur une menace, l’autorité sur un système et la légitimité pour engager une activité sont trois choses différentes. Elles peuvent appartenir à la même personne dans une petite structure, mais cette réunion des rôles doit être explicite, pas découverte pendant une crise.

Le code britannique de gouvernance publié en avril 2025 distingue clairement le rôle des dirigeants de la gestion quotidienne de la cybersécurité. Il leur demande notamment de définir l’appétence au risque, d’établir une responsabilité de niveau dirigeant et de s’assurer que les ressources soutiennent la stratégie.[16] Il prévoit aussi un dialogue avec le CISO et une implication de la direction dans les décisions critiques en cas d’incident.[16] C’est ici un repère de gouvernance, pas une transposition automatique du droit britannique en France.

Le même code recommande des exercices au moins annuels impliquant les parties pertinentes, ainsi que l’intégration des enseignements dans les plans et les évaluations de risques.[16] La conclusion opérationnelle proposée dans ce chapitre est de tester les droits de décision pendant ces exercices. Une équipe peut connaître parfaitement son outil et rester paralysée parce qu’aucune personne disponible ne se croit autorisée à agir.

Le code britannique de sécurité des logiciels, actualisé en janvier 2026, désigne de son côté un responsable de haut niveau chargé de s’assurer que les principes sont suivis et que les équipes disposent des ressources nécessaires.[18] Cette distinction est importante : être comptable d’un résultat n’oblige pas à exécuter chaque tâche. À l’inverse, confier une tâche ne suffit pas à transférer la responsabilité de l’organisation.

Les dépendances relevées par l’ENISA en 2026 compliquent encore ces frontières : les impacts peuvent se propager entre services et fournisseurs.[1] Le CISO ne peut donc pas déduire seul la bonne décision d’un indicateur technique. Il lui faut des propriétaires de services capables d’exprimer les conséquences, et une autorité habilitée à arbitrer entre elles.

## Les erreurs classiques

**Faire du CISO un guichet universel.** Chaque approbation marginale consomme du temps et dilue la portée des vraies décisions. Réservez son intervention aux sujets où son expertise ou son autorité est effectivement nécessaire.

**Écrire un RACI sans décision concrète.** Une matrice de rôles peut aider. Elle reste vide si elle ne dit pas qui tranche, dans quel délai, avec quelles informations et quelle solution de remplacement. « Consulté » n’est pas un mécanisme de crise.

**Déléguer sans limite, puis reprocher l’initiative.** Autoriser une équipe à agir exige de définir les systèmes concernés, les effets admissibles, la traçabilité et le retour arrière. Sinon chacun apprendra que l’option la moins risquée pour sa carrière consiste à attendre.

**Confondre acceptation et permission générale.** Un responsable métier ne peut pas rendre licite une action interdite en signant une fiche de risque. Les obligations applicables doivent être qualifiées avec les fonctions compétentes ; l’arbitrage économique intervient dans ce cadre, pas à sa place.

## Faire autrement

Partez des décisions récurrentes et des décisions de crise. Pour chacune, distinguez qui formule les options, qui apporte les conséquences métier, qui tranche et qui exécute. Donnez au CISO un accès réel à l’escalade, y compris lorsqu’il conteste une décision. Son désaccord documenté est une information de gouvernance, pas une insubordination à neutraliser.

Faites approuver des délégations bornées avant l’urgence. Définissez les actions autorisées, leurs préconditions, leur durée, leurs effets maximaux et les exclusions. Ajoutez un suppléant, un canal de secours et une règle en cas d’absence de réponse. Les seuils doivent refléter votre activité ; les exemples de la fiction ne sont pas un barème universel.

Séparez le confinement, l’arrêt durable et la reprise. Une équipe autorisée à restreindre provisoirement un compte ne dispose pas nécessairement du mandat pour arrêter une chaîne de production. La reprise exige ses propres critères : preuves de maîtrise, contrôle des dépendances et acceptation du mode dégradé. « L’alerte a disparu » ne constitue pas, à lui seul, un dossier de reprise.

Pendant l’incident, tenez un journal bref : heure, faits connus, incertitudes, options, décideur, action et prochain point. Il ne s’agit pas de rédiger un procès-verbal avant de protéger un système. Il s’agit de préserver suffisamment de contexte pour coordonner l’action et comprendre ensuite pourquoi une décision raisonnable a été prise.

Au niveau du conseil, présentez les expositions dépassant les limites déléguées, les arbitrages de ressources et les dépendances majeures. Faites acter les décisions attendues plutôt que d’accumuler des indicateurs techniques. Le conseil exerce une supervision ; il ne devrait pas devenir une permanence d’autorisation des comptes utilisateurs.

Appliquez enfin ces règles à l’innovation. Une expérimentation d’agent autonome doit préciser qui autorise ses actions, sur quelles données, avec quels plafonds et quel arrêt d’urgence. Déléguer à un logiciel ne rend pas l’autorité moins nécessaire. La feuille de route de gouvernance peut commencer modestement : clarifier quelques décisions fréquentes, éprouver les absences, corriger les ambiguïtés, puis étendre. Un mécanisme exercé vaut mieux qu’un document exhaustif que personne n’ose appliquer.

## La fiche à emporter

Pour chaque décision sensible, conserver une fiche d’autorité :

- **Objet :** quelle décision exacte doit être prise ?
- **Expertise :** qui expose les faits, les incertitudes et les options ?
- **Conséquences :** quel responsable décrit l’impact sur l’activité ?
- **Autorité :** qui tranche, dans quelles limites, avec quel suppléant ?
- **Urgence :** que peut-on faire immédiatement, et que se passe-t-il sans réponse ?
- **Contraintes :** quelles obligations ou exigences de sécurité physique s’imposent ?
- **Exécution :** qui agit, journalise, vérifie et peut revenir en arrière ?
- **Réexamen :** quand l’autorisation expire-t-elle et qui décide de la reprise ?

Test décisif : simulez l’absence du CISO et du dirigeant habituel. Si personne ne peut nommer la prochaine action autorisée, la gouvernance n’est pas encore opérationnelle. Ce n’est pas une faute à distribuer ; c’est un travail à terminer.

---

# Conclusion — Une roadmap, pas une collection de bonnes intentions

Le board n’est pas l’ennemi. Les standards non plus. Les investissements passés ne sont pas forcément absurdes, la veille n’est pas une distraction par nature et les analystes ne sont pas responsables de toutes les décisions prises avec leur graphique dans la pièce.

Le problème apparaît lorsque ces éléments cessent d’éclairer une décision et commencent à la remplacer.

Nous avons suivi sept tentations : promettre une certitude, produire des preuves pour elles-mêmes, défendre les dépenses passées, collectionner les nouveautés, cacher les renoncements, emprunter une autorité extérieure et centraliser toutes les décisions. Aucune ne manque de logique à court terme. C’est précisément ce qui les rend dangereuses. Elles récompensent souvent celui qui les adopte avant de coûter à l’organisation.

La sortie n’est pas une personnalité plus héroïque. C’est une manière de décider qui survit à l’absence du héros.

## Une roadmap commence par ce que l’on refuse d’y mettre

Une liste de projets devient une roadmap lorsque quatre éléments sont visibles :

- **Le résultat attendu :** une capacité métier protégée ou rétablie, pas seulement un produit installé.
- **La séquence :** les dépendances qui rendent un projet possible et les travaux qu’il déplace.
- **La capacité disponible :** argent, temps des équipes, intégration, exploitation et conduite du changement.
- **Les portes de sortie :** ce qui déclenche un arrêt, un changement de périmètre ou une révision de priorité.

Sans ces quatre éléments, vous avez peut-être un excellent catalogue. Il peut même être joliment animé.

### Exemple travaillé : quatre chantiers, et pas six « absolument prioritaires »

**Hypothèses pédagogiques, entièrement fictives.** Une entreprise de distribution dépend de ses commandes en ligne et de sa préparation logistique. L’équipe a établi les constats suivants pour cet exemple : des accès prestataires privilégiés sont insuffisamment bornés ; la restauration technique a été exercée mais pas la reprise complète des commandes ; des alertes existent sans procédure d’intervention suffisamment testée ; plusieurs usages d’IA sont en expérimentation. Rien ne démontre encore qu’une nouvelle plateforme générale de sécurité corrigerait mieux ces lacunes que les moyens disponibles.

On suppose une enveloppe de **60 jours-personnes de changement pour le premier trimestre**, après réserve de l’exploitation courante et de la réponse aux incidents. Cette enveloppe est illustrative, pas un benchmark. Chaque métier doit encore confirmer sa contribution ; une journée de l’équipe sécurité ne remplace pas une journée de l’équipe applicative.

| Chantier retenu | Première preuve attendue | Responsable de réalisation et dépendances | Enveloppe illustrative du trimestre |
|---|---|---|---:|
| 1. Borner les accès privilégiés des prestataires | Sur le périmètre critique choisi, aucun accès ne subsiste sans propriétaire, justification et échéance ; une révocation est vérifiée côté système cible | Responsable IAM avec exploitation et propriétaires des contrats ; créneau d’intervention prestataire requis | 20 jours-personnes |
| 2. Exercer la reprise des commandes | Une commande témoin parcourt le service restauré ; les données et dépendances sont validées par le métier, pas seulement par l’outil de sauvegarde | Responsable continuité et direction des opérations, avec équipes applicatives ; environnement et créneau d’essai disponibles | 20 jours-personnes |
| 3. Fermer la boucle détection–intervention | Un scénario choisi déclenche une alerte traitable ; un intervenant joignable prend une décision et vérifie son effet | Responsable SOC avec exploitation ; autorité d’action et accès d’urgence définis | 12 jours-personnes |
| 4. Encadrer un usage d’IA réellement demandé | Le pilote respecte un périmètre de données et de permissions ; l’arrêt et la révocation sont testés avant une extension | Responsable du produit métier avec sécurité, juridique et plateforme ; propriétaire et cas d’usage identifiés | 8 jours-personnes |
| **Total** | **Quatre preuves observables, pas quatre promesses de transformation** | **Contributions à confirmer avant engagement** | **60 jours-personnes** |

Pourquoi cet ordre ? Les deux premiers chantiers traitent ici des chemins plausibles vers l’interruption d’une activité essentielle. Le troisième évite de confondre la présence d’une alerte avec une capacité de réaction. Le quatrième limite un risque en cours d’introduction sans lancer un programme disproportionné sur une hypothèse encore floue.

Ce n’est pas une hiérarchie universelle. Une campagne active visant un composant exposé pourrait imposer un travail d’urgence avant ces chantiers. Une obligation applicable et imminente peut aussi changer la séquence. Dans ce cas, on affiche le chantier déplacé et son risque résiduel. On ne conserve pas les quatre dates en ajoutant le mot « accélération » au compte rendu.

**Ce qui attend, dans cet exemple :**

- Le remplacement général de la plateforme de collecte : aucun déficit prioritaire démontré ne justifie encore le coût de migration. Réexamen si l’outil existant empêche le scénario d’intervention retenu ou si son coût complet devient insoutenable.
- L’achat d’un SOC « autonome » : la chaîne de décision et les droits d’intervention ne sont pas assez définis pour automatiser des actions sensibles. Réexamen après le chantier 3, sur des actions bornées et réversibles.
- L’extension de l’IA à de nouvelles équipes : attente des résultats du pilote, sans bloquer les usages déjà autorisés dans leurs limites.

Un report n’est donc ni un rejet idéologique ni un oubli. C’est une décision assortie d’une condition de réouverture.

## Passer du trimestre à douze mois sans lire l’avenir

- **Premier trimestre : établir et éprouver le périmètre initial.** Produire les quatre preuves ci-dessus. Si les équipes métier ne sont pas disponibles, réduire explicitement le périmètre ou décaler un chantier. Ne pas lancer quatre projets nominaux qui attendent tous la même personne.
- **Deuxième trimestre : étendre ce qui a fonctionné.** Élargir les contrôles d’accès et les exercices aux dépendances les plus critiques. Corriger les obstacles révélés avant de multiplier les déploiements. Chiffrer les coûts récurrents observés, distinctement des coûts de démarrage.
- **Troisième trimestre : investir là où la limite est démontrée.** Ouvrir un achat si les outils, compétences ou contrats existants ne permettent pas d’atteindre le résultat nécessaire. Réutiliser le scénario d’échec comme test d’acceptation. Une consultation fournisseurs arrive ici comme conséquence d’un diagnostic, pas comme son substitut.
- **Quatrième trimestre : vérifier, simplifier et renouveler les choix.** Rejouer les tests importants, supprimer les doublons dont l’inutilité est établie, préparer les renouvellements et réviser les scénarios. Un contrat coûteux ne disparaît pas au moment où l’on décide qu’il est regrettable ; vérifier son échéance et le coût de sortie.

Les trimestres donnent un rythme de revue. Ils ne garantissent pas les délais d’intégration. Le planning détaillé doit être reconstruit avec les équipes qui réalisent et exploitent, en fonction des dépendances constatées.

## La page à présenter au comité de direction

Pour chaque chantier, une fiche suffit si elle contient les éléments suivants :

- **Nous protégeons :** activité, service, utilisateurs et dépendances concernés.
- **Nous craignons :** scénario, conséquence et éléments qui le rendent plausible ici.
- **Nous savons :** preuves disponibles, périmètre observé et limites de ces preuves.
- **Nous proposons :** résultat attendu et alternative examinée, y compris l’absence de nouvel achat.
- **Nous mobilisons :** coût initial, coût récurrent et capacité des équipes concernées.
- **Nous déplaçons :** travail abandonné ou reporté, avec sa conséquence.
- **Nous vérifierons :** test d’acceptation, responsable, échéance et contrôle après changement.
- **Nous arrêterons ou modifierons si :** résultat insuffisant, coût excessif, hypothèse invalidée ou exposition nouvelle.
- **Le risque restant appartient à :** dirigeant métier habilité à décider dans les limites de sa délégation ; au-delà, escalade vers l’instance compétente.

Le conseil supervise l’appétence au risque, la gouvernance et les moyens. La direction organise les arbitrages et les responsabilités. Le CISO apporte l’analyse, les limites des contrôles et une capacité de contradiction. Présenter un risque à un conseil ne vaut pas, à lui seul, acceptation explicite de ce risque.

## Le test final : que se passe-t-il si vous avez tort ?

Une bonne décision n’est pas celle qui interdit toute erreur. C’est celle dont les hypothèses sont visibles, dont l’échec peut être détecté et dont les conséquences sont contenues autant que possible.

Avant de signer, demandez :

- Si notre lecture de la menace est fausse, quel indicateur nous le montrera ?
- Si le contrôle ne fonctionne pas, qui le découvrira avant l’attaquant ?
- Si la technologie déçoit, pouvons-nous revenir en arrière ?
- Si le budget baisse, quelle capacité devons-nous préserver et qu’abandonnons-nous réellement ?
- Si le CISO est absent, qui peut décider et sur quelle base ?

Il reste de la place pour l’innovation dans cette approche. Beaucoup, même. Mais elle doit montrer un gain dans une tâche réelle, prendre sa part des contraintes et accepter un test qui puisse échouer.

Vous n’avez pas besoin d’une roadmap impressionnante. Vous avez besoin d’une roadmap dont les premières lignes tiennent lorsque les conditions deviennent moins aimables.

Les diapositives pourront rester vertes. À condition, cette fois, que quelqu’un ait regardé derrière.

## Sources

[1] https://enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience — ENISA — Threat Landscape 2026 : dépendances et résilience
[3] https://www.enisa.europa.eu/news/supporting-nis2-implementation-through-actionable-guidance
[4] https://messervices.cyber.gouv.fr/nis2
[6] https://www.nist.gov/cyberframework
[7] https://www.theguardian.com/business/2025/may/21/cyber-attack-cost-marks-and-spencer-lost-sales-company-results-reveal
[9] https://blog.cloudflare.com/18-november-2025-outage — Cloudflare — Panne du 18 novembre 2025
[10] https://www.cisa.gov/news-events/alerts/2025/05/27/new-guidance-siem-and-soar-implementation — CISA — Recommandations SIEM et SOAR, 27 mai 2025
[11] https://www.anthropic.com/research/writing-tools-for-agents — Anthropic — Concevoir des outils pour les agents, 11 septembre 2025
[13] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — Anthropic — Demystifying evals for AI agents — 9 janvier 2026
[16] https://www.gov.uk/government/publications/cyber-governance-code-of-practice/cyber-governance-code-of-practice — Gouvernement britannique — Code de gouvernance cyber, 8 avril 2025
[17] https://www.cisa.gov/news-events/news/continued-progress-towards-secure-open-source-ecosystem — CISA — Progrès vers un écosystème libre sécurisé, 8 juillet 2024 (fondation)
[18] https://www.gov.uk/government/publications/software-security-code-of-practice/software-security-code-of-practice — Gouvernement britannique — Code de sécurité des logiciels, mise à jour du 15 janvier 2026
[19] https://web.archive.org/web/20261022073220/https://www.gartner.com/en/about/magic-quadrant-faq — Gartner — FAQ Magic Quadrant, archive du 22 octobre 2026
