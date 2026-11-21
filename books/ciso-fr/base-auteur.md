# La sécurité n’est pas un concours de slides

## Menaces réelles, dépenses utiles et décisions défendables — base de travail pour un livre de CISO

- **Format :** matière à écrire, pas texte à publier tel quel ; arguments, tensions, enchaînements et outils.
- **Angle :** comprendre pourquoi des décisions individuellement raisonnables produisent parfois une sécurité collectivement absurde.
- **Cible de l’ironie :** les incitations et les raccourcis de l’industrie ; pas les équipes sous-financées ni les dirigeants supposés idiots.
- **Promesse :** savoir quoi financer, quoi conserver, quoi arrêter et ce qui ferait changer d’avis.
- **Règle éditoriale :** les positions et méthodes ci-dessous sont des propositions de l’auteur ; les faits externes portent des références. Aucun dialogue, client, résultat d’essai ou budget inventé.

# Introduction — Trois choses que l’on confond trop facilement

- **Nœud central : menace / obligation / offre commerciale.**
  - Menace : mécanisme susceptible de provoquer une perte sur une activité donnée.
  - Obligation : exigence applicable, dont le respect peut être nécessaire indépendamment d’un classement interne des risques.
  - Offre : moyen possible de répondre à un besoin ; son existence ne prouve pas la priorité du besoin.
  - Quatrième dimension à ne pas mépriser : assurance donnée à un client, un régulateur ou un dirigeant. Démontrer peut être une obligation ou une condition d’accès au marché, pas seulement du théâtre.
- **Position à défendre :** une stratégie cyber n’est ni un catalogue de technologies ni une collection d’interdictions ; c’est une allocation de capacités sous contraintes.
- **Objection sérieuse :** attendre une preuve parfaite peut coûter plus cher que décider avec une information incomplète.
  - Réponse : ajuster la profondeur de l’analyse à l’impact et à la réversibilité ; autoriser une décision provisoire, pas une certitude provisoire.
- **Socle de menace :** l’ENISA décrit en 2026 des menaces persistantes et des dépendances numériques ; les événements analysés dans cette édition portent sur 2025.[1]
  - À en tirer : des familles de scénarios à examiner.
  - À ne pas en tirer : une probabilité locale, un budget « nécessaire » ou un ordre automatique des projets.
- **Fil conducteur des sept chapitres :**
  - 1 — obtenir un arbitrage stratégique ;
  - 2 — déterminer ce qui oblige réellement ;
  - 3 — réévaluer ce qui est déjà acheté ;
  - 4 — décider ce qui mérite une expérience ;
  - 5 — rendre le programme exécutable ;
  - 6 — choisir un fournisseur sans emprunter son jugement ;
  - 7 — distribuer le pouvoir d’agir.
- **Questions de départ pour l’auteur :**
  - Quelle dépense apparemment bureaucratique était en réalité nécessaire ?
  - Quelle innovation séduisante mérite tout de même d’être adoptée ?
  - Quel investissement techniquement bon a échoué faute d’organisation ?
- **Trait d’ironie possible :** « Le catalogue est complet. Il reste à choisir ce que nous voulons protéger. »

## Trois exigences de lecture pour un CISO senior

- **Une bonne décision peut rester imparfaite :** le livre doit expliquer ce qu’elle sacrifie, pas seulement pourquoi l’alternative est mauvaise. Exiger à la fois indépendance totale, exploitation minimale et coût réduit peut rendre toute option irréalisable.
- **La rationalité locale ne garantit pas la solidité collective :** des contrats, exceptions et projets acceptables séparément peuvent dépendre du même moyen d’administration ou de la même compétence rare. Rendre visible ce qui échouerait ensemble.
- **La recommandation doit supporter sa défaite :** prévoir ce qui se passe si le budget est refusé, le fournisseur ne négocie pas, l’autorité tranche autrement ou le prérequis n’arrive pas ; une escalade n’est pas une résolution tant que personne n’a décidé.
- **Adapter le niveau de formalisation :** approfondir les décisions à impact fort, difficiles à inverser ou reposant sur une assurance fragile ; ne pas imposer sept formulaires à une action courante déjà autorisée.
- **Trois fils, répartis plutôt que répétés :** portefeuille de dépendances (chapitre 3 → arbitrage du 1) ; temps et preuves qui vieillissent (2, 4, 5) ; pouvoir réel et désaccord (6, 7).

# 1 — Le CISO challengé par le board

## Nœud et frontière du chapitre

- **Question centrale :** comment comparer une dépense cyber aux autres emplois des ressources sans promettre l’immunité ?
- **Ne pas empiéter sur le chapitre 7 :** ici, arbitrage stratégique et information de direction ; là-bas, autorité opérationnelle et gestion des exceptions.
- **Point de départ à développer :** demande de justification budgétaire face à un lancement, une acquisition ou une réduction de coûts ; pas un board transformé en tribunal ignorant.

## Thèse, contre-thèse, position

- **Thèse :** la direction n’achète pas une technologie ; elle décide quel niveau de perte et de perturbation l’entreprise peut supporter, dans les limites des obligations applicables.
- **Contre-thèse :** elle a raison de demander des résultats, une synthèse et une comparaison économique ; « le risque est difficile à mesurer » ne dispense pas de rendre compte.
- **Position :** distinguer ce qui est observé, estimé et inconnu ; montrer les options et l’incertitude qui pourrait inverser leur ordre.
- **Cas où la pratique courante est justifiée :**
  - Un indicateur synthétique est utile si son périmètre et ses exceptions sont visibles.
  - Une quantification est utile si les hypothèses sont explicites et la décision testée contre plusieurs valeurs plausibles.
  - Un financement de conformité peut rester rationnel même si sa contribution à la réduction d’une menace est difficile à isoler.

## Ce qui pousse à mal décider

- **CISO :** incitation à dramatiser pour obtenir les moyens, puis à rassurer pour démontrer leur utilité.
- **Finance :** besoin de comparer ; risque de privilégier ce qui se chiffre facilement plutôt que ce qui compte vraiment.
- **Métier :** coût du retard immédiatement visible ; coût d’un incident incertain et partagé.
- **Direction :** demande de certitude pouvant masquer une question légitime : « que dois-je décider aujourd’hui ? »
- **Contradiction à exploiter :** demander au CISO d’être alarmant au budget et rassurant au reporting ; le même risque change de couleur selon le calendrier.

## Arguments et distinctions à développer

- **Séparer trois justifications d’investissement :**
  - Économie observable : dépense supprimée, temps effectivement libéré, contrat remplacé.
  - Réduction de risque : scénario, exposition, contrôles et incertitudes ; pas une économie comptable automatiquement encaissable.
  - Condition d’activité : exigence juridique, contractuelle ou client à qualifier précisément.
- **Ne pas interdire le ROI :** refuser le ROI inventé ; conserver le calcul lorsqu’un bénéfice incrémental et ses coûts sont mesurables.
- **Arbitrage technique derrière la dépense :** pour un même scénario, comparer réduction d’exposition, prévention, détection/confinement et reprise ; apprécier délai, réversibilité, dépendances et perte résiduelle. L’assurance peut transférer une partie du coût financier, pas rétablir à elle seule le service ; la combiner aux mécanismes techniques plutôt que l’y substituer.
- **Éviter l’incident-totem :** le cas M&S rapporté en mai 2025 peut illustrer les catégories d’impacts économiques et le caractère provisoire d’une estimation ; il ne permet pas de chiffrer votre risque.[7]
- **Distinguer les organes réels :** conseil, président, direction générale, comité exécutif ; « board » est ici un raccourci, pas une attribution juridique universelle.
- **Ancrage réglementaire :** l’article 20 de NIS 2 traite de l’approbation et de la supervision des mesures par les organes de direction ; ne pas en déduire une sanction française précise sans vérifier le droit applicable.[14]

## Décision senior : quand attendre est déjà choisir

