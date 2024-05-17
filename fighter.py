import pygame

class Fighter():
    def __init__(self,x,y,data,spritesheet,animation_list):
        self.size = data[0]
        self.scale = data[1]
        self.offset = data[2]

        self.flip = False
        self.animationlist = self.load_images(spritesheet,animation_list)
        self.action = 0 #0 = idle, 1 = run, 2 = jumping, 3 = attack1, 4 = attack2 , 5 = hit, 6 = death
        self.frame_index = 0
        self.image = self.animationlist[self.action][self.frame_index]
        self.rect = pygame.Rect(x,y,40,60)
        self.vel_y =0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100



    def load_images(self,spritesheet,animation_steps):
        animation_list = []
        for y,animation in enumerate(animation_steps):

            temp_img_list = []
            for x in range(animation):
                temp_img = spritesheet.subsurface(pygame.Rect(x*self.size,y*self.size,self.size,self.size))
                pygame.transform.scale(temp_img,(self.size*self.scale,self.size*self.scale))
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.scale,self.size*self.scale))
)
            animation_list.append(temp_img_list)
        return animation_list


    def move(self, Screen_Width, Screen_Height, surface,target):
        Speed =10
        Gravity = 1
        dx = 0
        dy = 0

        # Get the keys that are pressed
        key = pygame.key.get_pressed()

        #can only move if not attacking
        if self.attacking == False:

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
                self.attack(surface,target)
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

        #ensure the fighter is facing the right direction
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        self.rect.x +=dx
        self.rect.y +=dy

    def attack(self,surface,target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx -(2 * self.rect.width* self.flip),self.rect.y,2*self.rect.width,self.rect.height)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(self.image,(self.rect.x - (self.offset[0]*self.scale),self.rect.y - (self.offset[1]*self.scale)))