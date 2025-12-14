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