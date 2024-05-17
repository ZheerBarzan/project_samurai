import pygame
from fighter import Fighter

# Initialize the game
pygame.init()

# Set up the screen
Screen_Width = 1500
Screen_Height = 1000

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Samurai Showdown")

#set frame rate
clock = pygame.time.Clock()
fps = 60

#load background image
background = pygame.image.load('assets/images/background/background.png').convert_alpha()

#function for drawing the background
def draw_background():
    scaled_background = pygame.transform.scale(background, (Screen_Width, Screen_Height))
    screen.blit(scaled_background, (0, 0))




# create 2 instances of the Fighter class
fighter_1 = Fighter(200, 770)
fighter_2 = Fighter(1200, 770)
# Set up the game loop
run = True
while run:
    clock.tick(fps)
    #draw the background
    draw_background()
    # move fighters
    fighter_1.move(Screen_Width, Screen_Height, screen, fighter_2)
    #fighter_2.move()
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


