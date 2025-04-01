import pygame
from case import Case
from game import Game
from random import randint

x_case, y_case = 0,0
while (x_case < 1 or x_case > 27) and (y_case < 1 or y_case > 15):
    x_case, y_case = int(input("Entrer le nombre de case en x")), int(input("Entrer le nombre de case en y"))   

pygame.init()
screen = pygame.display.set_mode((50*x_case,50*y_case))
pygame.display.set_caption("Démineur")  # Titre de la fenêtre
pygame.display.set_icon(pygame.image.load("image/bombe.png")) #Icone de la fenetre
all_case = pygame.sprite.Group()
def grille(x_case, y_case, pourcentage):
    x = 0
    y = 0
    for i in range(y_case):
        for i in range(x_case):
            if randint(1, 101) < pourcentage:
                all_case.add(Case(x, y, True))
            else:
                all_case.add(Case(x, y, False))
            x += 50
        y += 50
        x = 0 
    pygame.display.flip()

def calcul_bombe(all_case, case):
    decalage = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0),  (1, 1)]
    for dx, dy in decalage:
        x = case.x_id + dx
        y = case.y_id + dy
        for i_case in all_case:
            if i_case.x_id == x and i_case.y_id == y:
                if i_case.bombe:
                    case.compteur += 1
        


pourcentage = int(input("Entrer le pourcentage de mine (ex : 20)"))
grille(x_case, y_case, pourcentage)
compteur_nul = 0
for i in all_case:
    calcul_bombe(all_case, i)
    if i.compteur == 0 and not i.bombe:
        compteur_nul += 1
compteur_nul = randint(0, compteur_nul)
for i in all_case:
    if compteur_nul > 0:
        if i.compteur == 0:
            compteur_nul -= 1
    elif i.compteur == 0 and not i.bombe:
        i.marque = True
        break
game = Game(screen, all_case)
game.run()
pygame.quit()