- **Dilemme :** suspendre un lancement pour lever une incertitude de reprise, ou autoriser un périmètre limité en conservant une exposition connue. Le conseil peut avoir raison de refuser une étude supplémentaire si son résultat ne peut plus changer la décision utile.
- **Distinguer trois temps :** temps nécessaire pour décider, temps avant effet du contrôle et temps pendant lequel le service reste exposé. Une solution supérieure à terme peut arriver après la fenêtre où elle était utile.
- **Information discriminante :** demander quel résultat ferait préférer l’autre option. S’il n’en existe aucun, l’étude sert probablement à rassurer, à gagner du temps ou à justifier un choix déjà pris ; nommer cette fonction au lieu d’appeler cela de l’analyse.
- **Portefeuille :** plusieurs acceptations locales peuvent dépendre de la même identité, du même prestataire ou de la même ressource rare. Faire remonter la conséquence simultanée au niveau compétent, sans additionner des scores hétérogènes ; la cartographie technique est développée au chapitre 3.
- **Choix défendable mais imparfait :** conserver une concentration réellement exploitable plutôt que financer une diversité sans compétence pour la tenir ; montrer ce qui resterait utilisable si la dépendance commune tombait.
- **Le piège du CISO :** attendre une preuve exhaustive pour protéger sa recommandation alors que le coût du retard ou la fermeture d’une option est déjà visible. La prudence doit aussi rendre compte de ce qu’elle laisse se produire.
- **Limite :** l’urgence économique ne crée ni exemption juridique ni délégation implicite. Une mesure provisoire reste bornée par les pouvoirs existants et les contraintes applicables.

## Erreurs à attaquer

- Budget construit comme une liste de produits, sans activité protégée ni alternative.
- Maturité globale utilisée pour masquer une dépendance critique non testée.
- Absence d’incident présentée comme preuve du succès de tous les investissements.
- Signature du dirigeant interprétée comme autorisation d’ignorer la loi.
- « Réduction de risque » présentée sans préciser quel risque subsiste et sur quel périmètre.

## Outil : note décider / attendre / préserver une option

- **Choix à trancher :** option retenue, meilleure alternative réalisable et raison de ne pas la retenir ; pas une liste de solutions également prioritaires.
- **Fenêtre :** événement qui impose la décision, option qui disparaît si l’on attend, exposition et coûts maintenus pendant ce temps.
- **Inconnue discriminante :** information encore susceptible d’inverser le choix, moyen de l’obtenir et effort proportionné ; sinon arrêter l’étude.
- **Conséquence collective :** services susceptibles de tomber ensemble, capacité de reprise restante et ressource disputée entre programmes.
- **Mandat :** contributions métier, finance, CISO et exploitation ; autorité habilitée ; désaccord résiduel conservé, sans fausse unanimité.
- **Si la réunion ne tranche pas :** décision actuellement en vigueur, responsable du provisoire, limites et prochaine escalade ; ne pas convertir le silence en acceptation.
- **Preuve et inversion :** contrôler le résultat et l’hypothèse décisive ; rouvrir si le service attendu ne peut plus être tenu, pas seulement si le budget change.

## Matière à apporter par l’auteur

- Un arbitrage où la finance avait raison contre la sécurité.
- **Question :** quelle hypothèse économique, si elle était fausse, inverserait la décision proposée à la direction ?
- Un indicateur utile au dirigeant mais dangereux lorsqu’on en retire le périmètre.
- Une décision qui a changé après découverte d’une dépendance métier.
- **Ironie possible :** « Le risque est sous contrôle. Le périmètre du graphique aussi. »

# 2 — Le CISO bouffé par les standards

## Nœud et frontière du chapitre

- **Question centrale :** qu’est-ce qui nous oblige, et quelle preuve démontre réellement quoi ?
- **Point de départ à développer :** la même équipe répond à plusieurs audits, appels d’offres et régimes juridiques ; les pièces se ressemblent, les périmètres non.
- **Ne pas confondre :** droit, certification, guide technique, exigence d’assureur et clause client.

## Thèse, contre-thèse, position

- **Thèse :** un taux de conformité peut augmenter tandis qu’un service critique reste mal maîtrisé.
- **Contre-thèse :** la documentation, les responsabilités et la traçabilité peuvent être des contrôles à part entière ; pas une taxe administrative par nature.
- **Position :** mutualiser les contrôles et les preuves, jamais inventer l’équivalence des exigences.
- **Quand l’auditeur a raison :** preuve hors période, périmètre incomplet, exception non exécutée, déclaration invérifiable.
- **Quand l’outil GRC se justifie :** volume et répétition mesurés, propriétaires identifiés, règles de conservation définies ; pas pour découvrir après l’achat qui fait le travail.

## Mécanismes et contradictions

- **Effet de score :** réduire le périmètre ou reclasser un écart peut améliorer un tableau sans modifier l’exposition.
- **Effet de calendrier :** préparer l’audit devient une activité séparée de l’exploitation.
- **Effet commercial :** une nouvelle clause client introduit une charge récurrente sans budget associé.
- **Contradiction utile :** vouloir une preuve unique pour tout, puis exiger que chaque audit démontre une réalité différente.

## Conséquence opérationnelle des exigences

