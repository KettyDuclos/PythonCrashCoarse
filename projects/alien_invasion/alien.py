import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_settings, screen, ship):

         super(Bullet, self).__init__()
        self.screen = screen