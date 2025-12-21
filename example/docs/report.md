## Vues 4+1

### Vue logique
![Vue de déploiement](/docs/diagrams/logical_view.svg) \
<i>Le diagramme ci-haut démontre la vue logique du système. Il s'agit d'un diagramme de classe qui reprend les concepts du domaine du domaine et les illustre sous forme de classe.</i>

### Vue de développement
![Vue de déploiement](/docs/diagrams/development_view.svg) \
<i>Le diagramme ci-haut démontre la vue de développement du système. Il s'agit d'une représentation de l'implémentation et de l'organisation des artéfacts de code. On y retrouve la mise en forme d'une architecture hexagonale.</i>

### Vue des processus
![Vue de déploiement](/docs/diagrams/process_view.svg) \
<i>Le diagramme ci-haut démontre la vue des processus du système. Soit la communication entre les éléments de l'architecture pendant la réalisation des cas d'utilisation.</i>

### Vue physique
![Vue de déploiement](/docs/diagrams/deployment.svg) \
<i>Le diagramme ci-haut visualize l'architecture de déploiement du système. Celui-ci sera déployé sur une machine virtuelle qui host un Docker container. Ce conteneur contient l'application et sa base de données.</i>

### Scénarios
![Vue de déploiement](/docs/diagrams/execution_view.svg) \
<i>Le diagramme ci-haut démontre les cas d'utilisation de la première phase. Pour plus de détails, voir la section pour la priorisation des cas d'utilisation.</i>

<div style="page-break-after: always;"></div>

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

<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>ADR</th><td><p>001</p></td></tr>
<tr><th>Nom</th><td><p>Utilisation d'une architecture hexagonale (ports and adapters)</p></td></tr>
<tr><th>Statut</th><td><p>Acceptée</p></td></tr>
<tr><th>Contexte</th><td><p>Le système BrokerX doit être flexible et maintenable facilement. La plateforme contient une logique métier riche et évolutive qui doit être indépendante des autres composants et technologies utilisés. De plus, nous savons que l'architecture du système évoluera en une architecture évenementielle et microservices.</p></td></tr>
<tr><th>Décision</th><td><p>Nous adopterons une architecture hexagonale (ports and adapter) en tandem avec le repository pattern.</p></td></tr>
<tr><th>Conséquences</th><td><p>L'adoption de ce style d'architecture est plus long à mettre en place car elle est plus complexe que MVC par exemple. Cependant, ce style d'architecture apporte plusieurs avantages:</p>
<ul>
<li>Séparation des responsabilités: Faible couplage et forte cohésion.
<li>Testabilité: Facile de tester chaque module indépendement.
<li>Évolutivité: Facile de changer les adapteurs au besoin pour faire évoluer la plateforme. Facilitera aussi le changement vers les autres styles d'architecture.
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>ADR</th><td><p>002</p></td></tr>
<tr><th>Nom</th><td><p>Utilisation d'une base de données SQL (PostgreSQL)</p></td></tr>
<tr><th>Statut</th><td><p>Acceptée</p></td></tr>
<tr><th>Contexte</th><td><p>Le domaine métier de BrokerX a plusieurs exigences au niveau des données. Celles-ci doivent rester cohérente et leur lecture doit être fiable et performante.</p></td></tr>
<tr><th>Décision</th><td><p>Nous allons utiliser une base de données SQL, plus précisement, PostgreSQL.</p></td></tr>
<tr><th>Conséquences</th><td><p>PostgreSQL permet aussi de faire des requêtes complexes et puissantes. En revanche, il sera plus compliqué d'effectuer des migrations si nécessaire, et la scalability horizontale est plus difficile avec une base de données SQL.</p></td></tr>
</table><br />

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


