import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,60)
        self.vel_y =0
        self.jump = False
        self.attack_type = 0


    def move(self, Screen_Width, Screen_Height):
        Speed =10
        Gravity = 1
        dx = 0
        dy = 0

        # Get the keys that are pressed
        key = pygame.key.get_pressed()
        #movement
        if key[pygame.K_a]:
            dx = -Speed
        if key[pygame.K_d]:
            dx = Speed
        #jumping
        if key[pygame.K_w] and self.jump == False:
            self.vel_y = -30
            self.jump = True
        #attack
        if key[pygame.K_s] or key[pygame.K_e]:
            #determine which attack is used
            if key[pygame.K_s]:
                self.attack_type = 1
            if key[pygame.K_e]:
                self.attack_type = 2
            pass

        # add gravity
        self.vel_y += Gravity
        dy += self.vel_y

        # ensure the fighter is within the screen boundaries
        if self.rect.left +dx < 0:
            dx = -self.rect.left
        if self.rect.right +dx > Screen_Width:
            dx = Screen_Width - self.rect.right
        if self.rect.top +dy < 0:
            dy = -self.rect.top
            self.vel_y = 0
        if self.rect.bottom +dy > Screen_Height -130:
            dy = Screen_Height - 130 - self.rect.bottom
            self.vel_y = 0
            self.jump = False

        self.rect.x +=dx
        self.rect.y +=dy

    def attack(self):

    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)