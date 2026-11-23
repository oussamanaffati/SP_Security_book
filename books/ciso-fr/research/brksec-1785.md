# BRKSEC-1785 — idées retenues, preuves et limites

Consulté le 23 novembre 2026. Source unique de cette passe : [1], distincte des identifiants du [registre de développement](developpement-sources.md). Les liens « Cisco, p. … » de la base renvoient aux rubriques ci-dessous, puis à la page exacte du PDF.

## Identité et méthode

**Titre affiché :** *Final Frontier - Security Playbook for the AI Era*. **Intervenants affichés :** Jatin Sachdeva et Mike McPhee, tous deux Principal Solutions Engineer (couverture, page PDF 1). Session **BRKSEC-1785**, Cisco Live APJC 2026. Le support porte © 2026 ; la page 2 annonce une modération Webex jusqu’au 19 novembre 2026, ce qui ne prouve pas le jour de présentation. Métadonnée de création : 10 novembre 2026 ; ce n’est pas une date de conférence. Le champ technique « author » du PDF indique Natalie Bain : ne pas le confondre avec les intervenants crédités.

**Numérotation :** 62 pages PDF, couverture comprise. Ici, « p. » désigne toujours l’index physique PDF, base 1, ciblé par `#page=N`, et non un numéro de diapositive imprimé. Les diapositives retenues n’affichent pas de numéro de slide distinct. La page PDF 53 porte toutefois « 58 » : aucun décalage uniforme n’a été supposé. Les titres de diapositives ci-dessous permettent de retrouver le passage même si le lecteur ignore les fragments de lien.

**Lecture :** extraction et lecture du texte des 62 pages, y compris ressources et clôture ; inspection visuelle des pages 1, 15, 26, 29, 34, 38, 51 et 53. Le graphique circulaire des pages 15–40 est illustratif : ni dénominateur ni mesure d’efficacité ne permet d’en tirer des pourcentages. Copie PDF, extraction intégrale, images et ledger de travail conservés hors dépôt, dans `/data/books/ciso-sans-boule-de-cristal/cisco-brksec-1785/`.

**Statut des preuves :** source primaire pour ce que Cisco recommande ou annonce ; pas validation indépendante de ses produits. Les conséquences CISO ci-dessous sont des interprétations éditoriales. Aucun nouveau taux, incident, résultat de laboratoire ni gain économique n’est introduit. Les sources historiques de la base sont conservées, pas présentées comme nouvellement auditées. La recherche telco demandée séparément n’est pas encore intégrée à cette passe.

<a id="maintenabilite"></a>

## 1. Acheter la maintenabilité — chapitre 3, axe 1

**Source :** « Recommended Model », « Step 1: Retire LDoS », « Why Technical Debt Can No Longer Wait », [pages PDF 14–17](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=14).[1]

> Remove what cannot be patched, supported, or upgraded.

Cisco recommande inventaire, priorité aux systèmes exposés à Internet, puis priorités métier, avec considérations particulières pour infrastructures critiques et OT (p. 16). **Interprétation retenue :** faire du renouvellement une décision sur la capacité de corriger et maintenir, pas sur l’âge seul. **Limite :** le support ne démontre pas qu’un retrait immédiat soit sûr ; maintien isolé et condition de sortie sont des propositions auteur, pas une garantie d’efficacité. Remplace une consigne générique sur le renouvellement.

<a id="dependances"></a>

## 2. Distribuer le contrôle ne supprime pas la dépendance — chapitre 3, axe 3

**Source :** « The new Zero Trust imperative is mesh of enforcers! », [page PDF 26](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=26) ; illustration de politique d’accès d’un agent, p. 29.[1]

> Common Control Plane

Le schéma distingue décision de politique et points d’application : pare-feu, SSE, agents, CNI et groupes de sécurité cloud. **Interprétation retenue :** tester règles conservées et capacité de changement quand la commande commune manque. **Limite :** le schéma ne décrit pas le comportement réel en panne et n’établit ni défaillance ni point unique de panne d’un produit. La comparaison avec le cas Cloudflare reste une question à éprouver, pas un incident commun. Remplace une conclusion générale sur la consolidation.

<a id="contenir"></a>

## 3. Acheter du temps, pas effacer la dette — chapitre 4, axe 1

**Source :** « Step 4: Compensating Controls », p. 32 ; « Step 5: Strategically Placed Live Protect Shields », p. 34 ; « A Runtime Shield Embedded in the Network OS », [page PDF 35](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=35) ; cycle de retrait p. 37 ; correctifs p. 40.[1]

> Not a patch — a shield

