import pygame
from settings import Settings

class Ship():

    def __init__(self, ai_settings, screen):
        """ initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the left center of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.rect.left

        self.center = float(self.rect.centery)

        #Moving flag
        self.moving_up = False
        self.moving_down = False
        
        

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.speed_factor
        
        self.rect.centery = self.center
        

    



    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)