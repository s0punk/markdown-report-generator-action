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