import pygame

class Fighter():
    def __init__(self,player,x,y,flip,data,spritesheet,animation_list,sound):
        self.player = player
        self.size = data[0]
        self.scale = data[1]
        self.offset = data[2]
        self.flip =  flip
        self.animationlist = self.load_images(spritesheet,animation_list)
        self.action = 0 #0 = idle, 1 = run, 2 = jumping, 3 = attack1, 4 = attack2 , 5 = hit, 6 = death
        self.frame_index = 0
        self.image = self.animationlist[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x,y,100,210)
        self.vel_y =0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.hit = False
        self.health = 100
        self.alive = True



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


    def move(self, Screen_Width, Screen_Height, surface,target, round_over):
        Speed =10
        Gravity = 1
        dx = 0
        dy = 0
        self.running = False
        self.attack_type =0

        # Get the keys that are pressed
        key = pygame.key.get_pressed()

        #can only move if not attacking
        if self.attacking == False and self.alive == True and round_over == False:
            # check player 1 movement
            if self.player == 1:
            #movement
                if key[pygame.K_a]:
                    self.running = True
                    dx = -Speed
                if key[pygame.K_d]:
                    self.running = True
                    dx = Speed
                #jumping
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_s] or key[pygame.K_e]:
                    self.attack(target)
                    #determine which attack is used
                    if key[pygame.K_s]:
                        self.attack_type = 1
                    if key[pygame.K_e]:
                        self.attack_type = 2
            # check player 2 movement
            if self.player == 2:
            #movement
                if key[pygame.K_LEFT]:
                    self.running = True
                    dx = -Speed
                if key[pygame.K_RIGHT]:
                    self.running = True
                    dx = Speed
                #jumping
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_DOWN] or key[pygame.K_RETURN]:
                    self.attack(target)
                    #determine which attack is used
                    if key[pygame.K_DOWN]:
                        self.attack_type = 1
                    if key[pygame.K_RETURN]:
                        self.attack_type = 2


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
        if self.rect.bottom +dy > Screen_Height -155:
            dy = Screen_Height - 155 - self.rect.bottom
            self.vel_y = 0
            self.jump = False

        #ensure the fighter is facing the right direction
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -=5
        #update the rectangle position
        self.rect.x +=dx
        self.rect.y +=dy

    def update_animation(self):
        #check what action the player is doing
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)#death
        elif self.hit == True:
            self.update_action(5)#hit
        elif self.attacking == True:
            if self.attack_type == 1:#attack 1
                self.update_action(3)
            elif self.attack_type == 2:#attack 2
                self.update_action(4)
        elif self.jump == True:
            self.update_action(2)#jump
        elif self.running == True:
            self.update_action(1)#run
        else:
            self.update_action(0)#idle
        animation_cooldown = 50
        self.image = self.animationlist[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index +=1
        #if the animation has run out then reset
        if self.frame_index >= len(self.animationlist[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animationlist[self.action]) -1
            else:
                self.frame_index = 0

                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 100
                self.attack_type = 0
                #check if damage has been taken
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 100
                    self.update_action(0)

    def attack(self,target):

        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_sound.play()
            attacking_rect = pygame.Rect(self.rect.centerx -(2 * self.rect.width* self.flip),self.rect.y,2*self.rect.width,self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True

    def update_action(self,new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def draw(self,surface):
        img = pygame.transform.flip(self.image,self.flip,False)
        surface.blit(img,(self.rect.x - (self.offset[0]*self.scale),self.rect.y - (self.offset[1]*self.scale)))