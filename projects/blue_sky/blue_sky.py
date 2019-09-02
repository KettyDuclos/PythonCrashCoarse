import sys
import pygame
from avatar import Avatar

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    bg_color = (0, 0, 255)

    #Make an Avatar
    avatar = Avatar(screen)


    #Start the main loop for the game.
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        

        #Redraw the screen during each pass through the loop
        screen.fill(bg_color)
        avatar.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

run_game()