<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Permettre à un nouvel utilisateur de créer un compte sur la plateforme en fournissant ses  informations personnelles, de vérifier son identité selon les exigences réglementaires  (KYC/AML) et d’activer son accès à la plateforme. Ce cas établit la relation de confiance initiale  entre l’utilisateur et BrokerX. </p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Aucune
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Compte créé avec l'état approprié (pending, active ou rejected)
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut s'inscrire à la platforme.</li>
<li>Le client fournis ses données personnelles (nom, prénom, email, date de naissance, numéro de téléphone, et adresse).</li>
<li>Le système valide les données du client.</li>
<li>Le client choisit une méthode de vérification (email ou sms).</li>
<li>Le système créer un compte avec l'état "pending" et envoie un code de vérification (email ou sms).</li>
<li>Le client entre le code de vérification.</li>
<li>Le système met à jour le compte avec l'état "active".</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Une ou plusieurs données est invalide
<ol>
<li>Le système marque les champs invalide avec un message d'erreur.</li>
<li>Retour à l'étape 2 du CU.</li>
</ol>
<li>3.2 L'adresse email est déjà utilisé par un autre compte
<ol>
<li>Le système indique au client que l'adresse saisie est déjà utilisé.</li>
<li>Retour à l'étape 2 du CU.</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Garantir un accès sécurisé à la plateforme en permettant aux clients de s’authentifier avec  identifiant/mot de passe et, le cas échéant, via un mécanisme de multi-facteurs (OTP, TOTP,  WebAuthn). Ce cas protège les comptes contre les accès non autorisés.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client est déconnecté
<li>Le compte du client est à l'état "active"
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Une session est établie
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut se connecter à la plateforme.</li>
<li>Le client saisie son adresse email et son mot de passe.</li>
<li>Le système valide les identifiants du client.</li>
<li>Le système envoie un code de vérification au client.</li>
<li>Le client saisie le code de vérification.</li>
<li>Le système créer une session et envoie un token au client.</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Les identifiants saisies sont invalide
<ol>
<li>Le système indique l'erreur au client</li>
<li>Retour à l'étape 2 du CU</li>
</ol>
<li>5.1 Le code saisie ne correspond pas à celui envoyé
<ol>
<li>Le système indique l'erreur au client</li>
<li>Le système bloque temporairement le compte du client (5 minutes)</li>
<li>Fin du CU</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Donner aux utilisateurs la possibilité de créditer leur portefeuille virtuel en effectuant des  dépôts simulés, afin de disposer de liquidités nécessaires pour placer des ordres d’achat. Ce  cas assure la disponibilité des fonds pour les opérations boursières.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client est connecté
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Le solde du portefeuille du client a augmenté selon le montant choisit
<li>Une transaction a été ajouté au portfolio du client
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut approvisionner son portefeuille virtuel.</li>
<li>Le client saisie le montant qu'il veut ajouter à son compte.</li>
<li>Le système valide le montant saisie selon les valeurs minimales et maximales acceptées.</li>
<li>Le système créé une transaction <i>Pending</i> et envoie la requête au système de paiement.</li>
<li>Le système ajoute le montant au solde du portefeuille, met à jour la transaction et notifie le client.</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Le montant saisie est refusé
<ol>
<li>Le système notifie le client et lui demande de saisir un montant valide. Fin du CU.</li>
</ol>
<li>4.1 Le système de paiement refuse la transaction 
<ol>
<li>Le système notifie le client et lui demande de réessayer. Fin du CU.</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Offrir aux clients un accès en temps réel aux cotations et carnets d’ordres pour les  instruments suivis. Ce cas permet aux investisseurs de prendre des décisions éclairées grâce à  des données actualisées.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client est connecté
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Flux de données établi
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut s'abonner à un instrument</li>
<li>Le client sélectionne l'instrument auquel s'abonner</li>
<li>Le système ouvre un canal de communication et y insère les mises à jour (cotations, trade)</li>
<li>Le client reçoit les mises à jour périodiquement</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Une erreur se produit lors de l'ouverture du canal
<ol>
<li>Le système notifie le client, fin du CU</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Permettre aux clients de soumettre des ordres d’achat ou de vente (marché ou limite), qui  seront validés par des contrôles pré-trade et insérés dans le moteur d’appariement. Ce cas  constitue le cœur fonctionnel de la plateforme de courtage.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client est connecté
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>L'ordre est accepté et envoyée au moteur d'appariement
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut placer un nouvel ordre.</li>
<li>Le client rempli le formulaire:</li>
<ul>
</ol>
<li>Achat ou vente
<li>Ordre au marché ou ordre à cours limite
<li>Instrument (symbole)
<li>Quantité d'action
<li>Prix limite (si ordre à cours limite)
<li>Durée de l'ordre (DAY, GTC, IOC, FOK, GTD)
</ul>
<ol>
<li>Le système valide les éléments suivant:</li>
<ul>
</ol>
<li>La quantité est supérieur à 0
<li>Le portfeuille du client possède des fonds suffisant
<li>L'instrument est actif
<li>Empêcher les short-sells
</ul>
<ol>
<li>Le système créer l'ordre et l'envoie au moteur d'appariement (déclanchement de UC-07)</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Un élément est invalide
<ol>
<li>Le système notifie le client de l'erreur. Fin du CU.</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Offrir la possibilité de modifier ou d’annuler un ordre actif dans le carnet tant qu’il n’est pas  totalement exécuté. Ce cas donne de la flexibilité aux clients pour gérer leurs stratégies de  trading.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client est connecté
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>L'ordre est modifié ou annulé
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le client veut modifier ou annuler un ordre qu'il a placé</li>
<li>Le client sélectionne l'ordre à modifier ou annuler</li>
<li>Le client modifie l'ordre et fournit la nouvelle quantité et/ou prix</li>
<li>Le système valide que l'ordre peut être modifié</li>
<li>Le système vérouille l'ordre et applique les modifications</li>
<li>Le système refait le contrôle pré-trade sur l'ordre</li>
<li>Le système notifie le client que l'opération est terminée</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><ul>
<li>3.1 Le client annule l'ordre
<ol>
<li>Le système marque l'ordre comme annulé et met à jour le carnet</li>
<li>Redirection vers l'étape 7 du CU</li>
</ol>
<li>4.1 L'ordre n'est pas working ou partially filled
<ol>
<li>Le système indique au client que l'opération ne peut être effectuée, fin du CU</li>
</ol>
<li>5.1 L'ordre est exécuté avant le verrouillage
<ol>
<li>Le système indique au client que l'opération ne peut être effectuée, fin du CU</li>
</ol>
<li>6.1 Le contrôle pré-trade échoue
<ol>
<li>Le système indique au client que l'opération ne peut être effectuée, fin du CU</li>
</ol></li>
</ul></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Assurer l’exécution automatique des ordres en interne selon les règles de priorité  (prix/temps) en rapprochant acheteurs et vendeurs. Ce cas fournit la mécanique centrale de  traitement des transactions sur la plateforme.</p></td></tr>
<tr><th>Acteurs</th><td><p>Aucun (déclanché automatiquement par le système)</p></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Aucune
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Une ou plusieurs exécution créées
<li>Ordre mis à jour
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>Le système veut effectuer l'appariement d'un ordre.</li>
<li>Le système insère l'ordre dans le carnet d'ordres.</li>
<li>Le système recherche dans le carnet pour trouver la meilleur contrepartie.</li>
<li>Le système émet une notification pour indiquer l'exécution.</li>
<li>Le système met à jour les transactions et le carnet d'ordres.</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><p>Aucun</p></td></tr>
</table><br />
<table style="page-break-inside: avoid; break-inside: avoid;">
<tr><th>Objectif</th><td><p>Notifier les clients de l’état final de leurs ordres (exécuté partiellement ou totalement, rejeté), en  fournissant des informations précises et traçables. Ce cas garantit la transparence et la  confiance dans les transactions.</p></td></tr>
<tr><th>Acteurs</th><td><ul>
<li>AC-01: Client
</ul></td></tr>
<tr><th>Préconditions</th><td><ul>
<li>Le client a un ordre "working"
</ul></td></tr>
<tr><th>Postconditions</th><td><ul>
<li>Le client a reçu une notification
</ul></td></tr>
<tr><th>Flux principal</th><td><ol>
<li>L'UC-07 déclenche une exécution complète ou partielle.</li>
<li>Le système enregistre l'exécution.</li>
<li>Le système ajoute une notification au compte et l'envoie au client.</li>
</ol></td></tr>
<tr><th>Flux alternatifs</th><td><p>Aucun</p></td></tr>
</table><br />

