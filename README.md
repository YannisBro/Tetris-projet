## **Voici notre projet python : Tetris**

Tetris se joue sur un quadrillage, appelé la matrice, possédant une gravité (du haut vers le bas). Des formes géométriques, composées de quatre carrés, tombent depuis le haut de l'écran. Le joueur doit contrôler la chute de ces pièces :

    - En les déplaçant latéralement
    - En les faisant tourner sur elles-mêmes

Il n'est pas possible de ralentir la chute des pièces.

Le joueur doit ainsi empiler les pièces sur le bas de l'écran. Les pièces tombent une par une, et fusionnent avec le reste des pièces déjà tombées une fois parvenues en bas.

Le but du jeu est de former des lignes : lorsqu'un bloc termine une ou plusieurs lignes (occupant alors toute la largeur de la matrice), les lignes en question disparaissent. Les pièces se trouvant au-dessus de la ligne disparue sont alors décalées vers le bas. En complétant des lignes, on peut donc empêcher la pile de pièces d'atteindre le haut de l'écran : si cela se produit, la partie est alors terminée. 

____________________________________________________________________________________________________________________________________________________________

**Décomposition en sous problème :**

- Création des différentes formes de bloc
- Fonction permettant de supprimer une ligne quand elle est complète
- Pouvoir controler le bloc qui desend
- Choisir aléatoirement le bloc
- Créer une variable de score
- Modéliser le plateau de jeux
- Fonction pour la rotation des blocs

____________________________________________________________________________________________________________________________________________________________

**Minimum viable Product :**

- Création d'un plan de jeux et création des différents blocs
- Pouvoir gerer les mouvements des blocs (tourner, gauche, droite, descendre)
- Système de score
- Repèrer quand une ligne est complète et la supprimer

*Pour cela je vais utiliser pygame et la blibliothèque random avec des fonctions pour définir chaque bloc et leur mouvement*

à l'aide d'internet pour quelques fonctions
