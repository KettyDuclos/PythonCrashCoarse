import pygame

class Avatar():

    def __init__(self, screen):
        """Initialize the avatar and set its starting position"""
        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('image.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)