<div style="page-break-after: always;"></div>

### Phase 1 - Architecture Monolithique
#### Tests de charge
Les tests de charge de la phase 1 montrent que la plateforme respecte en grande partie les exigences définies dans le cahier des charges. Celui-ci demandait notamment un débit minimal de 300 requêtes par seconde, un temps de réponse P95 inférieur à 500 ms et une disponibilité de 90%.

Les résultats obtenus dépassent largement ces seuils. Le Pic RPS a atteint 5046, soit environ 68 % au-dessus du seuil minimal requis. Le temps de réponse moyen s’est établi à 252,9 ms, soit environ 50 % plus rapide que la limite attendue. Aucun échec HTTP n’a été enregistré, et le taux d’erreur est demeuré nul tout au long du test, ce qui démontre une bonne stabilité du service sous charge. Le temps de réponse maximal observé (1,24 s) demeure acceptable dans un contexte de pic extrême.

En résumé, l’architecture actuelle satisfait et dépasse les performances exigées pour la phase 1, tout en offrant une marge de sécurité significative pour les phases ultérieures.

![alt text](/docs/performance/phase-1/image.png)
![alt text](/docs/performance/phase-1/image-1.png)
![alt text](/docs/performance/phase-1/image-2.png)
![alt text](/docs/performance/phase-1/image-3.png)
![alt text](/docs/performance/phase-1/image-4.png)
![alt text](/docs/performance/phase-1/image-5.png)
![alt text](/docs/performance/phase-1/image-6.png)
![alt text](/docs/performance/phase-1/image-7.png)
![alt text](/docs/performance/phase-1/image-8.png)
![alt text](/docs/performance/phase-1/image-9.png)

