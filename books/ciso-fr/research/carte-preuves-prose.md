# Carte des preuves — manuscrit en prose

Version du 23 novembre 2026, finalisée le 24 novembre 2026. Les fichiers `chapters/00.md` à `08.md` sont canoniques. Les commentaires HTML `preuve:` placés juste après un paragraphe relient les assertions documentaires aux références ci-dessous ; ils ne s'affichent pas dans la lecture Markdown rendue. Le manuscrit assemblé conserve exactement ces commentaires pour rester identique aux neuf composants. Les analyses et recommandations voisines ne sont pas présentées comme les conclusions mesurées des sources.

Trois espaces de noms, sans collision : **D** pour le registre de développement conservé ; **C** pour la lecture Cisco conservée ; **P** pour le [registre de cette refonte](prose-ledger.json). Les identifiants numériques de ces registres ne doivent pas être mélangés. Les sources externes sont des cas historiques et des documents datés, non une promesse de dernière actualité.

## Correspondance par assertion

| Marqueur | Fiches | Assertion soutenue et localisation | Référence auditable |
|---|---|---|---|
| D1 | 01, 07 | Copies numériques mais infrastructure de restauration manquante ; incompatibilité/support de systèmes, résumé exécutif et Impact. Réunion Gold par WhatsApp à 10 h le 28 octobre 2023, Causality. Pas de point d'entrée certain attribué. | [British Library, source 1](developpement-sources.md#source-1) |
| D2 | 03 | Panne du plan de contrôle et de l'analytique des 2–4 novembre 2023 ; architecture sur trois centres et dépendances ; services réseau et sécurité maintenus, introduction et Intended Design. | [Cloudflare, source 2](developpement-sources.md#source-2) |
| D3 | 02 | ENISA qualifie son guide de non juridiquement contraignant et renvoie aux autorités nationales ; publication du 26 juin 2025, pas conclusion sur la loi française. | [ENISA guide, source 3](developpement-sources.md#source-3) |
| D5 | 04 | 20 % des violations analysées ; corpus 22 052 incidents / 12 195 violations confirmées ; fenêtre principale 1er novembre 2023–31 octobre 2024. Introduction, Results and analysis, méthodologie. | [DBIR 2025, source 5](developpement-sources.md#source-5) |
| P1 | 04 | CVSS de base mesure la sévérité, pas seul le risque ; groupes base/menace/environnement et nomenclature. Guide FIRST v4.0, version documentaire 1.2. | Source [1] ci-dessous |
| P2 | 01 | 188 incidents significatifs de 2024, dont 113 défaillances système et 15 actions malveillantes ; résumé, pages PDF 4–6 / imprimées 3–5. | Source [2] ci-dessous |
| P3 | 05 | Près de deux heures de retour arrière, au moins douze heures jusqu'au rétablissement complet ; congestion de réenregistrement ; changement de configuration, pas patch de sécurité. Rapport FCC publié le 22 juillet 2024, §§2, 6–8, 26–27. | Source [3] ci-dessous |
| C-maint | 03 | Recommandation de retrait des systèmes non corrigeables/supportables, exposition et précautions OT ; pages PDF 14–17. | [Maintenabilité](brksec-1785.md#maintenabilite) |
| C-plan | 03 | Schéma de points d'application distribués et plan de contrôle commun ; page PDF 26. Aucun comportement en panne certifié. | [Dépendances](brksec-1785.md#dependances) |
| C-temp | 04 | Live Protect présenté comme temporaire et ciblé, non correctif ; pages PDF 34–37. | [Confinement](brksec-1785.md#contenir) |
| C-essai | 04 | Ambition de constats vérifiables Foundry, pas benchmark ; pages PDF 49–51. | [Essai](brksec-1785.md#pilote) |
| C-cadence | 05 | Cadence annoncée de versions/divulgations et traitement critique hors cycle ; pages PDF 40–43. | [Cadence](brksec-1785.md#cadence) |
| C-achat | 06 | Annonce sans coût additionnel, plateformes/horizons distincts et réserve de livraison ; page PDF 38. Pas de disponibilité actuelle certifiée. | [Achat](brksec-1785.md#achat) |
| C-agent | 07 | Agents d'opérations, inventaire et accès, pages PDF 44–47. Les permissions et la révocation développées sont une analyse, pas une procédure Cisco démontrée. | [Agents](brksec-1785.md#agents) |

Introduction et conclusion : pas de nouveau fait public nécessitant un marqueur. Position constructeur autorisée par le contexte utilisateur ; aucune clientèle, réunion ou expérience personnelle ajoutée. La situation finale est explicitement hypothétique, sans budget ni résultat inventé. Les mécanismes techniques non attribués sont des raisonnements d'architecture conditionnels, pas des observations d'une entreprise réelle.

## Recherches héritées conservées

Le dossier telco complet, ses propositions, sa provenance, sa revue réelle `grok-4.7`, ses ledgers et corps primaires restent dans `/data/books/ciso-sans-boule-de-cristal/telco-verification/`. Le dossier Cisco reste dans `/data/books/ciso-sans-boule-de-cristal/cisco-brksec-1785/` et le développement dans `/data/books/ciso-sans-boule-de-cristal/developpement/`. Ces chemins sont des emplacements de travail, pas des liens publics. Aucune copie intégrale de PDF ou de page tierce n'est ajoutée au dépôt. Les synthèses et les URL permettent l'audit public ; les corps locaux permettent l'audit détaillé sur la machine.

Les propositions de format « trois axes » de ces dossiers sont historiques. Leur fact-check n'est pas annulé par la nouvelle prose. Les apports telco retenus ici sont ENISA pour le conseil et FCC pour le budget. CISA, code britannique et Talos restent en réserve ; aucun réétiquetage statistique n'est fait pour les intégrer à tout prix.

La nouvelle récupération FIRST a utilisé HTTP direct après l'échec de l'extracteur configuré en recherche seule ; corps lu et conservé temporairement dans `/data/cache/scratch/ciso-first-user-guide.txt`. Les autres assertions reprennent les pièces primaires locales, sans nouvelle récupération réseau. Les [incertitudes et limites de lecture](../progress/incertitudes-prose.md) comprennent les troncatures héritées et la divergence interne ENISA sur le nombre de pays. La cohérence des citations ne constitue pas une validation indépendante de toutes les assertions.

## Sources

[1] https://www.first.org/cvss/v4.0/user-guide — FIRST CVSS v4.0 User Guide
    > "CVSS Base Score (CVSS-B) Measures Severity, not Risk"
[2] https://www.enisa.europa.eu/sites/default/files/2025-07/ENISA_Telecom_Security_Incidents_2024_en_1.pdf — ENISA Telecom Security Incidents 2024
    > "Malicious actions accounted for 15 incidents representing 8% share of total incidents"
[3] https://docs.fcc.gov/public/attachments/DOC-404150A1.txt — FCC AT&T Mobility Outage
    > "It took close to two hours to roll back the network change."
