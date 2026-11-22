# Sources et limites — base auteur développée

Consultation : 22 novembre 2026. Cas historiques choisis pour leur mécanisme, pas présentés comme l’actualité la plus récente. Les identifiants ci-dessous proviennent du ledger local [ledger de développement](developpement-ledger.json), distinct du registre historique du dépôt. La liste des liens est générée en fin de fichier.

<a id="source-1"></a>

## [1] British Library — retour d’expérience du 8 mars 2024

**Document primaire :** récit institutionnel de l’attaque du 28 octobre 2023, et de la reprise dans l’état connu au 8 mars 2024. Corps du PDF récupéré et lu ; copie de travail `page1.pdf`, extraction `page1.txt`.

**Affirmations utilisées :** chapitre 1, des copies des collections numériques existaient mais l’absence d’infrastructure viable freinait la restauration (Executive Summary, p. 2). Chapitre 7, réunion Gold à 10 heures par WhatsApp vidéo en l’absence de courrier électronique le 28 octobre 2023 (section Causality, p. 4).

**Courts extraits vérifiés :**

> we have been hampered by the lack of viable infrastructure on which to restore it.

> convening at 10:00 by WhatsApp video call in the absence of email.

**Limites :** compte rendu de l’organisation touchée, pas expertise indépendante exhaustive. Ne prouve ni un délai de reprise universel ni l’inutilité des sauvegardes. Ne pas transformer le canal de crise utilisé en recommandation générale de WhatsApp. Le point d’entrée exact de l’attaque demeure incertain dans le rapport ; aucun récit de compromission certaine n’a été ajouté.

**Angle auteur proposé :** financer le retour du service et préparer une autorité joignable hors du système habituel. Ce sont des recommandations tirées du cas, non des effets mesurés.

<a id="source-2"></a>

## [2] Cloudflare — panne du plan de contrôle et de l’analytique, novembre 2023

**Document primaire :** billet de Matthew Prince, « Post mortem on the Cloudflare Control Plane and Analytics Outage ». Incident décrit du 2 novembre au 4 novembre 2023. HTML récupéré directement ; texte conservé dans `page2.txt`.

**Affirmations utilisées :** chapitre 3, architecture du plan de contrôle et de l’analytique sur trois centres de données en Oregon ; dépendances non évidentes de certains systèmes critiques ; maintien des services réseau et de sécurité. Passages : introduction et « Intended Design ».

**Courts extraits vérifiés :**

> some critical systems had non-obvious dependencies that made them unavailable.

> Throughout the incident, Cloudflare's network and security services continued to work as expected.

**Limites :** post-mortem du fournisseur ; ce n’est ni une cyberattaque ni la preuve que trois fournisseurs différents sont tombés. Certains clients ne pouvaient plus modifier des services, mais le trafic continuait. La généralisation aux dépendances communes entre contrats est un angle de raisonnement, pas une observation de ce cas. Extraction HTML artisanale imparfaite : titre, introduction et architecture lus ; la totalité des détails tardifs du billet n’est pas certifiée par cette extraction. Aucune affirmation ne repose sur ces passages tardifs.

**Angle auteur proposé :** tester l’indépendance effective des chemins de secours plutôt que compter les logos.

<a id="source-3"></a>

## [3] ENISA — publication du 26 juin 2025

**Document primaire :** « Supporting NIS2 implementation through actionable guidance », page institutionnelle récupérée directement ; `page3.txt`.

**Affirmations utilisées :** chapitre 2, le guide n’est pas juridiquement contraignant ; les entreprises concernées sont invitées à consulter leurs autorités nationales pour connaître leurs obligations. Paragraphe suivant la liste des fournisseurs dans le périmètre.

**Court extrait vérifié :**

> The implementation guidance is not a legally binding document

**Limites :** cette phrase porte sur le guide, pas sur la directive NIS2 ni sur le règlement d’exécution. Aucun état exhaustif de la transposition française n’est affirmé. L’utilité contractuelle éventuelle d’un référentiel est un raisonnement général à valider pour chaque contrat.

<a id="source-5"></a>

## [5] Verizon — DBIR 2025

**Document primaire :** rapport 2025, PDF récupéré directement ; `page5.pdf` et extraction `page5.txt`. Sections lues pour les affirmations : Introduction, Summary of findings, Results and analysis, Appendix A: Methodology. L’extraction de certaines pages en colonnes entrelace les phrases ; les passages de statistique utilisés restent lisibles.

**Affirmations utilisées :** chapitre 4, exploitation de vulnérabilités présente dans 20 % de toutes les violations analysées, formulation explicite dans Results and analysis. Corpus global : 22 052 incidents, dont 12 195 violations de données confirmées (Introduction). Fenêtre de collecte annoncée : 1er novembre 2023–31 octobre 2024 (méthodologie). Les graphiques de tendance mobilisent aussi des données antérieures.

**Courts extraits vérifiés :**

> But that uncertainty doesn’t take away from exploitation of vulnerabilities being present in 20% of all breaches we analyzed

> Thus, the incidents described in this report took place between Nov 1, 2023, and Oct 31, 2024.

**Limites :** corpus de cas fournis par Verizon, contributeurs et divulgations publiques, pas échantillon aléatoire de toutes les entreprises. La figure des vecteurs initiaux exclut Error/Misuse et affiche son propre dénominateur ; le texte auteur s’appuie sur l’énoncé explicite concernant l’ensemble des violations, pas sur un recalcul de cette figure. Le chiffre n’est ni un taux annuel de victimes ni une probabilité de compromission de l’organisation lectrice. Édition historique 2025, pas prétention d’utiliser la dernière édition disponible.

## Sources non retenues et incidents de récupération

Le ledger initial du dépôt a été consulté comme piste, non comme substitut de lecture des nouvelles preuves. L’extracteur web configuré refuse l’extraction ; récupération HTTP directe utilisée. `bs4` et `pdftotext` absents : extraction HTML simple et outil `read_file` pour les PDF, sans installation ni changement de configuration.

La page Gartner `https://www.gartner.com/en/research/methodologies/magic-quadrants` a renvoyé HTTP 403. Elle conserve l’identifiant technique [4] dans le ledger de travail mais n’est pas citée dans le manuscrit ni dans la liste des sources utilisées. L’attribution « Gartner le présente comme un point de départ » de l’ancienne base n’a donc pas été reproduite comme fait nouvellement vérifié : l’axe est conservé comme recommandation éditoriale. Pas de chiffre, citation ni prétendue lecture inventés pour combler ce blocage.

## Périmètre de publication

Publier au besoin les trois fichiers éditoriaux, pas les PDF, extractions complètes ou logs de récupération. Les extraits courts ci-dessus servent à contrôler les affirmations. Les fichiers bruts sont des pièces de travail ; les conserver hors du dépôt public. La validation automatique des références ne vaut pas expertise indépendante du fond.

## Sources

[1] https://www.bl.uk/home/british-library-cyber-incident-review-8-march-2024.pdf
[2] https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage
[3] https://www.enisa.europa.eu/news/supporting-nis2-implementation-through-actionable-guidance
[5] https://www.verizon.com/business/resources/reports/2025-dbir-data-breach-investigations-report.pdf