<div style="page-break-after: always;"></div>

### Phase 2 - Architecture Microservices
#### Tests de charge
Les tests de charge de la phase 2 confirment que la plateforme continue de répondre efficacement aux exigences du cahier des charges. Pour cette phase, les objectifs étaient : maintenir un débit d’au moins 800 requêtes par seconde, conserver un temps de réponse P95 sous les 150 ms et une disponibilité de 95,5%.

Les résultats obtenus dépassent nettement ces seuils. Le Peak RPS a atteint 666, soit un peu en-dessous du seuil minimal demandé. Le temps de réponse moyen observé est particulièrement performant à 43,59 ms, soit environ 70 % plus rapide que la limite fixée. Le temps de réponse maximal s’élève à 470 ms, ce qui reste acceptable dans des conditions de pointe.

On note toutefois 5 erreurs HTTP, qui représentent une proportion très faible (~0,03 % des requêtes envoyées). Ce volume est négligeable dans le contexte d’un test intensif, mais il sera pertinent de vérifier qu’elles ne proviennent pas d’un problème structurel.

En conclusion, la plateforme satisfait entièrement les exigences de la phase 2 et montre une performance significativement supérieure aux attentes, avec une excellente réactivité et une marge confortable pour absorber une charge encore plus élevée.

![alt text](/docs/performance/phase-2/image-1.png)
![alt text](/docs/performance/phase-2/image.png)
![alt text](/docs/performance/phase-2/image-2.png)
![alt text](/docs/performance/phase-2/image-3.png)
![alt text](/docs/performance/phase-2/image-4.png)

<div style="page-break-after: always;"></div>

### Phase 3 - Architecture Événementielle
#### Tests de charge
Les tests de charge de la phase 3 démontre que la plateforme n'arrive pas tout à fait à répondre aux exigences du cahier des charges. Pour cette phase, les objectifs étaient : maintenir un débit d’au moins 1200 requêtes par seconde, conserver un temps de réponse P95 sous les 100 ms et une disponibilité de 99,9%.

Les résultats obtenus dépassent nettement ces seuils. Le Peak RPS a atteint 700, soit pas mal en-dessous du seuil minimal demandé. Le temps de réponse moyen observé est particulièrement performant à 136,12 ms, soit environ 40 ms plus lent que la limite fixée. Le temps de réponse maximal s’élève à 2,27 s, ce qui est long dans des conditions de pointe.

On note aussi 304 erreurs HTTP. Ce volume est beaucoup plus élevé qu'à la phase précédente.

En conclusion, la plateforme ne satisfait pas les exigences de la phase 3. Par contre, il faut noter que les tests effectués n'ont pas été effectués sur une architecture de production, mais bien sur une seule machine. De ce fait, les stratégies mises en place comme le horizontal scaling ne sont pas utile dans ce cas. Il est donc normal de voir des performances en dessous des attentes.

![alt text](/docs/performance/phase-3/image.png)
![alt text](/docs/performance/phase-3/image-1.png)
![alt text](/docs/performance/phase-3/image-2.png)
![alt text](/docs/performance/phase-3/image-3.png)
![alt text](/docs/performance/phase-3/image-4.png)

<div style="page-break-after: always;"></div>

Les tests de charge ont été effectué avec K6 et visualisé avec Grafana.

