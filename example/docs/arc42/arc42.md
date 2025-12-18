# Arc42 et DDD

Ce document, basé sur le modèle arc42, décrit une plateforme de courtage en ligne pour investisseurs particuliers dans le cadre du cours LOG430.

## 1. Introduction et Objectifs

### Panorama des exigences
BrokerX est une plateforme de courtage en ligne permettant à des investisseurs d'émettre des ordres, consulter leur portefeuilles, recevoir exécutions et confirmations puis effectuer le règlement et la compensation des transactions.

L'objectif principal de BrokerX est de fournir une platforme de courtage fiable, performante et sécurisée pouvant supporter un grand nombre de transactions simultannées.

#### Priorisation des cas d'utilisation
| Priorité | UC | Justification |
|----------|----|---------------|
| **Must** | UC-03: Approvisionnement du portefeuille | Nécessaire pour placer un ordre d'achat. |
| **Must** | UC-05: Placement d’un ordre (marché/limite) avec contrôles pré-trade | Permet d'exécuter le matching des ordres (UC-07) qui est aussi un cas d'utilisation prioritaire. Sans cette fonctionnalité, il n'y aurait aucun autre moyen d'acheter ou de vendre.  |
| **Must** | UC-07: Appariement interne & Exécution | Core de la plateforme, algorithme principal. |
| **Should** | UC-04: Abonnement aux données du marché | Devrait être implémenté si possible car a un impacte sur le placement d'un ordre. Toutefois, cet impacte est mineur donc ce cas n'est pas prioritaire. |
| **Should** | UC-06: Modification / Annulation d’un ordre | Comme UC-04, ce cas impacte aussi le placement d'un ordre mais il n'est pas absolument nécessaire. |
| **Could** | UC-01: Inscription & Vérification d’identité | Nécessaire pour les prochaines itérations, mais on peut fonctionner avec un compte existant pour l'instant. |
| **Could** | UC-02: Authentification & MFA | Nécessaire pour les prochaines itérations, mais on peut fonctionner avec un compte pré-connecté pour l'instant. |
| **Won't** | UC-08: Confirmation d’exécution & Notifications | Bonus pour le UX mais pas prioriatire pour l'instant. |

### Objectifs qualité
| Priorité | Objectif qualité | Scénario |
|----------|------------------|----------|
| 1 | **Efficacité de performance** | Être capable de gérer un débit d'au moins 1200 ordres par seconde avec un temps de latence de moins de 100 ms. |
| 2 | **Fiabilité** | Avoir une disponibilité d'au moins 99.9%. |
| 4 | **Maintenabilité** | Code simple et bien structuré pour faciliter l'évolution. |

### Parties prenantes
- Développeur: Analyse de la logique métier, conception de l'architecture, implémentation, documentation, tests et déploiement.
- Clients: Utilisent la plateforme via son interface.
- Instrument Service: Stock tous les instruments et l'historique des quotes
- Portfolio Service: Effectue toute la gestion des portfolios des utilisateurs (solde, positions, historique des transactions)
- Matching Engine: Effectue l'appariement des ordres, la validation des trades et stock les ordres du carnet

## 2. Contraintes d'architecture
| Contrainte | Description |
|------------|-------------|
| **Technologie** | Utilisation de Docker |
| **Déploiement** | Déploiement via conteneur Docker et pipeline CI/CD sur une machine virtuelle |
| **Style d'architecture** | Architecture microservices |
| **Solution de persistance** | Implémenter une couche de persistance cohérente (ORM ou DAO) |

## 3. Portée et contexte du système
### Contexte métier
![Diagramme de contexte](/docs/diagrams/context.svg) \
<i>Le diagramme ci-haut démontre le contexte du système. Les clients de BrokerX communiquent avec la plateforme afin de gérer leur portfolio, consulter les cotations du marché et placer des ordres. Ensuite, BrokerX s'occupe de l'appariement et de l'exécution des ordres au fur et à mesure que des nouvels ordres sont placés par les clients. Finalement, BrokerX communique en parallèle avec un fournisseur de données de marché pour afficher les cotations aux clients.</i>

