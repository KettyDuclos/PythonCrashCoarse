import pygame
from settings import Setting
from rocket import Ship
import game_functions as gf


def run_game():
    #initialize the pygame, settings and create a screen object.
    pygame.init()
    rs_settings = Setting()
    screen = pygame.display.set_mode(
        (rs_settings.screen_width, rs_settings.screen_height))
    pygame.display.set_caption("Rocket Invasion")

    #Make a ship.
    ship = Ship(screen)

    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(rs_settings, screen, ship)

run_game()