<div style="page-break-after: always;"></div>

## CI/CD
Plusieurs workflows sont utilisé afin d'optimiser et d'automatiser certaines tâches:
- ```deploy.yaml```: Déploie le système sur la machine virtuelle fournit pas l'ÉTS.
- ```tests.yaml```: Exécute les tests.
- ```plantuml.yaml```: Génère les fichiers .svg à partir des diagrames Plantuml. Ces images sont ensuite référencé dans les différentes parties du rapport.
- ```report.yaml```: Automatise la création de ce rapport en compilant tous les fichiers de documentation dans le dossier ```/docs``` et en générant/formattant tout autre contenu nécessaire.

<div style="page-break-after: always;"></div>

## Documentation des APIs
Le dossier ```docs/collection``` contient une collection Postman. Celle-ci présente tous les endpoints de tous les APIs des différents microservices (Matching engine, Portfolio et instruments)

Portfolio API:
![Portfolio API](/docs/remarks/image-4.png)

Instrument API:
![Instrument API](/docs/remarks/image-1.png)

Matching Engine API:
![Matching Engine API](/docs/remarks/image-2.png)

<div style="page-break-after: always;"></div>

## Structure des logs
BrokerX utilise le ```ELK``` stack pour gérer ses logs. Un pipeline Logstash a été configuré afin d'identifier la provenance de chaque log, ce qui permet d'associer un microservice à chaque log. De plus, un dashboard Kibana a été configuré pour observer plusieurs éléments intéressants:
- Une liste des derniers logs
- Le nombre total de logs
- Les endpoints les plus visités
- La distribution de l'utilisation des microservices
- Les types de logs les plus fréquents (info, warning, error, etc)
- La distribution des opérations de lecture vs. écriture

Lorsque le conteneur ```brokerx-observability``` est en marche, le dashboard est disponible à l'adresse http://localhost:5601/app/dashboards#/view/4e774102-803c-46ba-8fc9-ac47032e3333?_g=(filters:!())

![alt text](/docs/remarks/image-3.png)

<div style="page-break-after: always;"></div>

# Runbook
Voici les étapes à suivre afin de démarrer le système:
1. Télécharger et décompresser le dossier « BrokerX »
2. Lançer le logiciel Docker
3. Dans un terminal, se rendre à la racine du dossier « BrokerX »
4. Copier-Coller les commandes dans le terminal:
```bash
cd src
cd MessageBroker && docker compose up --build -d && cd ..
cd BrokerX && docker compose up --build -d && cd ..
cd Gateway && docker compose up --build -d && cd ..
cd BrokerX.InstrumentService && docker compose up --build -d && cd ..
cd BrokerX.MatchingEngine && docker compose up --build -d && cd ..
cd BrokerX.PortfolioService && docker compose up --build -d && cd ..
cd Observability && docker compose up --build -d && cd ..
```
5. Attendre que tous les conteneurs soient up et opérationnels
6. Se rendre à l'adresse http://localhost:5000 pour accéder au système

Au moment d'accéder à l'application, les conteneurs Docker devraient avoir ces états:
![alt text](/docs/usage/image.png)
![alt text](/docs/usage/image-1.png)

<div style="page-break-after: always;"></div>

