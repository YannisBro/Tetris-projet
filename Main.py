# Crée par Yannis Bronnec et Gaya Slimani.

import pygame
import random


espace = pygame.image.load("fond.jpg")

# Définition de la couleur des diffÃ©rents bloc

couleur = [
    (0, 0, 0),
    (37, 253, 233),
    (225, 14, 141),
    (225, 56, 113),
    (247, 255, 0),
    (96, 255, 84),
    (255, 15, 239),
]

# DÃ©finition de la forme des diffÃ©rentes figures et leur rotation


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]]]

    def __init__(self, x, y):
        self.x = x # Position x
        self.y = y # Position y
        self.type = random.randint(0, len(self.figures) - 1) # Type de bloc
        self.color = random.randint(1, len(couleur) - 1) # Couleur du bloc
        self.rotation = 0 # Rotation du bloc

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type]) # Ajouter + 1 Ã  la variable rotation (donc changer la rotation)


class Tetris:
    level = 2 # DÃ©finir le difficultÃ© du niveau ( Vitesse de tombÃ© )
    score = 0 # Variable du score
    state = "start" # Le jeux commence sur "Start"
    x = 100 # Position x du tableau sur le fond
    y = 60  # Position y du tableau sur le fond
    zoom = 20 # Taille du tableau sur le fond
    figure = None # Pointeur de figure de base

    def __init__(self, height, width):
        self.height = height # Hauteur du tableau
        self.width = width # Largeur du tableau
        self.field = [] # Case vide du tableau
        self.score = 0 # DÃ©finition du score du 0
        self.state = "start" # On commence le jeux sur l'Ã©tat "Start"
        
        # CrÃ©ation du tableau tout les x hauteur et tout les x largeur
        
        for i in range(height):
            nouvelle_ligne = []
            for j in range(width):
                nouvelle_ligne.append(0)
            self.field.append(nouvelle_ligne)



    def new_figure(self):
        self.figure = Figure(3, 0)

    # Permet de savoir si le bloc qui flotte actuellement touche un bord ou un autre bloc
    
    def intersects(self):
        intersection = False # On se set sur False
        for i in range(4): # On vÃ©rifie si dans le tableau de 4x4 du bloc si il y a un champ non vide
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True # On se set sur True
        return intersection

# Quand une ligne est complète on la détruit

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j] 
        
        self.score += lines ** 2 # On rajoute 1 au score

    def go_space(self): 
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self): # Fait descendre la figure jusqu'a ce qu'il touche un objet et se freeze
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self): # Permet de figer le bloc sur le terrain qui devient donc un obstacle
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines() # regarde si on peut casser la ligne
        self.new_figure() # Fait appelle a une nouvelle figure
        if self.intersects():
            self.state = "gameover" # Si un bloc freeze touche un autre bloc freeze = game over

    def go_side(self, dx): # Pour dÃ©placer le bloc sur les cotÃ©s
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self): # Faire la rotation d'un bloc
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation # Si la rotation fait toucher un autre bloc on ne la rotate pas


# Initialise le jeux

pygame.init()

# Definition de couleur

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRIS = (128, 128, 128)
BLEU = (0,204,203)
CYAN = (169,234,254)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris Yannis et Gaya") # Nom de la fenÃªtre

# Boucle jusqu'a ce que l'utilisateur clique sur le bouton "quitter"

done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

# Faire descendre les bloc proportionellement au nombre d'fps

    if counter % (fps // game.level // 2) == 0 :
        if game.state == "start":
            game.go_down()

# DÃ©finition des touches de clavier pour les actions du jeux

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)


    if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pressing_down = False

    screen.blit(espace, (0, 0))

# Dessine le tableau de jeux

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRIS, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, couleur[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

# Dessine le bloc choisis

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, couleur[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

# DÃ©finition des diffÃ©rents texte

    font = pygame.font.SysFont('Comic Sans MS', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLEU)
    text_game_over = font1.render("Game Over", True, (BLEU))

    screen.blit(text, [150, 0]) # Afficher le score

# DÃ©finition du game over

    if game.state == "gameover": # On passe l'Ã©tat du jeux en mode game over
        screen.blit(text_game_over, [50, 200])



    pygame.display.flip() 
    clock.tick(fps) # Le nombre d'image par seconde

pygame.quit() # Pour quitter a fenetre de jeux