![Modèle du domaine](/docs/diagrams/mdd.svg) \
<i>Le diagramme ci-haut présente le modèle du domaine de BrokerX. Premièrement, il décrit les clients (User) et leur portfolio (solde, positions, transactions, etc). Deuxièmement, il décrit les ordres et ce qui les entours (carnet d'ordres, matching engine, contrôle pré-trade, etc).</i>

### Contexte technique
Client: Application Blazor Server (C#) \
Persistence: Base de données PostgreSQL

## 4. Stratégie de solution
| Problème | Stratégie de solution | Justification | 
|----------|-----------------------|---------------|
| **Efficacité de performance** | Utiliser C# et PostgreSQL | Combiner la puissance de C# et les query optimisées de Postgres permettra d'atteindre les critères de performance demandé. |
| **Fiabilité** | Utilisation d'une base de données SQL | Propriétés ACID. |
| **Maintenabilité** | Utiliser une architecture hexagonale avec C# | En découplant le business core du reste du système, il sera facile de changer de framework au besoin. |

## 5. Vue des blocs de construction
![Vue logique](/docs/diagrams/logical_view.svg) \
<i>Le diagramme ci-haut démontre la vue logique du système. Il s'agit d'un diagramme de classe qui reprend les concepts du domaine du domaine et les illustre sous forme de classe.</i>

![Vue du dévelopement](/docs/diagrams/development_view.svg) \
<i>Le diagramme ci-haut démontre la vue de développement du système. Il s'agit d'une représentation de l'implémentation et de l'organisation des artéfacts de code. On y retrouve la mise en forme d'une architecture hexagonale.</i>

![Vue d'exécution](/docs/diagrams/engine_saga_state_machine.svg) \
<i>Le diagramme ci-haut démontre le diagrame d'état de la saga chorégraphiée du moteur d'appariement.</i>

## 6. Vue d'exécution
![Vue d'exécution](/docs/diagrams/execution_view.svg) \
<i>Le diagramme ci-haut démontre les cas d'utilisation de la première phase. Pour plus de détails, voir la section pour la priorisation des cas d'utilisation.</i>

## 7. Vue de déploiement
![Vue de déploiement](/docs/diagrams/deployment.svg) \
<i>Le diagramme ci-haut visualize l'architecture de déploiement du système. Celui-ci sera déployé sur une machine virtuelle qui host un Docker container. Ce conteneur contient l'application et sa base de données.</i>

## 8. Concepts transversaux
- Ordres et exécutions
- Portefeuille, portfolio et positions
- Cotations
- Conformité et risque
- Observabilité et audit
- Microservices
- Message broker
- Architecture hexagonale
- Persistence, base de données SQL, ACID

## 9. Décisions d'architecture
<!-- include:files path="example/docs/adr/"  -->

## 10. Exigences qualité

### Efficacité de performance
Être capable de gérer un débit d'au moins 1200 ordres par seconde avec un temps de latence de moins de 100 ms.

### Fiabilité
Avoir une disponibilité d'au moins 99.9%.

### Maintenabilité
Code simple et bien structuré pour faciliter l'évolution.

## 11. Risques et dettes techniques
- Très difficile de faire de la scalabilité horizontale avec une base de donnée SQL
- Complexité ajoutée si on doit modifier le schéma de la base de données
- Point de défaillance unique: si la base de donnée plante, le système devient complètement inutilisable

## 12. Glossaire
| Terme | Définition |
|-------|------------|
| **Ordre** | Directive d'achat ou de vente d'un titre, comme une action, un FNB ou une option, à un prix donné ou selon certaines conditions |
| **CI/CD** | Continuous Integration/Continuous Deployment : pratiques d'automatisation du développement et déploiement des applications |
| **ORM** | Object-Relational Mapping: couche d'abstraction qui traduit les objets en tables relationnelles et vice-versa |
| **DAO** | Data Access Object: abstrait les opérations de base de données |
| Priorité **Must** | Aspect non-négociable qui est absolument nécessaire |
| Priorité **Should** | Aspect important mais non vital, qui apporte une valeur significative |
| Priorité **Could** | Aspect agréable à avoir mais qui a un impact faible si il est exclu |
| **Carnet d'ordres** | Liste des ordres actifs en attente de matching par le moteur d'exécution |
| **Exécution** (Fill) | Événement qui résulte de l’appariement d’un ordre avec une contrepartie dans le carnet d’ordres |
| **Instrument** | Actif financier négociable |
| **Cotation** (Quote) | Information de marché en temps réel décrivant l’état d’un instrument |
| **Portfolio** | Ensemble des avoirs financiers d’un utilisateur (liquidité & positions) et son historique des transactions |
| **Position** | Quantité d’un instrument financier détenue par un utilisateur dans son portfolio |
| **Règlement** | Mise à jour des positions et soldes après exécution |
| **Ordre au marché**(Market order) | Exécuté immédiatement au meilleur prix disponible |
| **Ordre à cours limité** (Limit order) | Exécuté seulement au prix limite ou meilleur |
| **Day order** (DAY) | Ordre valide jusqu’à la fin de la journée de trading |
| **Good Till Cancelled** (GTC) | Ordre qui reste active jusqu’à annulation par le client (ou expiration système) |
| **Immediate-Or-Cancel** (IOC) | Exécution immédiate d'un ordre, partiel possible, reste annulé |
| **Fill-Or-Kill** (FOK) | Ordre qui doit être exécuté entièrement tout de suite, sinon annulé |
| **Good-Till-Date** (GTD) | Ordre qui est actif jusqu’à une date/heure précise. |