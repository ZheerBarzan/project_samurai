import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,60)

    def move(self):
        Speed =10
        dx = 0
        dy = 0

        # Get the keys that are pressed
        key = pygame.key.get_pressed()
        #movement
        if key[pygame.K_a]:
            dx = -Speed
        if key[pygame.K_d]:
            dx = Speed

        self.rect.x +=dx
        self.rect.y +=dy
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)