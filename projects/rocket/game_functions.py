import sys
import pygame
from settings import Setting

rs_settings = Setting

def check_events(ship):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    ship.moving_down = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    ship.moving_down = False

def update_screen(rs_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(rs_settings.bg_color)
    ship.blitme()

    #make most recently drawn screen visible
    pygame.display.flip()

