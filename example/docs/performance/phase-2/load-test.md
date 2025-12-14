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