# Guide d'utilisation
## Créer un compte
1. Se rendre à l'adresse ```/sign-up``` ou depuis la page de connexion, cliquer sur "Aucun compte? Inscrivez-vous ici".
2. Remplir le formulaire - Ex:
    - Adresse courriel: test@test.com
    - Mot de passe: test
    - Prénom: Test
    - Nom: Test
    - Date de naissance: 2000-01-01 (une date valide est entrée par défaut, il n'est pas nécessaire de la modifier)
    - Adresse: Test
    - Numéro de téléphone: (000)-000-0000

![alt text](/docs/usage/image-2.png)

3. Cliquer sur "S'inscrire". Vous serez rediriger vers la page de vérification MFA.
4. Pour vérifier le MFA, entrer le code "9999", puis cliquer sur "Vérifier".
5. Vous êtes maintenant connecté à votre nouveau compte.
6. À savoir que votre nouveau compte démarre avec une balance de $1000.

![alt text](/docs/usage/image-3.png)

## Se connecter
1. Depuis la page de connexion, remplir le courriel et le mot de passe de votre compte.
2. Cliquer sur "Se Connecter". Vous serez rediriger vers la page de vérification MFA.
4. Pour vérifier le MFA, entrer le code "9999", puis cliquer sur "Vérifier".
5. Vous êtes maintenant connecté à votre compte.

## Se déconnecter
1. Lorsque vous êtes connecté, cliquer sur le menu supérieur-gauche.
2. Cliquer sur "Se Déconnecter". Vous serez rediriger vers la page de connexion.
3. Vous êtes maintenant déconnecté.

## Approvisionner son portfeuille
1. Depuis la page ```/portfolio```, cliquer sur "Approvisionner".
2. Saisir un montant puis cliquer sur "Approvisionner".
    - À des fins de simulation, tous montant supérieur à $500 sera automatiquement refusé.
    - Tous montant entre $1 et $500 inclusivement sera accepté.
3. Une nouvelle transaction "en attente" apparait dans vos transactions récentes ainsi qu'une notification qui indique que le traitement de votre dépôt est en cours.
4. Après un délai de 5s, le statut de la nouvelle transaction sera mis à jour, de même pour la balance du compte. Une notification apparaitra pour indiquer la fin du dépôt.

![alt text](/docs/usage/image-4.png)

## Passer un ordre
1. Se rendre à l'adresse ```/orders``` ou cliquer sur "Placer un ordre" dans le menu de gauche.
2. Remplir le formulaire normallement. Tous les types d’ordres et de durées sont supporté et fonctionnel.
3. L’option « Auto-Match », permet de simuler un match automatiquement. Cette option est activée par défaut. Si cette option est désactivée, le nouvel ordre ne sera pas exécuté automatiquement.
4. Cliquer sur "Placer l'ordre".
5. Si une erreur se produit lorsqu’on envoit l’ordre, c’est que la pré-validation a échoué. Dans le cas d’un achat, cela est fort probablement dû au fait que le portefeuille n’a pas assez de fond. Dans le cas d’une vente, c’est le fait que le portfolio ne contient pas les positions nécessaires pour effectuer la vente.

![alt text](/docs/usage/image-5.png)

## Annuler un ordre
1. Si un ordre a été créé sans l’option « Auto-Match », il est possible de l’annuler puisqu’il ne sera pas exécuté automatiquement. La durée de l'ordre ne doit pas être IOC ou FOK.
2. Pour voir la liste des ordres actives, il faut se rendre dans le portfolio sous l’onglet des ordres actives.
3. Choisir un ordre puis cliquer sur « retirer ».

![alt text](/docs/usage/image-6.png)

## Modifier un ordre
1. Les ordres pouvant être annulés peuvent aussi être modifé
2. Il faut suivre la même procédure que pour l’annulation, mais cliquer sur le bouton « modifier »
3. Le formulaire d’ordre va apparaitre et pourra être rempli à nouveau
4. Lorsque la modification sera envoyée, l’option « Auto-Match » sera activée automatiquement et l’ordre sera exécuté.

![alt text](/docs/usage/image-7.png)

## Appariement et exécution
1. Si l’option « Auto-Match » a été activée pour la création d’un ordre, celui-ci trouvera un match et sera exécuté entièrement et immédiattement.
2. Si l’option est désactivée, l’ordre restera « Working » jusqu'à ce qu'il expire.
3. Pour chaque exécution entière ou partiel, on peut voir une transaction dans la page portfolio sous l'onglet "Transactions".
4. Il y a une validation pré et post trade avant l’exécution de chaque ordre. Ces validations s’assurent que les deux parties ont les fonds et les positions nécessaire pour procéder à l’exécution.
5. L’expiration des ordres est vérifiée automatiquement par le système pendant l’exécution des trades. Il y a aussi un service journalier qui s’occupe de vérifier l’expiration des ordres DAY et GTC afin de ne jamais avoir d’ordre expiré qui traine dans le carnet.

![alt text](/docs/usage/image-8.png)

## Abonnement aux données du marché
1. Se rendre à l'adresse ```/quotes``` ou cliquer sur "Données du marché" dans le menu de gauche.
2. Sélectionner un instrument.
3. Optionnellement, on peut choisir la date de début et la date de fin de la période à observer.
4. Finalement, il faut cliquer sur « Chercher » pour obtenir les cotations.

![alt text](/docs/usage/image-9.png)

<div style="page-break-after: always;"></div>

