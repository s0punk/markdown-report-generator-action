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