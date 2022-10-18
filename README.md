## **Voici notre projet python : Tetris**

Tetris se joue sur un quadrillage, appelé la matrice, possédant une gravité (du haut vers le bas). Des formes géométriques, composées de quatre carrés, tombent depuis le haut de l'écran. Le joueur doit contrôler la chute de ces pièces :

    - En les déplaçant latéralement
    - En les faisant tourner sur elles-mêmes

Il n'est pas possible de ralentir la chute des pièces.

Le joueur doit ainsi empiler les pièces sur le bas de l'écran. Les pièces tombent une par une, et fusionnent avec le reste des pièces déjà tombées une fois parvenues en bas.

Le but du jeu est de former des lignes : lorsqu'un bloc termine une ou plusieurs lignes (occupant alors toute la largeur de la matrice), les lignes en question disparaissent. Les pièces se trouvant au-dessus de la ligne disparue sont alors décalées vers le bas. En complétant des lignes, on peut donc empêcher la pile de pièces d'atteindre le haut de l'écran : si cela se produit, la partie est alors terminée. 

____________________________________________________________________________________________________________________________________________________________

**Décomposition en sous problème :**
