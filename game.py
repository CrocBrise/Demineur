import pygame

class Game():
    def __init__(self, screen, all_case):
        self.font = pygame.font.Font(None, 54)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.all_case = all_case
        self.time = 0
        self.running = True
        self.color = {
            8 : "black",
            7 : "black",
            6 : "black",
            5 : "black",
            4 : "purple",
            3 : "red",
            2 : "blue",
            1 : "green",
            0 : "white"
        }
    
    

    def handlings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for case in self.all_case:
                        if case.rect.collidepoint(event.pos):
                            if case.bombe:
                                case.reveal = False
                                self.running = False
                            if case.reveal:
                                if case.compteur != 0:
                                    case.reveal = False
                                else:
                                    if case.compteur == 0:
                                        case.reveal_all(self.all_case)
                elif event.button == 3:
                    for case in self.all_case:
                        if case.rect.collidepoint(event.pos):
                            if case.drapeau:
                                case.drapeau = False
                            else:
                                case.drapeau = True
                            
                                

    def update(self):
        pass

    def display(self):
        self.screen.fill((169, 169, 169))
        for case in self.all_case:
            case.draw(self.screen, self.font, self.color)
        pygame.display.flip()

    def run(self):
        
        while self.running:
            self.handlings_events()
            self.update()
            self.display()
            self.clock.tick(100)
            self.time += 1