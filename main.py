import pygame
from pygame import mixer
from fighter import Fighter

# Initialize the game
mixer.init()
pygame.init()

# Set up the screen
Screen_Width = 1500
Screen_Height = 1000

#define colors
White = (255,255,255)
Yellow = (255,255,0)
Red = (255,0,0)

# define game variables
intro_count =3
last_count_update = pygame.time.get_ticks()
score= [0,0]
round_over = False
Round_over_cooldown = 5000


#define fighter variables
Samurai_size = 200
Samurai_sacle =5
Samurai_offset = [95,80]
Samurai_data = [Samurai_size,Samurai_sacle,Samurai_offset]

ninja_size = 200
ninja_sacle =5
ninja_offset = [85,85]
ninja_data = [ninja_size,ninja_sacle,ninja_offset]

#load music and sounds

pygame.mixer.music.load('assets/audio/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0,5000)
katana = pygame.mixer.Sound('assets/audio/katana.wav')
katana.set_volume(0.5)
kunai = pygame.mixer.Sound('assets/audio/sword.wav')
kunai.set_volume(0.5)


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

victory_image = pygame.image.load('assets/images/background/victory.png').convert_alpha()



samurai_animation = [8,8,2,6,6,4,6]
ninja_animation = [4,8,2,4,4,3,7]

#define font
count_font = pygame.font.Font("assets/fonts/PressStart2P.ttf", 150)
score_font = pygame.font.Font("assets/fonts/PressStart2P.ttf", 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


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
fighter_1 = Fighter(1,200, 640,False,Samurai_data,samurai,samurai_animation,katana)
fighter_2 = Fighter(2,1200, 640,True,ninja_data,ninja,ninja_animation,kunai)
# Set up the game loop
run = True
while run:
    clock.tick(fps)
    #draw the background
    draw_background()
    #draw health bars
    draw_health_bars(fighter_1.health, 50, 100)
    draw_health_bars(fighter_2.health, 950, 100)
    #draw the score
    draw_text('Samurai: ' + str(score[0]), score_font, Red, 100, 50)
    draw_text('Ninja: ' + str(score[1]), score_font, Red, 1100, 50)

    if intro_count <=0:
        # move fighters
        fighter_1.move(Screen_Width, Screen_Height, screen, fighter_2, round_over)
        fighter_2.move(Screen_Width, Screen_Height, screen, fighter_1, round_over)
    else:
        # display count timer
        draw_text(str(intro_count), count_font, Red, (Screen_Width//2) - 50, (Screen_Height//2) - 50)
        if (pygame.time.get_ticks() - last_count_update) > 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()


    #update fighters
    fighter_1.update_animation()
    fighter_2.update_animation()
    # Draw the fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        if fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        screen.blit(victory_image, (Screen_Width//2 - 200, 200))
        if pygame.time.get_ticks() - round_over_time > Round_over_cooldown:
            fighter_1 = Fighter(1, 200, 640, False, Samurai_data, samurai, samurai_animation, katana)
            fighter_2 = Fighter(2, 1200, 640, True, ninja_data, ninja, ninja_animation, kunai)
            round_over = False
            intro_count = 3
            last_count_update = pygame.time.get_ticks()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update the display
    pygame.display.update()


pygame.quit()


