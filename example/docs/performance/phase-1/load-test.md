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