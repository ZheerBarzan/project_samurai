import pygame

# Initialize the game
pygame.init()

# Set up the screen
Screen_Width = 1500
Screen_Height = 1000

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Samurai Showdown")

#load background image
background = pygame.image.load('assets/images/background/background.png').convert_alpha()

#function for drawing the background
def draw_background():
    scaled_background = pygame.transform.scale(background, (Screen_Width, Screen_Height))
    screen.blit(scaled_background, (0, 0))

# Set up the game loop
run = True
while run:
    draw_background()
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update the display
    pygame.display.update()


pygame.quit()


