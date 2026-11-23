# Audit global préalable — contrat prose

Date de travail : 23 novembre 2026 (horloge UTC). Référence Git initiale : `7c9560b`. Arbre propre à l'inventaire. Le travail interrompu avait bien produit et commité l'intégration Cisco : ne pas la refaire comme si elle n'existait pas. Aucun manuscrit en prose actif dans le dépôt à ce point ; les neuf fiches sont des consignes de rédaction. Le README attribue encore la prose future à Oussama. Ce contrat est remplacé explicitement par la demande présente.

## Lectures et pièces préservées

Lecture complète des neuf fiches, de `base-auteur.md`, du README et de la carte faisant office de plan. Lecture du registre de développement, de la note BRKSEC-1785, de l'annexe juridique, du dossier telco, de ses propositions et de sa provenance. Sources de travail consultées : extractions British Library, Cloudflare, ENISA (guide et incidents), DBIR 2025, FCC et les 62 pages textuelles de BRKSEC-1785. Les extractions historiques British Library et DBIR contiennent des coupures héritées ; celle de Cloudflare ne garantit pas la fin du billet. Les passages portant les faits retenus sont présents et lus. Ne pas présenter cette lecture comme une nouvelle vérification visuelle intégrale des PDF. FIRST CVSS v4.0, guide version documentaire 1.2, récupéré directement et lu en texte pour le nouveau développement sur la sévérité et l'exposition.

Les dossiers `/data/books/ciso-sans-boule-de-cristal/cisco-brksec-1785`, `telco-verification` et `developpement` restent intacts, hors publication des corps de sources. L'audit telco a réellement reçu une contradiction `grok-4.7`, mais ce n'est pas une revue du futur manuscrit. Ses propositions héritées de trois axes n'imposent plus la forme. La carte et la base resteront des archives éditoriales, non la livraison active.

## Diagnostic

La matière est bonne, sa forme n'est pas un livre. Les formulations « développer », « ici raconter » et les arbitrages compressés font porter au lecteur le travail de raisonnement. La nouvelle prose doit restituer les liens techniques entre faits, pas ajouter des transitions entre puces. Les situations sont conservées ; les trois parties obligatoires et les sous-listes ne le sont pas.

Le principal risque éditorial est la répétition : preuve, reprise, dépendance et autorité peuvent envahir tous les chapitres. Chaque mécanisme aura un lieu principal. Le principal risque factuel est l'effacement du dénominateur ou du statut d'une source : panne devenue attaque, roadmap devenue fonctionnalité livrée, recommandation devenue droit. Les réserves détaillées vont dans un suivi séparé ; celles nécessaires au sens restent dans la phrase.

## Plan interne traçable

| Fiche | Travail de fond | Épreuve contradictoire |
|---|---|---|
| 00 | Position constructeur ; distinguer menace, besoin et produit ; contrat de lecture | Ne pas remplacer le marketing par un scepticisme automatique |
| 01 | Conseil, chaîne de reprise, valeur d'information et choix refusé ; British Library et ENISA | La disponibilité n'absorbe pas la confidentialité ; financement n'est pas acceptation |
| 02 | Applicabilité, preuve de conception et de fonctionnement, changement invalidant | Un guide non contraignant n'est pas sans valeur ; ne pas simuler un avis juridique français |
| 03 | Maintenabilité, coût futur de sortie, chemins identité/commande ; Cloudflare et Cisco | Consolidation parfois meilleure que diversité de façade |
| 04 | CVSS, composant actif et chemins d'accès ; DBIR borné ; confinement ; pilote éliminable | Ne pas attendre une certitude parfaite ; qualité avant vitesse |
| 05 | Trésorerie et capacité de transition, remise en charge ; FCC AT&T ; gains non interchangeables | Le maintien peut devenir inadmissible ; le report n'est pas toujours prudent |
| 06 | Classement, capacité achetable, exigences éliminatoires, sortie réutilisable | Leader ou choix contraint légitimes ; ne pas inventer la méthodologie Gartner |
| 07 | Avis, acceptation, exécution ; agent et révocation ; crise hors canal principal | Urgence sans pouvoir nouveau ; exécuter une défaite légitime |
| 08 | Trajectoire conditionnelle complète, sélection et renoncements | Ne pas finir par un catalogue ni prétendre à une recette universelle |

Cycle séquentiel : écrire une fiche, auto-critiquer RSSI/ingénieur/dirigeant/lecteur, corriger puis commit local de la fiche et de sa revue. Deux passes finales distinctes : cohérence de l'argument et style ; preuves/liens/assemblage. Modèle de rédaction et auto-critique : `gpt-6-astra`, runtime déclaré. Pas de nouvelle revue indépendante revendiquée. Pas de push dans cette mission ; revue et publication finales réservées au parent.

## Acceptation

Neuf textes substantiels en prose française, sans scènes ni clients inventés ; sept situations conservées ; sources auditées à côté. Manuscrit concaténé exactement depuis les neuf fichiers canoniques, ordre 00–08. Comptages reproductibles, contrôle des expressions bannies et des listes, vérification du périmètre Git, rapport final et README univoque. Aucun score de détecteur d'IA. Le livre anglais demeure intouché.