- **Avant le contrôle :** qualifier entité, activité, pays, texte applicable et échéance ; distinguer droit, guide et contrat. Les registres doivent conclure, pas seulement accumuler les noms de textes.
- **Avant la crise :** préparer qualification, envoi, suppléance et destinataires ; ne pas attendre une certitude exhaustive ni le prochain comité pour suivre la procédure applicable.
- **Avant de mutualiser :** vérifier que la même preuve couvre les populations, périodes et modalités requises ; documenter les différences au lieu d’inventer une équivalence.
- **Repères de droit et délais :** voir l’[annexe juridique](#annexe-juridique). Pas de verdict français de transposition déduit d’un portail ni de délai universel appliqué à toute alerte.

## Décision senior : quand une preuve cesse de prouver

- **Dilemme :** réutiliser un test de restauration après modification du chemin d’administration, ou remobiliser l’exploitation pour refaire la démonstration. L’auditeur a raison si le changement touche l’hypothèse testée ; une nouvelle capture sans changement pertinent n’apporte pas nécessairement plus d’assurance.
- **Deux dimensions :** efficacité du contrôle et confiance dans ce que l’on en sait. Un essai rigoureux mais étroit n’établit pas une couverture générale ; un inventaire complet de déclarations n’établit pas un fonctionnement réel.
- **La date ne suffit pas :** une preuve devient caduque si identité, configuration, connecteur, périmètre ou mode d’exploitation changent d’une façon qui invalide sa conclusion. À l’inverse, ancienne ne signifie pas automatiquement inutile.
- **Échantillonnage :** conserver population, exclusions et raisons du choix ; inclure les exceptions ou les chemins difficiles qui pourraient renverser la conclusion. Ne pas laisser celui qui prépare l’audit sélectionner seulement les cas qu’il sait réussir.
- **Désaccord avec l’audit :** séparer contrôle défaillant, preuve insuffisante et interprétation différente de l’exigence. Corriger un système, refaire un test ou résoudre une interprétation sont trois travaux distincts.
- **Mesure compensatoire :** expliquer le mécanisme couvert, la limite et la vérification ; faire confirmer sa recevabilité. Une alternative techniquement séduisante ne satisfait pas automatiquement une exigence prescriptive.
- **Le piège du CISO :** demander le même niveau de preuve à chaque contrôle et produire une nouvelle bureaucratie au nom de la lutte contre la bureaucratie. Réserver le traitement approfondi aux preuves qui portent une décision importante.

## Erreurs à attaquer

- Appeler « obligation NIS 2 » toute recommandation d’un guide.
- Confondre certification d’un système de management et assurance de résistance à chaque attaque.
- Afficher « couvert » quand la correspondance n’est que partielle.
- Optimiser la production de captures alors que le contrôle sous-jacent n’est pas réalisé.
- Supprimer une conservation de preuve parce qu’elle n’aide pas directement le SOC, sans vérifier son autre finalité.

## Outil : registre d’applicabilité et passeport des preuves critiques

- **Applicabilité — juridique/conformité avec métiers :** texte, article, statut, entité, service, pays, date, autorité et articulation. Le catalogue opérationnel reste distinct du registre juridique.
- **Affirmation soutenue :** ce que la preuve établit exactement ; intention, installation ou fonctionnement. Aucun niveau ne remplace automatiquement l’autre.
- **Domaine de validité :** population, période, environnement, méthode, échantillon, exclusions et indépendance de la vérification ; ne pas effacer un échec en réduisant silencieusement le périmètre.
- **Déclencheurs de retest :** changements qui invalident la conclusion ; responsable chargé de les détecter et décision à suspendre, restreindre ou réexaminer si l’assurance disparaît.
- **Écart :** contrôle à corriger, preuve à compléter ou interprétation à trancher ; propriétaire et effet opérationnel, pas seulement couleur dans l’outil GRC.
- **Notifications :** qualification, envoi, suppléants, destinataires et horloges par régime ; détail maintenable en annexe juridique, sans attendre de compléter tous les dossiers de preuve pour traiter un incident.
- **Preuve et inversion :** retrouver un contrôle réellement exécuté avec ses exclusions ; refaire le test si l’hypothèse essentielle change, réutiliser la pièce lorsque son domaine de validité demeure pertinent.

## Matière à apporter par l’auteur

- Un audit qui a découvert un risque réel que l’équipe avait normalisé.
- **Question :** quelle preuve réclamée plusieurs fois peut être réutilisée, et quelle différence de périmètre interdit cette mutualisation ?
- Une exigence client coûteuse dont la négociation a réduit la charge sans dégrader la sécurité.
- Une correspondance trompeuse entre deux référentiels.
- **Ironie possible :** « Nous avons trois preuves du contrôle. Il nous manque le contrôle. »

# 3 — Le CISO qui veut trop valoriser ses investissements

## Nœud et frontière du chapitre

- **Question centrale :** faut-il continuer à financer ce que l’on possède déjà ?
- **Ne pas refaire le chapitre achat :** ici, arbitrage de renouvellement et dette d’exploitation ; chapitre 6, sélection et engagements fournisseur.
- **Point de départ à développer :** taux d’adoption faible, modules inutilisés, renouvellement proche ; injonction à « rentabiliser » sans vérifier le besoin.

## Thèse, contre-thèse, position

- **Thèse :** une dépense passée ne justifie pas une dépense supplémentaire.
- **Contre-thèse :** la migration, les pénalités, la double exploitation et la perte de compétences sont bien des coûts futurs ; sortir n’est pas automatiquement courageux ou rationnel.
- **Position :** comparer les options futures, pas réécrire le procès de l’achat initial.
- **Quand conserver est le bon choix :** capacité nécessaire éprouvée, coût de correction maîtrisable, alternative non supérieure sur le besoin réel, transition plus risquée que le maintien.
- **Quand consolider est rationnel :** réduction démontrée du travail d’intégration et des angles morts ; concentration des dépendances identifiée et tolérable.

## Le modèle central : cinq états, cinq questions

- **Acheté :** quel droit contractuel, quelle version, quels coûts variables ?
- **Déployé :** sur quels systèmes et identités, avec quelles exclusions ?
- **Alimenté :** les données utiles arrivent-elles, avec quelle complétude et fraîcheur ?
- **Exploité :** qui règle, analyse et agit, y compris pendant les absences ?
- **Éprouvé :** quel scénario a réellement été testé, avec quelle limite de transfert ?
- **Erreur de raisonnement :** franchir mentalement les cinq étapes en lisant la facture.
- **Appui technique :** l’alerte CISA du 27 mai 2025 présente notamment un guide de priorisation des journaux à ingérer pour la détection et la réponse ; ce n’est pas une étude de ROI.[10]

## Dilemmes à développer

- **Règle trop bruyante :**
  - Sans valeur utile démontrée : supprimer ou réduire peut être rationnel.
  - Nécessaire mais inexploitable : corriger la source, la logique, le périmètre ou la capacité de traitement ; ne pas compter sa présence comme couverture.
- **Plateforme unique :**
  - Gains possibles : contexte partagé, administration et intégrations réduites.
  - Risques à tester : plan d’administration commun, authentification commune, panne corrélée, sortie coûteuse.
  - Plusieurs logos ne prouvent pas l’indépendance : vérifier les dépendances communes réelles.
- **Coût évité :** distinguer baisse de facture, temps libéré et perte probabiliste ; ne pas les additionner comme des euros équivalents.
- **Contre-exemple à l’anti-plateforme :** un module peu utilisé peut être indispensable pour un scénario rare et grave ; faible fréquence ne signifie pas faible valeur.

## Décision senior : plusieurs bons contrats peuvent faire une mauvaise architecture

- **Dilemme :** consolider pour rendre enfin la supervision exploitable, tout en maintenant une capacité indépendante de reprise. Le fournisseur peut avoir raison sur la dispersion inefficace ; cela ne démontre pas que prévention, détection et reprise doivent partager tous leurs moyens de contrôle.
- **Défaillance commune :** relier les fonctions aux identités d’administration, données, connecteurs, prestataires, canaux de support et compétences dont elles dépendent. Plusieurs logos peuvent partager le même point de rupture.
- **Indépendance utile :** préciser ce qui continue de fonctionner pendant la perte du fournisseur ou du système d’identité central, et qui sait l’opérer. Une redondance non exerçable est une charge, pas une assurance.
- **Actifs cachés du legacy :** détections, historiques, automatismes, exceptions et connaissances d’exploitation. Leur valeur ne se réduit pas à la licence ; leur transfert ne se démontre pas avec un export qui n’a jamais été réutilisé.
- **Coût de sortie futur :** distinguer ce qui a déjà été perdu, ce qui reste contractuellement dû et ce que la transition créerait. Le raisonnement contre les coûts irrécupérables ne fait pas disparaître les contraintes de liquidité ou d’exploitation.
- **Décision inconfortable :** renouveler ce qu’on n’achèterait plus, parce que la sortie maintenant détruirait une capacité essentielle ; associer le renouvellement à un découplage réalisable, pas à une promesse sans équipe.
- **Le piège du CISO :** défendre sa réputation par un produit ou démontrer son courage par une migration. Dans les deux cas, l’identité du décideur devient un critère de portefeuille clandestin.

## Erreurs à attaquer

- Activer un module pour améliorer le taux d’adoption plutôt que répondre à un besoin.
- Présenter le silence comme une preuve de sécurité sans vérifier la collecte.
- Imputer au produit un défaut de processus, ou inversement couvrir un défaut produit avec du travail humain sans le compter.
- « Économiser » en supprimant la licence mais en conservant intégralement le travail.
- Interpréter un post-mortem public comme une démonstration de l’architecture à acheter.

## Outil : renouvellement et carte des défaillances communes

- **Options :** maintenir, réparer, réduire, remplacer ; écarter explicitement celles qui n’ont ni capacité ni trajectoire crédible.
- **Fonctions liées :** ce qui disparaît ensemble en cas de défaillance commune ; service minimum préservé et indépendance réellement exploitée.
- **Sortie au premier jour :** données, détections, preuves, compétences et interfaces perdues ; obligations de conservation et accès à maintenir.
- **Coûts futurs :** maintien, correction, chevauchement, transfert et retrait ; séparer cible économique et moyens nécessaires pour l’atteindre (chapitre 5).
- **Arbitrage de portefeuille :** risque commun accepté par l’autorité compétente, pas uniquement renouvellement approuvé par chaque propriétaire de contrat.
- **Preuve :** exercer un scénario de perte du moyen commun et réutiliser hors du produit un élément indispensable ; consigner les limites non testées.
- **Inversion :** conserver ou consolider si la capacité réellement tenue s’améliore ; préserver une fonction indépendante si la concentration rend plusieurs scénarios simultanément intolérables et si cette indépendance est soutenable.

## Matière à apporter par l’auteur

- Un mauvais achat devenu utile après correction de l’exploitation.
- **Question :** quel coût futur ou quelle limite prouvée justifierait de conserver un produit que l’on n’achèterait plus aujourd’hui ?
- Un bon produit qu’il fallait arrêter faute de capacité ou de besoin.
- Un renouvellement assumé sans promesse de transformation.
- **Ironie possible :** « Le module est inclus. Son exploitation, beaucoup moins. »

# 4 — Le CISO perdu dans la veille techno

## Nœud et frontière du chapitre

- **Question centrale :** quelle information mérite une action immédiate, une expérience ou simplement de rester dans la bibliothèque ?
- **Point de départ à développer :** avis de vulnérabilité, annonce fournisseur et vidéo transférée par la direction arrivent dans la même boîte ; ils n’ont ni le même degré d’urgence ni le même statut de preuve.

## Thèse, contre-thèse, position

- **Thèse :** la veille devient utile lorsqu’elle modifie une décision, pas lorsqu’elle remplit un tableau de tendances.
- **Contre-thèse :** une exploration sans cas d’usage immédiat peut révéler un changement structurel ; tout filtrer par les projets actuels rend aveugle.
- **Position :** réserver un espace exploratoire, mais ne pas lui accorder automatiquement un budget de production.
- **Quand agir vite :** exposition plausible à une exploitation en cours ; l’investigation et les mesures conservatoires n’attendent pas une revue d’innovation.
- **Quand essayer malgré l’incertitude :** coût et rayon d’impact bornés, apprentissage utile, possibilité d’arrêt ; un pilote peut acheter de l’information plutôt qu’un rendement immédiat.

## Les trois files de veille

- **Exposition urgente :** composant/identité concerné, présence réelle, exposition, indices de compromission, correctif ou mitigation, propriétaire ; si aucune option technique suffisante, proposer restriction ou suspension à l’autorité prévue au chapitre 7 et n’exécuter que les mesures autorisées ou préautorisées.
- **Décision d’évolution :** problème, alternative, date de décision, preuve recherchée ; architecture, compétences, changements de marché et technologies, pas uniquement IA.
- **Exploration :** sujet à potentiel encore mal défini, effort borné, signal qui le ferait passer dans l’autre file.
- **Règle :** ne pas confondre fréquence de publication et fréquence de changement nécessaire.

## Appliquer la méthode à plusieurs innovations

- **Contrôle d’accès ou plateforme réseau :** promesse à tester sur compatibilité, modes dégradés, latence et exploitation ; pas seulement sur une démonstration nominale.
- **Évolution cryptographique :** examiner durée de sensibilité des données, actifs concernés, dépendances protocolaires et capacité de migration ; ne pas remplacer toute l’infrastructure à partir d’une date prophétique.
- **Automatisation classique :** si des règles et des entrées stables suffisent, comparer cette option avant d’ajouter un modèle.
- **IA et agents :** séparer qualité de l’assistance, accès aux données et pouvoir d’action ; chaque axe peut introduire une limite différente.

## Cas approfondi : agent IA, sans le confondre avec toute l’innovation

- **Avant les tests :** données autorisées, destinations, sous-traitants, rétention, usage pour l’entraînement, secrets, contraintes contractuelles ; la lecture seule peut déjà divulguer.
- **Au niveau système :** identité dédiée, droits minimaux, limites d’action et sorties contrôlées ; une consigne au modèle n’est pas une barrière d’autorisation.
- **Protocole :** mêmes tâches que la référence actuelle ; cas difficiles et cas où il faut refuser ; essais répétés ; jeu tenu à part ; temps humain de correction compris.
- **Résultat :** vérifier l’état du système cible, pas le récit de l’agent ; tenir compte des actions partielles et des sessions encore actives.
- **Arrêt :** stopper l’orchestration, révoquer les accès, terminer les sessions ou travaux en cours lorsque nécessaire et vérifier l’effet ; un bouton d’arrêt n’annule pas une divulgation déjà faite.
- **Limite des sources :** le texte d’Anthropic sur les outils demande d’associer chaque tâche d’évaluation à une réponse ou un résultat vérifiable.[11] Son texte sur les évaluations définit le résultat comme l’état final de l’environnement.[13]
  - Usage proposé : vérifier l’effet plutôt que croire le récit de l’agent ; retours du concepteur, pas comparaison indépendante des fournisseurs.

## Décision senior : un pilote peut réussir sans rien nous apprendre

- **Dilemme :** adopter une assistance qui accélère les cas simples mais déplace la vérification des cas sensibles vers les rares experts ; ou prolonger un essai qui consomme précisément la capacité qu’il promet de libérer.
- **Réfutabilité :** nommer un résultat qui ferait abandonner. Si tout résultat peut être présenté comme une invitation à prolonger, l’essai est devenu un programme d’adoption déguisé.
- **Valeur d’information :** demander quelle option réellement disponible peut changer grâce à l’essai ; comparer ce gain de connaissance à l’effort, au retard et à l’exposition introduite, sans inventer sa valeur en euros.
- **Irréversibilité :** divulgation, action externe ou engagement ne s’annulent pas par arrêt du pilote. Définir les effets admissibles avant de choisir les données et les droits ; le bouton d’arrêt ne remplace pas cette limite.
- **Transfert :** distinguer performance du produit et contribution temporaire des spécialistes fournisseur. Tester avec les données, les compétences et les contraintes qui resteront après leur départ.
- **Contre-argument fournisseur :** un essai irréaliste peut disqualifier à tort une solution utile. Construire avec lui les conditions représentatives, sans lui confier seul le choix des cas ou le verdict.
- **Le piège du CISO :** opposer un refus abstrait à un usage déjà recherché par le métier, sans alternative praticable. Proposer un périmètre autorisé ou une autre manière de réaliser la tâche ; la pression du sponsor ne vaut pas autorisation.

## Erreurs à attaquer

- Assimiler une démonstration à un essai sur l’environnement cible.
- Mesurer le temps de génération sans le temps de vérification.
- Tester uniquement des cas positifs.
- Automatiser un processus dont les droits et les exceptions sont indéfinis.
- Rejeter toute nouveauté parce qu’un produit déçoit ; adopter toute une catégorie parce qu’un pilote réussit.

## Outil : contrat d’apprentissage et transfert en exploitation

- **Décision visée :** adopter, limiter, différer ou abandonner ; inconnue qui peut encore changer cette décision.
- **Référence :** méthode actuelle et option plus simple ; mêmes tâches pertinentes et même comptabilisation du travail humain.
- **Résultat disqualifiant :** erreur intolérable, dépendance inexploitable, gain annulé par la supervision ; critères fixés avant les résultats.
- **Effets non annulables :** données, actions et engagements autorisés ; responsable, limites techniques et conditions d’arrêt avant le premier essai.
- **Transfert :** soutien temporaire identifié, équipe d’exploitation, charge récurrente, cas exclus et variations d’entrées ; un résultat favorable ne prouve pas sa généralisation.
- **Preuve :** état du système cible, essais difficiles et de refus, temps de correction ; revalidation si modèle, outils, données ou périmètre changent matériellement.
- **Inversion et sortie :** si aucune nouvelle observation ne peut changer l’option, arrêter l’étude et décider ; si le service reste inexploitable, ne pas le renommer pilote permanent.

## Matière à apporter par l’auteur

- Une innovation d’abord rejetée qui a résolu un problème concret.
- **Question :** quel résultat donnerait raison à l’option la plus simple, même si l’innovation reçoit toute l’attention ?
- Un signal urgent noyé dans une veille trop large.
- Un pilote arrêté dont l’apprentissage a évité un mauvais contrat.
- **Ironie possible :** « La démo a réussi. Il reste à essayer notre problème. »

# 5 — Le CISO qui n’a pas d’argent

## Nœud et frontière du chapitre

- **Question centrale :** quels engagements peut-on réellement tenir avec l’argent, les compétences et la disponibilité présents ?
- **Différence avec le chapitre 3 :** portefeuille complet et capacité de travail, pas rentabilité d’un contrat isolé.
- **Point de départ :** budget stabilisé ou réduit, exigences supplémentaires, même équipe ; le manque d’argent n’est ni une faute morale ni une dispense d’arbitrage.

## Thèse, contre-thèse, position

- **Thèse :** un plan sous-financé ne devient pas exécutable en le baptisant « priorité ».
- **Contre-thèse :** certaines activités peuvent être simplifiées, certaines dépenses supprimées, certains modes de réalisation changés ; demander plus n’est pas toujours la bonne première réponse.
- **Position :** distinguer gaspillage, dette et contrainte structurelle ; une même coupe ne traite pas les trois.
- **Quand une hausse est nécessaire :** activité obligatoire ou critique non soutenable malgré un périmètre rationalisé ; expliciter alors augmentation, réduction d’activité ou autre arbitrage de direction, pas une promesse héroïque.

## Trois budgets à ne pas fusionner

- **Argent :** contrats, consommation variable, prestations, formation, maintien et sortie.
- **Capacité de changement :** intégration, migration, remédiation, disponibilité des équipes métier et IT.
- **Capacité récurrente :** supervision, réponse, mises à jour, gestion des accès, preuves, absences et incidents.
- **Contradiction :** l’automatisation peut libérer du travail récurrent après avoir consommé une capacité de changement que l’équipe n’a pas encore.
- **Indicateur utile :** engagements en cours, dépendance rare et file d’attente réelle ; éviter de réduire la capacité à un nombre d’ETP interchangeables.

## Arbitrages concrets

- **MDR/MSSP :**
  - Valeur possible : accès à une compétence rare, couverture élargie, réduction de certaines tâches internes.
  - À conserver en interne ou attribuer explicitement : propriétaire du service, décisions métier, interfaces, accès d’urgence et capacité à challenger le prestataire.
  - Test : réception → qualification → notification → action autorisée → vérification ; ne pas acheter « 24/7 » sans demander ce qui est réellement assuré à chaque étape.
- **Logiciel libre :**
  - Gain possible sur licence, souplesse et indépendance.
  - Charge possible sur maintien, intégration, expertise et soutien ; la CISA rappelle la diligence continue attendue des utilisateurs de projets libres.[17]
  - Inversion : préférer un service payant si le coût d’exploitation ou l’absence de relais rend le maintien interne fragile ; préférer le libre si compétences et responsabilités sont soutenables.
- **Collecte et stockage :** distinguer sources nécessaires à la détection, à l’enquête et aux obligations de conservation ; réduire après qualification, pas au seul volume.
- **Suppression d’un service ou d’une exposition :** parfois plus efficace que protéger indéfiniment un usage marginal ; accord métier et vérification des dépendances avant arrêt.

## Décision senior : la cible est finançable, le passage ne l’est pas

- **Dilemme :** remplacer une plateforme coûteuse alors que la migration monopoliserait l’équipe nécessaire à la reprise ; ou payer un renouvellement limité pour sécuriser d’abord cette reprise. Une économie cible ne finance pas automatiquement sa transition.
- **Goulot :** équipe identité, réseau, métier, achats ou intégration ; obtenir de son responsable une capacité dans la fenêtre utile. Un accord de principe n’est pas une ressource planifiable.
- **Trois gains différents :** facture supprimée à une date réelle ; heures de travail libérées ; capacité réaffectable au chantier suivant. La finance peut avoir raison d’exiger du cash : les deux derniers ne paient pas automatiquement une facture.
- **Trajectoire :** prérequis, fenêtres de changement, double exploitation, période de couverture incomplète, transfert des compétences et fermeture effective de l’ancien dispositif.
- **Allocation marginale :** financer ce qui lève la prochaine limite du scénario prioritaire ; davantage d’alertes ne résout pas une absence d’autorité pour agir.
- **Concentration après les coupes :** regarder quel contrôle, fournisseur ou individu porte désormais plusieurs engagements. Une économie locale peut déplacer une fragilité sur le portefeuille.
- **Le piège du CISO :** lisser la liste des services moins couverts pour rester un partenaire agréable. Un plan soutenable doit nommer les pertes de couverture et les faire arbitrer, pas les cacher dans une hypothèse d’efficience.

## Erreurs à attaquer

- Coupe identique sur toutes les lignes malgré des conséquences différentes.
- Capacité supposée gratuite chez l’IT, le métier ou le juridique.
- Pilote transformé en service permanent sans budget récurrent.
- Présenter un palier budgétaire comme « sécurité complète ».
- Faire signer une exposition irréaliste pour transférer le blâme au prochain incident.

## Outil : plan de passage et registre des engagements

- **Plan réalisable et palier :** service rendu, limites et plancher applicable ; capacité additionnelle obtenue avec le palier, pas seulement produit supplémentaire.
- **Ressource productrice :** responsable, compétence, fenêtre et preuve d’engagement ; un chantier sans disponibilité confirmée reste conditionnel, pas engagé.
- **Chemin critique :** prérequis, tests, changement, double exploitation et retrait ; distinguer dépendance technique et simple préférence de planning.
- **Flux économiques :** date d’arrêt de facture, coûts de chevauchement, capacité réellement réaffectable ; aucun gain compté deux fois.
- **Renoncement :** tâche arrêtée ou reportée, bénéficiaire consulté, conséquence, données et preuves conservées ; vérification après coup de l’économie ou de la capacité promise.
- **Test de résistance :** perte de la compétence rare ou retard du prérequis ; option de maintien licite, réduction d’activité ou financement à faire arbitrer.
- **Inversion :** si le gain cible exige une transition que l’organisation ne peut pas absorber, changer la séquence, réduire le périmètre ou maintenir provisoirement ; ne pas sacrifier une contrainte non négociable pour conserver un budget inchangé.

## Matière à apporter par l’auteur

- Une économie qui a augmenté la charge cachée.
- **Question :** quel engagement faut-il cesser ou réduire si l’équipe n’obtient aucun moyen supplémentaire ?
- Une activité arrêtée sans dommage, malgré son statut historique d’indispensable.
- Un prestataire qui a réellement amélioré la capacité, et la contribution interne nécessaire.
- **Ironie possible :** « Le budget n’a pas bougé. Les obligations n’ont pas reçu le mémo. »

# 6 — Le CISO qui se protège avec le Gartner en haut à droite

## Nœud et frontière du chapitre

- **Question centrale :** comment utiliser une opinion de marché sans en faire un mandat d’achat ?
- **Point de départ :** une sélection défendable devant les achats peut rester mauvaise pour les équipes qui devront exploiter le produit.
- **Cible :** la délégation du jugement ; pas une accusation de classement acheté.

## Thèse, contre-thèse, position

- **Thèse :** visibilité de marché et adéquation à un besoin local sont deux questions différentes.
- **Contre-thèse :** pérennité, disponibilité du support, écosystème et couverture internationale peuvent peser plus lourd qu’une fonction techniquement supérieure.
- **Position :** utiliser la recherche pour qualifier le marché et les candidats ; décider sur des contraintes et des essais propres au besoin.
- **Cas où le leader est le bon choix :** exigences réellement couvertes, exploitation soutenable, capacité contractuelle adaptée ; ne pas choisir un outsider pour afficher son indépendance.
- **Appui :** la FAQ Gartner présente les Magic Quadrants comme un point de départ à combiner avec d’autres recherches, pas comme l’unique outil de sélection.[19]

## Les trois décalages à démonter

- **Marché ≠ tâche :** la catégorie évaluée peut regrouper des capacités dont l’équipe n’a pas besoin ; vérifier la définition exacte et l’édition du rapport utilisé.
- **Fournisseur ≠ offre achetée :** région, version, licence, connecteurs, support et calendrier précis.
- **Qualité nominale ≠ exploitation locale :** complexité, dépendances, charge de configuration, données disponibles et fonctionnement en panne.
- **Mécanisme de l’alibi :** un choix consensuel est plus facile à défendre après un problème ; cela ne le rend ni systématiquement mauvais ni automatiquement adapté.
- **Ne pas remplacer un raccourci par un autre :** pas d’affirmation générale sur les pondérations Gartner sans examiner le rapport concerné ; pas de causalité « gros fournisseur donc mauvais pour petite équipe ».

## Arbitrages techniques et contractuels

- **Critères éliminatoires :** une exigence indispensable non satisfaite ne doit pas être compensée par des points d’ergonomie.
- **Comparaison pondérée :** utile seulement entre options admissibles, avec poids justifiés et sensibilité aux changements d’hypothèses.
- **Suite ou spécialistes :** intégration et compétences contre dépendances et interfaces ; vérifier le service dégradé, pas seulement le nombre de consoles.
- **Fonction annoncée :** distinguer disponible, essayée, contractuellement engagée et simple intention ; ne pas financer le bénéfice immédiat d’une fonction absente.
- **Sortie :** export exploitable, formats, historique, règles, délais, frais, assistance, accès et traitement des données ; un fichier téléchargé n’est pas une migration démontrée.
- **Support :** tester l’escalade et examiner les conditions ; un essai court ne prouve ni la santé financière ni la fiabilité annuelle du fournisseur.

## Décision senior : le favori peut-il réellement perdre ?

- **Dilemme :** retenir une offre supérieure mais difficile à quitter, ou une offre moins complète dont l’équipe maîtrise les interfaces. Le support et l’écosystème du leader peuvent valoir plus qu’une indépendance impossible à exploiter.
- **Rapport de force :** accord-cadre, remises liées à une suite, région imposée, délais d’achat ou intégrations existantes ; faire qualifier les contraintes déjà engagées et celles encore négociables.
- **Deux exercices distincts :** sélection réellement ouverte ; sécurisation d’un choix contraint. Ne pas fabriquer les notes du premier pour justifier le second, ni contourner les règles d’achat applicables.
- **Après la signature :** qui maîtrise les changements de version, les coûts variables, le support et le rythme de migration ? Un droit contractuel de sortie, un export technique et une capacité réelle à partir sont trois états différents.
- **Fournisseur qui refuse :** une clause ou un protocole idéal ne crée pas de pouvoir de négociation. Examiner périmètre réduit, compensation recevable, autre architecture, alternative exploitable ou escalade ; ne pas faire disparaître l’exigence du dossier.
- **Préserver un futur choix :** données réutilisables, interfaces, moyens d’administration de reprise et compétence interne ; cibler les leviers utiles plutôt que promettre une indépendance totale.
- **Le piège du CISO :** annoncer une mise en concurrence dont aucun résultat ne peut écarter le favori. Le dossier défend alors la procédure, pas la qualité de la décision.

## Erreurs à attaquer

- Copier le coin supérieur droit avant d’écrire le besoin.
- Donner la même note à « non testé » et à « conforme ».
- Laisser le fournisseur sélectionner seul les données et les cas d’essai.
- Considérer les heures d’ingénieur commercial comme le futur coût d’exploitation.
- Réutiliser un graphique sous licence sans vérifier les droits ; citer l’analyse pertinente plutôt que reproduire automatiquement l’image.

## Outil : carte du pouvoir d’achat et dépendance consentie

- **Besoin et admissibilité :** capacité indispensable, exigences éliminatoires et marges négociables ; les préférences ne compensent pas une condition indispensable.
- **Pouvoir réel :** ce qui est signé, qui peut refuser, coût de sortie de la négociation et alternatives opérables ; distinguer contrainte imposée et choix encore ouvert.
- **Preuve :** protocole comparable, interventions fournisseur consignées, contraintes et limites non testées ; conserver le droit de conclure à une inadéquation.
- **Concessions :** dépendance et limites acceptées par autorité habilitée, bénéfice obtenu en échange, mesures préservées ; pas de renoncement implicite aux obligations.
- **Trois sorties :** droit contractuel, portabilité technique et capacité opérationnelle ; démontrer au moins le chemin de sortie du composant indispensable, sans promettre que tout est migrable.
- **Levier après achat :** évolution de tarif, support, traitement des données ou fonction indispensable ; événement de renégociation et solution transitoire réalisable.
- **Inversion :** si le favori échoue à une condition indispensable, écarter ou faire réviser explicitement le besoin par l’autorité compétente ; si le choix est contraint, publier ses limites plutôt que lui fabriquer la meilleure note.

## Matière à apporter par l’auteur

- Une sélection où le leader a gagné pour de bonnes raisons.
- **Question :** quel échec à l’essai ferait réellement éliminer le fournisseur favori ?
- Une fonction inutile qui avait pesé lourd dans la grille.
- Une promesse qui a survécu à la vente mais pas au contrat.
- **Ironie possible :** « Nous avons acheté le leader. Il cherche encore le connecteur. »

# 7 — Le CISO qui décide de tout et de rien

## Nœud et frontière du chapitre

- **Question centrale :** qui a le droit de décider, dans quel délai, avec quel recours ?
- **Point de départ :** la mention « validé par la sécurité » recouvre recommandation technique, autorisation de changement et acceptation d’un risque métier ; personne ne parle du même acte.
- **Différence avec le chapitre 1 :** ici, rendre les décisions exécutables au quotidien et pendant une crise.

## Thèse, contre-thèse, position

- **Thèse :** centraliser toute validation autour du CISO peut créer un goulot et diluer la responsabilité métier.
- **Contre-thèse :** des droits de veto, des règles centrales et une autorité de crise peuvent être indispensables ; décentraliser n’est pas automatiquement responsabiliser.
- **Position :** délégation bornée pour les décisions maîtrisées ; escalade explicite pour les effets irréversibles, les obligations et les interdépendances importantes.
- **Quand centraliser :** arbitrage entre services, incident transverse, risque hors délégation, absence de compétence locale ou décision de sécurité physique selon l’organisation compétente.
- **Quand déléguer :** opération répétable, conséquences connues, limites claires, traces et mécanisme de recours.

## Distinguer les décisions avant les rôles

- **Avis :** dire si une option satisfait les exigences et expliciter les réserves.
- **Autorisation :** permettre une action dans un périmètre précis.
- **Acceptation du risque :** décider d’une exposition résiduelle dans une délégation valide ; ne dispense pas des obligations applicables.
- **Exécution :** réaliser et vérifier l’action ; ne prouve pas que l’autorisation existait.
- **Assurance :** vérifier que le dispositif fonctionne ; garder une capacité de contradiction distincte du déclarant lorsque possible.
- **Ancrage :** l’article 20 de NIS 2 vise les organes de direction ; il ne permet pas de remplacer l’analyse des responsabilités réelles par « le RSSI a signé ».[14]

## Mécanismes et contradictions

- **Double signature :** peut sécuriser une action sensible ; peut aussi organiser une attente illimitée si aucun suppléant ou délai n’est prévu.
- **Exception permanente :** lancement temporaire devenu architecture ; risque accepté une fois, contexte changé plusieurs fois.
- **Droit d’alerte sans accès au décideur :** responsabilité affichée sans moyen d’exercer le mandat.
- **Indépendance :** contester une décision exige un canal d’escalade protégé, pas une obligation de bloquer chaque demande.
- **Identités non humaines :** comptes techniques, applications OAuth, secrets CI/CD et agents portent aussi des pouvoirs ; les limiter à une procédure de départ RH laisse une partie du problème hors champ.

## Arbitrage technique à développer : interrompre, contenir, reprendre

- **Confinement :** distinguer suspension d’un compte, révocation d’un jeton, fin de session et annulation de travaux ; effet à vérifier sur le système cible.
- **Arrêt métier :** conséquences sur clients, opérations, sécurité physique et engagements ; décision selon l’autorité prévue, pas déduite d’une alerte seule.
- **Reprise :** conditions propres ; une sauvegarde accessible ne démontre ni intégrité ni absence de persistance.
- **Dépendance critique :** si le plan d’identité est compromis, prévoir un chemin d’administration de reprise dont la confiance et l’indépendance ont été vérifiées ; restaurer sous les mêmes pouvoirs compromis peut réintroduire le problème.
- **Notifications :** la décision d’envoyer une information à une autorité suit sa procédure et son délai ; ne pas la confondre avec validation de la communication commerciale.

## Décision senior : quand le CISO perd l’arbitrage

- **Dilemme :** contenir un service suspect lorsque l’exploitation estime l’arrêt dangereux. Ni coupure réflexe ni effacement de l’avis sécurité ; comparer conséquences, moyens de confinement partiel et pouvoirs réellement disponibles.
- **Désaccord sur les faits :** nommer l’observation discriminante, qui peut la produire et ce qui est autorisé pendant l’investigation. Une réunion supplémentaire ne remplace pas cette observation.
- **Désaccord sur l’exposition :** dans la tolérance et les délégations valides, le décideur tranche ; conserver l’avis contradictoire puis exécuter sans sabotage ni maquillage. Au-delà, escalader vers l’autorité compétente : la signature du métier ne suffit pas.
- **Désaccord sur le pouvoir :** expliciter la portée du veto, sa base, sa durée et la voie de recours. Une obligation légale ou un enjeu de sécurité des personnes appelle les fonctions compétentes ; toute incertitude ne donne pas au CISO un pouvoir d’arrêt personnel.
- **Décideur qui ne décide pas :** constater ce qui continue par défaut, les mesures conservatoires préautorisées et l’échelon de secours ; fixer un délai lié aux conséquences, pas seulement au prochain comité.
- **Exceptions cumulées :** plusieurs dérogations admissibles séparément peuvent former un chemin d’accès transversal durable ; revoir leur combinaison et leurs hypothèses, pas uniquement leurs dates d’échéance.
- **Mandat contingent :** dans une petite équipe, une personne peut cumuler des rôles, mais les actes restent distingués ; dans une organisation distribuée, privilégier des délégations vérifiables. La criticité physique peut imposer une autre chaîne d’autorité que celle du SOC.
- **Le piège du CISO :** défendre son indépendance en rouvrant sans fait nouveau une décision légitime qu’il a perdue ; ou conserver toute signature pour rendre sa fonction indispensable.

## Erreurs à attaquer

- RACI sans décision, délai ni remplaçant.
- Donner une autonomie puis sanctionner toute initiative conforme à la délégation.
- Maintenir une exception sans revoir ses hypothèses après un changement majeur.
- Faire du CISO le responsable implicite de toute perte économique.
- Supprimer un contrôle central avant que l’équipe locale ait les moyens d’assumer la délégation.

## Outil : protocole d’autorité et relevé de désaccord

- **Décision et bornes :** objet, systèmes, conséquences, durée, limites, initiateur, expert, décideur, exécutant et suppléant.
- **Nature du désaccord :** faits, exposition ou pouvoirs ; avis conservés, hypothèse déterminante et observation susceptible de la renverser.
- **Escalade :** niveau habilité à trancher, délai lié à la conséquence et recours ; exposition hors délégation jamais réputée acceptée par simple information.
- **En attendant :** action conservatoire autorisée ou escalade de secours, avec ses effets ; aucun silence valant accord universel.
- **Après arbitrage :** exécution de la décision valide, mesures conservées, faits déclencheurs de réouverture et suivi du risque résiduel ; pas de fausse unanimité dans le compte rendu.
- **Preuve :** exercice avec décideur absent, désaccord métier/sécurité et canal principal indisponible ; vérifier qu’une action autorisée est possible sans supposer une chaîne parfaite.
- **Inversion :** faire élargir explicitement la délégation par l’autorité compétente si l’attente crée le risque, dans les limites du droit applicable et des exigences de sécurité ; l’urgence ne crée pas ce pouvoir. Renforcer le contrôle si les exceptions ou leur combinaison dépassent les limites approuvées.

## Matière à apporter par l’auteur

- Un veto justifié et un veto de confort : mécanismes différents, même mot.
- **Question :** quelle décision doit rester centralisée, et laquelle pourrait être déléguée sans augmenter l’exposition au-delà des limites approuvées ?
- Une décision de crise ralentie par une procédure censée la sécuriser.
- Un pouvoir que le CISO doit conserver, et un autre qu’il doit cesser d’accaparer.
- **Ironie possible :** « Tout est sous contrôle. Tout attend aussi sa signature. »

# Conclusion — Construire la roadmap sans inventer les moyens

## Synthèse : sept décisions différentes

- **Board :** faire arbitrer des options comparables.
- **Standards :** qualifier les obligations et les preuves.
- **Investissements :** décider à nouveau des coûts futurs.
- **Veille :** choisir l’expérience ou l’action pertinente.
- **Budget :** limiter les engagements à la capacité disponible.
- **Fournisseurs :** vérifier l’adéquation et les engagements.
- **Gouvernance :** attribuer le pouvoir d’agir et le recours.

## Architecture de la roadmap

- **Entrées à qualifier avant arbitrage :** obligations applicables et échéances, sécurité des personnes et des installations, contraintes contractuelles.
  - Ne pas confondre obligation légale, clause déjà engagée et demande commerciale encore négociable. Une clause peut parfois être renégociée avec la contrepartie ; elle ne devient pas facultative par décision unilatérale du CISO.
  - Plancher de l’arbitrage : droit effectivement applicable, sécurité des personnes/installations et contraintes contractuelles établies comme non négociables pour cette décision ; les autres clauses restent à négocier ou à traiter explicitement.
- **Entrées de risque :** services critiques, scénarios de pertes, expositions observées, dépendances et incertitudes.
- **Entrées de capacité :** exploitation récurrente, compétences rares, changement et réserve d’incident.
- **Sorties :** chantiers retenus, prérequis, essais, extensions, reports et arrêts.
- **Pas de score unique magique :** un interdit juridique ou une dépendance bloquante ne se compense pas avec des points de bénéfice.

## Exemple de raisonnement conditionnel : quatre chantiers possibles

- **Lecture :** A, B, C et D sont des repères, pas un ordre automatique ; seules les dépendances explicites imposent une séquence.
- **Situation à examiner, sans budget ni résultat présupposé :** accès puissants mal bornés ; reprise métier non démontrée ; alertes sans action assurée ; nouveau cas d’usage IA demandé.
- **Chantier A — Réduire les pouvoirs exposés.**
  - Choisir si accès humains ou non humains ouvrent un chemin plausible vers un service critique.
  - Premier résultat : périmètre connu, pouvoirs nécessaires distingués des pouvoirs hérités, révocation vérifiée.
  - Report possible d’une extension générale de la plateforme d’identité ; commencer par les pouvoirs à conséquence forte.
- **Chantier B — Démontrer une reprise exploitable.**
  - Choisir si la continuité dépend d’hypothèses non éprouvées.
  - Dépendance : chemin d’administration de confiance, secrets et accès de reprise ; vérifier indépendance des sauvegardes et des permissions qui pourraient les détruire.
  - Séquence : préparer ce chemin avec A lorsque nécessaire ; restaurer et valider ensuite une transaction métier, ses données et ses dépendances.
  - Une sauvegarde techniquement restaurée n’est pas le résultat final.
- **Chantier C — Relier une détection à une action.**
  - Choisir si le scénario prioritaire produit des alertes que personne ne peut traiter ou exploiter.
  - Dépendances : données minimales, intervenant, autorité et accès ; corriger ces points avant un achat d’automatisation.
  - Mettre en place en parallèle les mesures urgentes réalisables ; ne pas laisser une exposition active attendre l’achèvement d’A ou B.
- **Chantier D — Tester l’innovation sur une tâche bornée.**
  - Choisir seulement si un besoin existe et si l’essai ne détourne pas une compétence indispensable aux autres engagements.
  - Dépendances : données autorisées, droits maîtrisés, référence de comparaison et capacité de supervision.
  - Sinon : rester en exploration ou différer ; un portefeuille à trois chantiers peut être meilleur qu’un quatrième ajouté pour avoir une case IA.
- **Ce qui peut changer l’ordre :** exploitation active, obligation datée, indisponibilité d’une dépendance critique, résultat d’essai invalidant une hypothèse.
- **Ce qui ne suffit pas :** remise de fin de trimestre, annonce d’un concurrent, nombre de logos sur une slide.

## Portes de décision sur douze mois, sans calendrier artificiel

- **Douze mois :** horizon de pilotage, pas promesse de livraison de tous les chantiers dans ce délai.
- **Qualification :** périmètre, propriétaires et dépendances confirmés ; chantier non lancé si personne ne peut l’exploiter.
- **Preuve initiale :** contrôle ou essai sur périmètre borné ; investissement suivant lié à un résultat observable.
- **Extension :** vérifier que l’élargissement ne change pas les hypothèses de volume, de droits ou de compétence.
- **Maintien :** exploitation et budget récurrent attribués ; détecter les changements qui invalident la preuve initiale.
- **Sortie :** supprimer ce qui a été remplacé, terminer la double exploitation, fermer les accès et conserver ce qui doit l’être.
- **Dates :** les fixer après estimation par les équipes concernées et examen des échéances imposées ; ne pas déduire l’effort de la place disponible dans un trimestre.

## Arbitrage de trajectoire : une option retenue, une option rejetée

- **Conditions du raisonnement :** une même équipe doit préparer une reprise de confiance et migrer une plateforme de sécurité ; la migration promet une économie à terme, mais exige une double exploitation et le transfert de contrôles existants. Il s’agit de critères de décision à confronter au terrain, pas d’un résultat d’entreprise rapporté.
- **Trajectoire à retenir si le maintien reste admissible :**
  - Maintenir le périmètre nécessaire de l’existant pendant une période contractuellement et opérationnellement maîtrisée.
  - D’abord démontrer le chemin d’administration et la reprise du service critique ; préserver cette capacité pendant la migration.
  - Ensuite transférer les contrôles et données indispensables sur un périmètre borné ; décommissionner l’ancien seulement après preuve de remplacement et traitement des obligations de conservation.
  - **Prix du choix :** économie retardée et coûts de chevauchement ; les accepter explicitement, sans les cacher dans le budget cible.
- **Trajectoire rejetée sous ces conditions :** migrer partout pour obtenir l’économie affichée avant de rendre la reprise indépendante ; la même équipe devient le goulot de deux changements et la capacité de retour n’est pas démontrée.
- **Ce qui renverse le choix :** maintenir l’existant devient inadmissible, une contrainte de calendrier s’impose, ou une capacité distincte de migration peut être réellement obtenue ; reprendre l’arbitrage au lieu de réciter « reprise d’abord ».
- **Si aucune trajectoire ne tient :** présenter financement, réduction licite d’activité ou autre mesure conservatoire à l’autorité compétente. Ne pas remettre les deux projets en vert en supposant que les personnes absorberont le conflit.
- **Décision d’arrêt :** si l’équipe ne peut pas produire le résultat de transfert défini, suspendre l’extension selon les règles approuvées ; ne pas supprimer l’ancien contrôle pour faire apparaître l’économie.

## Résistance du programme aux faits contrariants

- **Perte d’une dépendance commune :** quels investissements et services échouent simultanément ? Quel moyen d’administration, d’alerte et de reprise reste utilisable ?
- **Absence de la compétence rare :** quelle tâche doit attendre, quel service reste tenu, quel engagement n’est plus soutenable ? Ne pas compter des personnes non formées comme des remplaçants immédiats.
- **Prérequis en retard :** quelles actions conservatoires peuvent avancer, quelle extension est interdite et qui arbitre le risque de l’attente ?
- **Moyens de transition retirés :** distinguer économies finales annoncées et coûts pour y parvenir ; remettre la cible en discussion si son chemin n’est plus financé.
- **Preuve invalidée :** quel changement impose un retest ou un retour à un périmètre restreint ? Un contrôle installé n’a pas forcément perdu son efficacité, mais l’assurance utilisée pour décider doit être réexaminée.
- **Aucun résultat nouveau ne peut changer le choix :** arrêter l’étude et demander la décision ; continuer à tester ne doit pas servir à éviter un désaccord de pouvoir ou de valeur.
- **Bilan de portefeuille :** après chaque arrêt ou consolidation, regarder à nouveau les dépendances communes et les exceptions cumulées ; une liste plus courte de projets ne prouve pas une exposition moindre.

## Dernière fiche pour l’auteur

- **Décision :** qu’est-ce qui change concrètement après ce chapitre ?
- **Opposition :** quel interlocuteur compétent pourrait refuser la recommandation, et pourquoi ?
- **Preuve :** quel fait pourrait donner raison à cet interlocuteur ?
- **Renoncement :** quel travail ou quelle capacité est déplacé ?
- **Limite :** où la recommandation cesse-t-elle d’être raisonnable ?
- **Fin possible à écrire :** une sécurité qui sait expliquer ses choix, observer leurs limites et les réviser ; pas un CISO qui finit toujours par gagner la réunion.

# Annexe juridique

- **Objet :** détail maintenable des repères de champ et de notification ; les distinctions juridiques restent nécessaires, mais ne constituent pas le cœur argumentatif du chapitre 2.

- **Champ avant délais :** qualifier l’entité et ses services, les secteurs/annexes concernés, les seuils et exceptions ou désignations pertinentes, le statut essentiel/important, les États membres concernés, les textes nationaux en vigueur et l’autorité compétente.[14]
  - Règle de travail proposée : le registre conclut pour chaque entité, pas pour le groupe par intuition.
  - Les articles de la directive définissent l’architecture à mettre en œuvre par les États ; leur seule lecture ne suffit pas à établir une obligation opposable à une entreprise française. Les délais ci-dessous décrivent cette architecture, à relier au régime effectivement applicable avant de les utiliser comme échéances de l’entreprise.
- **NIS 2, directive 2022/2555 :**
  - Article 20 : gouvernance des organes de direction ; article 21 : mesures techniques, opérationnelles et organisationnelles appropriées et proportionnées ; article 23 : notification des incidents importants.[14]
  - Architecture générale de l’article 23 : alerte précoce sans retard injustifié, au plus tard 24 heures après prise de connaissance de l’incident important ; notification d’incident sans retard injustifié et, en tout état de cause, au plus tard 72 heures après cette prise de connaissance (plafond, pas délai d’attente autorisé) ; rapport final au plus tard un mois après la notification d’incident, distincte de l’alerte précoce.[14]
  - Compléments à garder avec les délais : rapport d’avancement puis rapport final si l’incident est toujours en cours ; rapports intermédiaires sur demande.[14]
  - Régime particulier des prestataires de services de confiance : pour les incidents importants affectant leurs services de confiance, la notification visée à l’article 23, paragraphe 4, point b, intervient sans retard injustifié et au plus tard en 24 heures après prise de connaissance, au lieu du délai général de 72 heures.[14]
  - Conséquence opérationnelle : préparer la qualification et l’envoi avant l’incident ; ne pas assimiler « toute alerte » à « incident important », ni attendre une certitude exhaustive pour enclencher la procédure.
- **Règlement d’exécution 2024/2690 :** exigences techniques et méthodologiques et précisions sur les incidents importants pour les catégories d’entités énumérées à son article 1 ; pas un référentiel universel pour toutes les entreprises.[15]
  - Catégories à vérifier : DNS, registres TLD, cloud, centres de données, CDN, services gérés, services de sécurité gérés, places de marché, moteurs de recherche, plateformes de réseaux sociaux et services de confiance.[15]
  - Ne pas présenter ce règlement comme supprimant tous les autres textes, obligations nationales ou régimes applicables.
- **Guide ENISA associé :** la page de présentation de l’ENISA précise qu’il est non juridiquement contraignant et ne remplace pas les cadres nationaux ; cette attribution porte sur la présentation consultée, pas sur une analyse exhaustive du guide.[3]
- **France :** pas de verdict global sur l’état de transposition déduit d’un portail ; relever les textes français effectivement en vigueur et leur champ avant toute affirmation d’opposabilité.
- **Autres branches du registre à qualifier selon l’activité :** RGPD, DORA, Cyber Resilience Act, obligations sectorielles et contrats. Liste de questions d’applicabilité, pas déclaration que tous s’appliquent ni qu’ils se cumulent intégralement.
  - Pour chaque ligne : nature du texte (directive, règlement, texte national, guide ou contrat), champ, articulation, date d’application et autorité ; ne pas copier la logique de transposition d’une directive sur un règlement.


# Repères documentaires — portée des preuves

- **ENISA, page d’actualité présentant le panorama 2026, 22 septembre 2026 :** événements observés en 2025 ; sert au cadrage des menaces et dépendances, pas à une probabilité d’entreprise ; le rapport intégral n’est pas la pièce citée ici.[1]
- **ENISA, annonce du guide NIS 2, 26 juin 2025 :** indique le statut non contraignant du guide ; ne permet pas d’établir l’opposabilité de la directive en droit français.[3]
- **The Guardian, 21 mai 2025 :** rapporte une estimation annoncée par M&S à cette date ; source de presse, pas coût final audité ni preuve d’efficacité d’un produit.[7]
- **CISA, 27 mai 2025 :** présentation de guides SIEM/SOAR et priorisation des journaux ; recommandation opérationnelle, pas mesure de rendement.[10]
- **Anthropic, 11 septembre 2025 et 9 janvier 2026 :** méthodes d’évaluation et résultat vérifiable ; sources d’un concepteur de modèles, sans validation indépendante de performance locale.[11][13]
- **Directive 2022/2555, texte du Journal officiel du 27 décembre 2022 :** champ et architecture de gouvernance/mesures/notification, notamment articles 2, 3, 20, 21 et 23 ; ne suffit pas à établir le régime national applicable à une entité.[14]
- **Règlement d’exécution 2024/2690 du 17 octobre 2024 :** champ, exigences et qualification d’incidents pour les catégories concernées ; pas un substitut à toute l’analyse juridique.[15]
- **CISA, 8 juillet 2024 :** fondation plus ancienne sur la diligence relative aux projets libres ; pas une comparaison de coût total des offres actuelles.[17]
- **FAQ Gartner, copie archivée du 22 octobre 2026 :** position déclarée sur l’usage des Magic Quadrants comme point de départ ; pas audit indépendant de la méthode ni examen d’un quadrant sectoriel particulier.[19]
- **Traçabilité :** sources initiales consultées le 20 novembre 2026 ; textes EUR-Lex directement relus lors de cette refonte. Les dates de publication ci-dessus ne sont pas des dates d’effet juridique déduites.

## Sources

[1] https://enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience — ENISA — Threat Landscape 2026 : dépendances et résilience
[3] https://www.enisa.europa.eu/news/supporting-nis2-implementation-through-actionable-guidance
[7] https://www.theguardian.com/business/2025/may/21/cyber-attack-cost-marks-and-spencer-lost-sales-company-results-reveal
[10] https://www.cisa.gov/news-events/alerts/2025/05/27/new-guidance-siem-and-soar-implementation — CISA — Recommandations SIEM et SOAR, 27 mai 2025
[11] https://www.anthropic.com/research/writing-tools-for-agents — Anthropic — Concevoir des outils pour les agents, 11 septembre 2025
[13] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — Anthropic — Demystifying evals for AI agents — 9 janvier 2026
[14] https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng?uri=CELEX%3A32022L2555 — Directive (UE) 2022/2555 — articles 20, 21 et 23 — texte du JO
[15] https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj/eng — Règlement d’exécution (UE) 2024/2690 — champ et exigences
[17] https://www.cisa.gov/news-events/news/continued-progress-towards-secure-open-source-ecosystem — CISA — Progrès vers un écosystème libre sécurisé, 8 juillet 2024 (fondation)
[19] https://web.archive.org/web/20261022073220/https://www.gartner.com/en/about/magic-quadrant-faq — Gartner — FAQ Magic Quadrant, archive du 22 octobre 2026