Cisco borne les types de vulnérabilités couverts, présente une protection ciblée et temporaire, puis un retrait après correction. **Interprétation retenue :** ne différer la correction que si la couverture du chemin exploitable est démontrée ; sinon réarbitrer. **Limite :** « Zero disruption » et absence d’effet sur CPU/mémoire/latence (p. 35) sont des promesses fournisseur, pas des résultats vérifiés ici. Aucune durée universelle de report n’est prescrite.

<a id="pilote"></a>

## 4. Mesurer une conclusion vérifiable — chapitre 4, axe 2

**Source :** « Foundry Security Spec », [page PDF 49](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=49) ; chaîne développement-test, p. 51.[1]

> From noisy alerts to verifiable security findings

**Interprétation retenue :** faire porter le pilote sur la reproductibilité autorisée et le travail net de validation, non sur le volume d’alertes. **Limite :** le support énonce une ambition, pas un benchmark. L’efficacité « comparable » des SLM Antares et les gains de Foundry (p. 51) ne sont pas repris. Remplace une formule générale sur le travail déplacé par un objet de test, sans ajouter de framework.

<a id="cadence"></a>

## 5. Financer une capacité récurrente de changement — chapitre 5, axe 1

**Source :** « Step 6: Fix (Patch, Update, etc.) », p. 40 ; « Consolidated Disclosure Model », p. 42 ; « Hardening our own systems », [page PDF 43](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=43).[1]

> Note: Critical issues are addressed out of cycle, as needed

Cisco annonce une cadence de divulgations et des versions durcies, sans exclure les correctifs urgents. **Interprétation retenue :** financer essais, bascule et retour arrière au-delà de la migration initiale ; préserver la voie urgente. **Limite :** cadence annoncée par Cisco, pas obligation générale ni calendrier opérationnel vérifié. Le nombre de CVE clôturées ne devient pas une mesure de sécurité. Remplace une répétition sur les heures de transition.

<a id="achat"></a>

## 6. Une roadmap n’est pas une capacité achetable — chapitre 6, axe 1

**Source :** limites de couverture p. 34 ; « Live Protect will be available across select Cisco platforms at zero additional cost », [page PDF 38](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=38).[1]

> when-and-if-available basis

La frise sépare « Available Today », trimestres annoncés et « Future » ; elle réserve les délais et la livraison. **Interprétation retenue :** vérifier version, matériel et charge d’exploitation, plutôt que transformer l’annonce sans surcoût en coût total nul. **Limite :** aucune disponibilité actuelle ni universalité de couverture certifiée ici. Remplace des critères génériques de comparaison, sans recommander un fournisseur.

<a id="agents"></a>

## 7. Gouverner les pouvoirs des agents d’exploitation — chapitre 7, axe 1

**Source :** « Step 7 – Yesterday’s scripts are today’s agents », [page PDF 44](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf#page=44) ; actifs, accès et composants IA, p. 45–47.[1]

> Yesterday’s scripts are today’s agents

Cisco attire l’attention sur l’IA dans les opérations IT, les services tiers et l’inventaire des modèles, agents, outils et MCP. **Interprétation retenue :** distinguer autorisation d’analyse et de modification, limiter les identifiants des connecteurs et vérifier la révocation. **Limite :** les détails de délégation et révocation sont notre prolongement, pas une procédure démontrée par le support. Aucun agent de l’auteur ni incident client n’est inventé.

## Pourquoi ne pas tout reprendre ?

- **Pages 5–9 : chiffres d’urgence omis.** « 8 hours », part de matériel vieillissant, vulnérabilités visant la fin de vie et délai médian de correction : populations, méthodes et comparabilité non vérifiées aux sources originales dans cette passe. Le support cite d’ailleurs le même intitulé de billet avec des dates différentes p. 5 et p. 43. Ces chiffres ne deviennent ni faits du livre ni probabilités locales.
- **Pages 10–14 : conserver l’équilibre, pas importer le slogan.** Fondamentaux et défense adaptative nourrissent la maintenabilité ; « machine speed » et « post-Mythos » ne constituent pas une preuve causale à ajouter au livre.
- **Pages 18–31, 45–54 : pas de catalogue de produits.** Retenir le mécanisme de dépendance et les pouvoirs des agents ; omettre listes de plateformes, promesses d’intégration et architecture à acheter. Les illustrations ne sont pas des incidents observés.
- **Pages 49–51 : pas de supériorité de modèle affirmée.** Le pilote reste éliminable ; aucune validation externe de Foundry, CodeGuard ou Antares n’est simulée.
- **Pages 55–62 : synthèse, ressources et clôture lues.** Les liens de ressources sont des pistes, non des sources supplémentaires réputées consultées. Ni cadre supplémentaire ni développement forcé des chapitres 1 et 2 : leurs arbitrages sont déjà distincts et mieux étayés par les cas conservés.

## Sources

[1] https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2026/pdf/BRKSEC-1785.pdf
