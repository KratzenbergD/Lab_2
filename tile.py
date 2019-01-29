import pygame


class Tile(pygame.sprite.Sprite):

     def __init__(self, imageSurf, coord):
         super().__init__()
         self.image = imageSurf
         self.rect = self.image.get_rect()
         self.rect.topleft = coord