import pygame

class Case(pygame.sprite.Sprite):
    def __init__(self, x_d, y_d, bombe):
        super().__init__()
        self.marque = False
        self.bombe = bombe
        self.x = x_d
        self.x_id = int(x_d / 50)
        self.y = y_d
        self.y_id = int(y_d / 50)
        self.compteur = 0
        self.reveal = True
        self.drapeau = False
        self.image_drapeau = pygame.image.load("image/drapeau.png")
        if self.bombe:
            self.image = pygame.image.load("image/bombe.png")
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)

    def reveal_all(self, all_case):
        self.marque = False
        self.reveal = False
        contours = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for dx, dy in contours:
            x = self.x_id + dx
            y = self.y_id + dy
            for case in all_case:
                if x == case.x_id and y == case.y_id and case.reveal:
                    if case.compteur != 0:
                        case.reveal = False
                    elif case.compteur == 0:
                        case.reveal_all(all_case)
                

    def draw(self, screen, font, color):
        if not self.reveal:
            if self.bombe:
                screen.blit(self.image, self.rect)
            else:
                text = font.render(str(self.compteur),1, color[self.compteur])
                screen.blit(text, (self.x + 15, self.y + 10))
        else:
            if self.drapeau:
                screen.blit(self.image_drapeau, self.rect)
        pygame.draw.rect(screen, "gray" if not self.marque else "red", (self.x, self.y, 50, 50), 2)