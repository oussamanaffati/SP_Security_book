# Mind map — La sécurité n’est pas un concours de slides

- **Centre : décider sous contraintes, pas collectionner des solutions.**
- **Lecture :** chaque branche possède son propre objet ; les flèches relient les décisions, elles n’imposent pas l’ordre des achats.

```mermaid
mindmap
  root((Décider en CISO))
    1 Board
      Comparer les options
      Distinguer économies et risque
      Exposer les inconnues
      Arbitrage stratégique
    2 Standards
      Droit et guides distincts
      Périmètre et applicabilité
      Contrôle et preuve
      Notifications préparées
    3 Investissements
      Coûts futurs
      Acheté à éprouvé
      Maintenir ou réparer
      Réduire ou remplacer
    4 Veille
      Urgence réelle
      Décision d'évolution
      Exploration bornée
      Essai contre référence
    5 Budget
      Argent
      Capacité de changement
      Capacité récurrente
      Arrêts explicites
    6 Gartner et achats
      Marché et besoin local
      Exigences éliminatoires
      Essai comparable
      Contrat et sortie
    7 Gouvernance
      Avis et autorisation
      Délégation bornée
      Suppléance et escalade
      Confinement et reprise
```

## Les tensions à garder visibles pendant la rédaction

- **1 ↔ 5 :** une décision de financement n’invente pas la capacité d’exploitation.
- **2 ↔ 5 :** une contrainte budgétaire ne rend pas une obligation facultative ; les options doivent traiter le conflit.
- **3 ↔ 6 :** le meilleur nouveau produit peut ne pas justifier une migration ; l’existant ne bénéficie pas d’une rente éternelle.
- **4 ↔ 6 :** l’expérience teste une hypothèse ; l’achat engage des coûts et une dépendance.
- **4 ↔ 7 :** déléguer une action à un agent ne supprime pas la question de l’autorité.
- **7 ↔ 1 :** la direction arbitre ; le fonctionnement quotidien ne doit pas attendre son prochain comité.
- **Tous ↔ roadmap :** une recommandation ne devient un chantier qu’avec une dépendance levée et une capacité attribuée.

## Carte de décision de la roadmap

```mermaid
flowchart TD
    S[Service et scenario de perte] --> Q[Obligations et expositions a qualifier]
    Q --> U{Urgence ou echeance imposee}
    U -->|Oui| M[Mesure immediate et arbitrage explicite]
    U -->|Non| O[Options et preuves manquantes]
    M --> O
    O --> C[Capacite et dependances]
    C --> G{Peut-on tenir engagement et exploitation}
    G -->|Non| L{Droit applicable securite personnes ou installations clause non negociable}
    L -->|Oui| H[Financer ou reduire activite licitement ou escalader]
    H --> Q
    L -->|Non| R{Option retenue par autorite habilitee}
    R -->|Financer| CAP[Budget recurrent et capacite attribues]
    CAP --> C
    R -->|Reduire perimetre| Q
    R -->|Differer| D[Exposition documentee et revue datee]
    D --> REV{Revue echue ou hypothese changee}
    REV -->|Oui| Q
    REV -->|Non| D
    G -->|Oui| DEC[Decision de autorite habilitee]
    DEC --> T[Essai ou correction bornee]
    T --> P{Resultat conforme aux criteres}
    P -->|Non| A[Arreter ou corriger une hypothese precise]
    A --> O
    P -->|Oui| E[Etendre puis maintenir]
    E --> V{Changement materiel ou hypothese invalidee}
    V -->|Oui| O
    V -->|Non| N[Maintenir jusqu'a la prochaine revue]
    N --> V
```

## Angles morts à chercher, pas liste universelle d’achats

- **Chemin d’attaque :** exposition → identité humaine ou machine → droits → données ou service → conséquence.
- **Chemin de reprise :** administration de confiance → accès aux sauvegardes → restauration intègre → transaction métier → dépendances.
- **Chemin d’innovation :** problème → référence simple → essai → coût de supervision → autorisation → arrêt possible.
- **Chemin d’achat :** besoin → options admissibles → preuve locale → engagement contractuel → exploitation → sortie.
- **Chemin de gouvernance :** expertise → décision habilitée → exécution → vérification → recours.
