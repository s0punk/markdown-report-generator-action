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