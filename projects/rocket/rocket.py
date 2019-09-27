import pygame
import sys
from rocket_ship import Ship

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 400))
    pygame.display.set_caption("Rocket Invasion")

    #Make a rocket_ship
    ship = Ship(screen)

    #store bg color
    bg_color = (230,230,230)


    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #game navigation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move ship to the right
                    ship.rect.centerx += 1
                if event.key == pygame.K_LEFT:
                    #move ship to the left
                    ship.rect.centerx -= 1
                if event.key == pygame.K_UP:
                    #move ship up
                    ship.rect.top -= 1
                if event.key == pygame.K_DOWN:
                    ship.rect.bottom += 1


        
        
        #Redraw the screen during each pass through the loop
        screen.fill(bg_color)
        ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
