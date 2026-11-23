# La sécurité n’est pas un concours de slides

Base auteur développée. Trois axes par chapitre ; les sous-points donnent de la matière à écrire, pas une prose à recopier. Les cas publics sont sourcés ; les choix et les formules proposés sont des angles éditoriaux, pas des conclusions des sources. Détail des preuves et limites : [registre de sources](research/developpement-sources.md) et [lecture critique de BRKSEC-1785](research/brksec-1785.md). Les références Cisco utilisent les pages physiques du PDF, pas une numérotation de slides supposée.

## Introduction — Acheter moins de certitudes

Menace, obligation et offre commerciale ne sont pas synonymes. Partir de cette confusion : une menace justifie une analyse, une obligation impose de qualifier son champ, une offre doit encore prouver son utilité. Le CISO ne promet pas l’immunité ; il rend les choix possibles, y compris ceux qui déplaisent à la sécurité.

## 1 — Board : obtenir une décision, pas une bonne note

- **Présenter un choix, pas un catalogue.**
  - Développer le passage du produit au service : non pas « acheter une sauvegarde », mais pouvoir rouvrir l’activité avec ses données, ses accès et ses applications. Comparer les pertes plausibles et les moyens requis, sans déguiser une hypothèse en prévision.
  - Ici, raconter la British Library après l’attaque d’octobre 2023 : des copies des collections numériques existaient, mais l’infrastructure viable pour les restaurer manquait. Le rapport du 8 mars 2024 distingue clairement conservation des données et retour du service.[1](research/developpement-sources.md#source-1)
  - Faire apparaître le choix : financer la chaîne de reprise plutôt qu’un stockage supplémentaire si le blocage est applicatif. Formule possible : « Le board n’achète pas des copies. Il achète une chance de rouvrir. »
- **Attendre a aussi un prix.**
  - Une étude peut éviter une mauvaise décision ; elle peut aussi consommer le créneau de migration ou prolonger une exposition. Décrire les deux coûts, au lieu d’opposer courage et prudence.
  - Ici, développer l’information décisive : si un test de restauration peut changer l’ordre des investissements, le financer ; si son résultat arrivera après l’échéance de choix, décider avec l’incertitude explicitée.
  - Le report doit avoir une condition de sortie observable. « Nous attendons » n’est pas une stratégie si personne ne sait quel résultat permettra de cesser d’attendre.
- **Un budget refusé laisse une exposition.**
  - Distinguer refus de dépense et acceptation du risque : le premier ne désigne ni le décideur habilité pour le second, ni les services qu’il accepte de dégrader.
  - Développer la contre-proposition : préserver la reprise, différer une extension, réduire le périmètre couvert. Nommer ce que chaque option laisse sans protection supplémentaire et qui doit l’arbitrer.
  - Ne pas transformer le désaccord en menace. Si l’exposition dépasse les délégations ou l’appétence, la remonter ; sinon, exécuter le choix valide sans continuer à vendre l’option refusée.

## 2 — Standards : prouver utile, pas produire plus

- **Tout référentiel n’est pas une obligation.**
  - Avant de chiffrer un programme, séparer exigence légale, engagement contractuel, certification recherchée et guide volontaire. Une même recommandation peut devenir contractuellement importante sans devenir, pour autant, une loi universelle.
  - Ici, utiliser un contraste vérifiable : dans sa publication du 26 juin 2025, l’ENISA précise que son guide d’implémentation NIS2 n’est pas juridiquement contraignant et invite les entreprises concernées à consulter leurs autorités nationales.[3](research/developpement-sources.md#source-3)
  - Angle à développer : qualifier le texte, l’entité et le périmètre avec le juridique avant d’acheter la conformité. Le guide peut être excellent ; ce n’est pas une raison pour lui attribuer une force qu’il ne revendique pas.
- **Mutualiser les preuves, pas inventer leur équivalence.**
  - Partir d’un rapport de revue des accès : il peut servir plusieurs demandes si les comptes, la période et les contrôles observés correspondent. Un fichier commun réduit les copies ; il ne résout pas un écart de périmètre.
  - Ici, développer la différence entre « la procédure existe » et « les droits ont effectivement été retirés ». Le même document ne prouve pas automatiquement la conception du contrôle et son fonctionnement.
  - Le choix utile : compléter seulement la preuve manquante plutôt que refaire tout l’audit. Accepter toutefois une collecte distincte lorsque l’exigence, la population ou l’indépendance du contrôle diffère réellement.
- **Une preuve récente peut déjà être caduque.**
  - Expliquer le mécanisme : une migration d’identité peut invalider une revue des privilèges ; une nouvelle dépendance peut invalider un test de reprise pourtant récent. C’est la conclusion qui vieillit, pas seulement le fichier.
  - Ici, construire le passage autour du changement intervenu depuis le test, puis du contrôle ciblé qui permet de retrouver confiance. Ne pas réclamer une campagne entière pour chaque modification mineure.
  - Formule possible : « Une capture datée d’hier peut raconter le système d’avant-hier. » La preuve utile permet de décider aujourd’hui, pas seulement de fermer une demande documentaire.

## 3 — Investissements : sauver la capacité, pas l’achat

- **La facture ne prouve pas la protection.**
  - Suivre une capacité jusqu’à son usage : les journaux arrivent-ils, l’alerte est-elle comprise, quelqu’un peut-il agir ? Une licence activée n’efface ni un connecteur cassé ni une réponse sans responsable.
  - Ici, partir du retrait recommandé par Cisco pour ce qui ne peut plus être corrigé, supporté ou mis à niveau : inventaire, exposition Internet d’abord, puis priorités métier, avec précautions pour infrastructures critiques et OT.[Cisco, p. 14–17](research/brksec-1785.md#maintenabilite) Angle auteur : acheter la capacité de rester maintenable, pas seulement une nouvelle boîte.
  - Contradiction : retirer brutalement un équipement industriel peut dégrader le service qu’il protège. Développer le maintien borné avec isolement éprouvé et sortie préparée ; l’impossibilité de contenir l’exposition peut rendre le remplacement prioritaire.
- **Sortir peut coûter plus que rester.**
  - Comparer les dépenses et les risques futurs : reprise des règles, export de l’historique, formation, exploitation en parallèle et contrôles temporairement moins efficaces. L’argent déjà dépensé n’est pas un argument pour renouveler.
  - Ici, développer le maintien temporaire assumé : rester peut être rationnel si une sortie précipitée casse la détection. Mais préciser ce qui rendra la sortie praticable, faute de quoi le temporaire devient une rente.
  - Faire changer la recommandation si le fournisseur ne peut plus satisfaire une exigence indispensable. Une transition coûteuse peut alors être nécessaire, même sans économie promise.
- **Plusieurs fournisseurs peuvent tomber ensemble.**
  - Compter les dépendances plutôt que les logos : identité, hébergement, réseau, administration. Deux contrats ne créent pas deux chemins de secours si le même service est nécessaire pour les utiliser.
  - Ici, raconter la panne Cloudflare des 2–4 novembre 2023 : malgré un plan de contrôle et une analytique répartis sur trois centres, des dépendances non évidentes ont rendu certains systèmes critiques indisponibles. Les services réseau et de sécurité continuaient ; le plan de contrôle et l’analytique étaient touchés. Ce cas concerne un seul fournisseur, pas une panne multi-fournisseurs : il illustre le mécanisme de dépendance, que l’on propose ensuite de rechercher entre contrats.[2](research/developpement-sources.md#source-2)
  - Confronter ce cas au schéma Cisco : des points d’application distribués partagent un plan de contrôle.[Cisco, p. 26](research/brksec-1785.md#dependances) Angle de test proposé, pas panne démontrée : sans ce plan, quelles règles restent appliquées, lesquelles peuvent encore changer ? Consolider si le gain d’exploitation justifie cette dépendance, pas parce que les icônes sont dispersées.

## 4 — Veille : apprendre quelque chose ou arrêter

- **Une alerte urgente n’est pas un sujet d’innovation.**
  - Traiter l’exposition sans attendre un achat d’innovation. Cisco présente Live Protect comme une protection temporaire ciblée, pas un correctif.[Cisco, p. 34–37](research/brksec-1785.md#contenir) Angle auteur : contenir peut acheter du temps si le chemin couvert est vérifié et la correction reste la sortie ; sans couverture démontrée, réarbitrer l’urgence avec l’autorité habilitée.
  - Ici, placer un chiffre précisément borné : le DBIR 2025 situe l’exploitation de vulnérabilités à 20 % des violations de données analysées. Le corpus comprend 22 052 incidents, dont 12 195 violations de données confirmées ; la période de collecte des incidents est du 1er novembre 2023 au 31 octobre 2024.[5](research/developpement-sources.md#source-5)
  - Ne pas convertir ce chiffre en probabilité locale. S’en servir pour ouvrir la question « sommes-nous exposés ? », puis revenir aux actifs et protections réels. Une tendance ne remplace pas un diagnostic.
- **Un pilote doit pouvoir perdre.**
  - Définir le résultat qui rendrait préférable l’existant ou une option plus simple. Pour une aide à l’analyse d’alertes, comparer la qualité de la décision finale, pas seulement la vitesse de rédaction du résumé.
  - Ici, reprendre l’ambition de constats vérifiables de Foundry, présentée par Cisco, sans reprendre sa promesse d’efficacité.[Cisco, p. 49–51](research/brksec-1785.md#pilote) Essai proposé : pour détecter des vulnérabilités, demander une preuve reproductible sur le périmètre autorisé, puis compter relectures et faux positifs. Plus de découvertes annoncées peut signifier plus de travail, pas plus de protection.
  - Préserver la contradiction : une solution moins rapide peut rester préférable si elle réduit une erreur grave. Décider de cette priorité avant de voir les résultats, pas pour sauver le favori après coup.
- **Une démo réussie ne finance pas l’exploitation.**
  - Retirer progressivement l’assistance temporaire du fournisseur : qui maintient les connecteurs, traite les incidents et adapte les règles ? L’essai doit révéler le travail qui reviendra à l’équipe.
  - Ici, développer un essai d’automatisation d’abord sans action irréversible : observer les propositions, puis n’autoriser que les actions bornées. Arrêter l’assistant ne garantit pas l’annulation d’une action déjà transmise.
  - Accepter de ne pas industrialiser une réussite technique si personne ne peut l’exploiter. « Cela marche » et « nous pouvons le faire fonctionner » sont deux conclusions différentes.

## 5 — Budget : financer le passage, pas seulement la cible

- **Une économie future ne paie pas la transition.**
  - Montrer les dépenses qui se superposent : ancien contrat, nouvelle plateforme, migration des données, formation et retour arrière. Présenter le moment où l’ancien coût disparaît, pas seulement la facture cible.
  - Ici, partir de la cadence de versions durcies annoncée par Cisco, qui prévoit aussi des corrections hors cycle.[Cisco, p. 40–43](research/brksec-1785.md#cadence) Angle auteur : financer les heures récurrentes de test, bascule et retour arrière, pas seulement la migration initiale. Une cadence fournisseur ne réserve pas la capacité de l’équipe ; préserver aussi une voie urgente.
  - Arbitrage proposé : réduire la première vague pour conserver une reprise praticable, quitte à retarder l’économie. Inverser ce choix si le maintien devient inadmissible ou si une capacité de transition distincte est réellement disponible.
- **Moins de licences ne signifie pas moins de travail.**
  - Distinguer trois résultats : une dépense supprimée, une tâche supprimée et du temps réaffectable. Ils ne coïncident pas si les contrats continuent ou si le travail revient sous forme de maintenance interne.
  - Ici, développer le cas de l’automatisation sans inventer de gains : décrire la tâche retirée, puis la validation, les exceptions et l’entretien ajoutés. La preuve attendue est le travail net que l’équipe peut effectivement cesser.
  - Contrepoint : une petite réduction de charge peut être précieuse sans permettre de supprimer un poste. La présenter comme une capacité de réponse retrouvée, pas comme une économie de trésorerie fictive.
- **Sans moyens supplémentaires, quelque chose doit céder.**
  - Faire apparaître l’activité sacrifiée : réduire une couverture, reporter une migration ou arrêter un service. « Absorber » masque l’arbitrage lorsque toutes les personnes sont déjà engagées.
  - Ici, développer une décision que le responsable métier peut prendre : préserver le service essentiel et différer une amélioration réversible, plutôt que répartir silencieusement la dégradation partout.
  - Ne pas laisser croire qu’un arbitrage budgétaire dispense d’une obligation. Si les moyens manquent pour la satisfaire, escalader vers l’autorité compétente ; ne pas promettre une conformité que le plan ne permet pas d’atteindre.

## 6 — Gartner et achats : le favori peut-il perdre ?

- **Le classement ouvre la recherche, il ne conclut pas l’achat.**
  - Utilité légitime : découvrir des acteurs, structurer une comparaison. Puis passer de « qui domine le marché ? » à « qui répond à notre besoin avec notre exploitation ? ».
  - Ici, opposer une feuille de route à une capacité achetable : Cisco annonce Live Protect sans surcoût, mais distingue disponibilité annoncée et plateformes futures, avec réserve de livraison.[Cisco, p. 38](research/brksec-1785.md#achat) Angle auteur : exiger la preuve sur la version et le matériel visés, puis chiffrer l’exploitation. Sans surcoût ne signifie ni couverture locale ni coût total nul.
  - Ne pas remplacer le culte du leader par celui du challenger. Le leader peut gagner, notamment si son intégration et son support réduisent réellement le travail ; il doit simplement pouvoir perdre sur une exigence indispensable.
- **Une compétition sans élimination possible est un décor.**
  - Montrer comment le résultat peut être verrouillé avant les essais : contrat groupe, compétence rare déjà disponible ou calendrier incompatible avec une migration. La contrainte peut être valable ; la cacher fausse la discussion.
  - Ici, développer un critère éliminatoire annoncé avant le test : si l’export exploitable des données est indispensable, son absence ne se compense pas par une belle interface. Une révision de cette exigence suppose une décision explicite de l’autorité habilitée, et seulement si le droit et les engagements applicables le permettent ; un échec au test ne suffit pas à la rendre facultative.
  - Quand une seule offre reste réaliste, faire approuver un choix contraint et ses limites. Ne pas fabriquer trois candidats et une matrice flatteuse pour donner une apparence d’ouverture.
- **La dépendance peut réduire le levier de négociation.**
  - Déplacer l’attention du rabais vers la sortie : quels droits sur les données, quels formats disponibles, quel délai de restitution et quelle assistance de migration ? Les conditions contractuelles et la faisabilité technique doivent se rejoindre.
  - Ici, développer la différence entre « export autorisé » et « export réutilisable » : conserver événements et règles ne suffit pas si leur sens disparaît hors de la plateforme. Éprouver un échantillon représentatif avant de promettre la réversibilité.
  - Accepter une dépendance consciente si sa valeur justifie le coût futur ; éviter d’acheter une fausse indépendance plus coûteuse à maintenir que le risque qu’elle est censée réduire.

## 7 — Gouvernance : décider sans tout signer

- **L’avis du CISO n’est pas une autorisation universelle.**
  - Séparer l’expertise sur le risque, la décision de l’accepter dans une délégation et l’autorité d’exécuter une action. Un avis favorable sur un contrôle n’autorise pas à lui seul la mise en production d’un service.
  - Ici, prolonger le propos de Cisco sur les scripts devenus agents d’opérations IT et sur l’inventaire de leurs composants et accès.[Cisco, p. 44–47](research/brksec-1785.md#agents) Angle auteur : autoriser l’analyse n’autorise pas la modification réseau ; borner les identifiants du connecteur et vérifier leur révocation. Arrêter l’agent ne suffit pas à retirer les pouvoirs déjà transmis.
  - Ne pas confondre visibilité du board et transfert de responsabilité. L’enjeu éditorial est de montrer qui peut décider quoi, sans transformer chaque exception en séance du conseil.
- **Le CISO peut perdre un arbitrage légitime.**
  - Donner de la place à l’autre intérêt : disponibilité du service, engagement client, capacité de changement. Le désaccord ne prouve ni l’incompétence du décideur ni l’excès de prudence du CISO.
  - Ici, développer l’après-décision : conserver la recommandation écartée, les hypothèses du choix et les conditions de réexamen, puis contribuer à l’exécution. La trace sert à piloter, pas à préparer un « je vous l’avais dit ».
  - Une délégation dépassée ou une obligation non satisfaite change la situation : ce n’est plus simplement perdre un arbitrage valide. Escalader ce défaut plutôt que prétendre pouvoir tout arrêter personnellement.
- **Le silence ne vaut pas acceptation.**
  - L’absence de réponse laisse une décision en suspens. Préparer le suppléant, le canal joignable hors du système principal et les mesures conservatoires déjà autorisées ; l’urgence ne crée pas une délégation.
  - Ici, revenir brièvement à la British Library : le 28 octobre 2023, son équipe de crise Gold s’est réunie à 10 heures par appel vidéo WhatsApp en l’absence de courrier électronique. Le détail montre l’utilité d’un canal de secours, pas une recommandation universelle de cet outil.[1](research/developpement-sources.md#source-1)
  - Développer la frontière : une restriction réversible prévue par le mandat n’équivaut pas à l’arrêt général d’une activité. Si aucune autorité ne répond, documenter l’escalade et rester dans les pouvoirs effectivement accordés.

## Conclusion — Assumer ce qui attend

Revenir à un choix simple : lorsque la même équipe doit sécuriser la reprise et migrer, préserver d’abord la reprise si le maintien reste admissible. L’économie retardée est alors assumée, pas oubliée. Changer de trajectoire si le maintien devient inadmissible ou si une équipe distincte devient disponible. La maturité ne consiste pas à tout lancer : elle consiste à pouvoir expliquer ce qui attend, pourquoi, et ce qui ferait changer la décision.
