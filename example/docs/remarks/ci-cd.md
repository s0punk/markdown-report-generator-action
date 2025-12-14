## CI/CD
Plusieurs workflows sont utilisé afin d'optimiser et d'automatiser certaines tâches:
- ```deploy.yaml```: Déploie le système sur la machine virtuelle fournit pas l'ÉTS.
- ```tests.yaml```: Exécute les tests.
- ```plantuml.yaml```: Génère les fichiers .svg à partir des diagrames Plantuml. Ces images sont ensuite référencé dans les différentes parties du rapport.
- ```report.yaml```: Automatise la création de ce rapport en compilant tous les fichiers de documentation dans le dossier ```/docs``` et en générant/formattant tout autre contenu nécessaire.