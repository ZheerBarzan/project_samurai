import pygame
from fighter import Fighter

# Initialize the game
pygame.init()

# Set up the screen
Screen_Width = 1500
Screen_Height = 1000

#define colors
White = (255,255,255)
Yellow = (255,255,0)
Red = (255,0,0)

#define fighter variables
Samurai_size = 200
Samurai_sacle =5
Samurai_offset = [100,80]
Samurai_data = [Samurai_size,Samurai_sacle,Samurai_offset]

ninja_size = 200
ninja_sacle =5
ninja_offset = [50,110]
ninja_data = [ninja_size,ninja_sacle,ninja_offset]

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Samurai Showdown")

#set frame rate
clock = pygame.time.Clock()
fps = 60

#load background image
background = pygame.image.load('assets/images/background/background.png').convert_alpha()

#load the spritesheets
samurai = pygame.image.load('assets/images/samuraiMack/samurai.png').convert_alpha()
ninja = pygame.image.load('assets/images/kenji/ninja.png').convert_alpha()


samurai_animation = [8,8,2,6,6,4,6]
ninja_animation = [4,8,2,4,4,3,7]


#function for drawing the background
def draw_background():
    scaled_background = pygame.transform.scale(background, (Screen_Width, Screen_Height))
    screen.blit(scaled_background, (0, 0))

#health bar
def draw_health_bars(health,x,y):
    ratio = health/100
    #draw health bar
    pygame.draw.rect(screen, White, (x-10, y-10, 520, 70))
    pygame.draw.rect(screen, Red, (x, y, 500, 50))
    pygame.draw.rect(screen, Yellow, (x, y, 500*ratio, 50))
    pygame.draw.rect(screen, Yellow, (x, y, 500*ratio, 50))




# create 2 instances of the Fighter class
fighter_1 = Fighter(200, 770,False,Samurai_data,samurai,samurai_animation)
fighter_2 = Fighter(1200, 770,False,ninja_data,ninja,ninja_animation)
# Set up the game loop
run = True
while run:
    clock.tick(fps)
    #draw the background
    draw_background()
    #draw health bars
    draw_health_bars(fighter_1.health, 50, 100)
    draw_health_bars(fighter_2.health, 950, 100)
    # move fighters
    fighter_1.move(Screen_Width, Screen_Height, screen, fighter_2)


    #fighter_2.move(Screen_Width, Screen_Height, screen, fighter_1)

    #update fighters
    fighter_1.update_animation()
    fighter_2.update_animation()
    # Draw the fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update the display
    pygame.display.update()


pygame.quit()


