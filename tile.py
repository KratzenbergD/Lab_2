import pygame


class Tile(pygame.sprite.Sprite):
    """ This class handles information
        about each individual Tile in the map."""

    def __init__(self, imageSurf, coord, world_coordinates):
        super().__init__()
        self.image = imageSurf
        self.rect = self.image.get_rect()
        self.rect.topleft = coord
        self.debug = False
        self.word_coordinates = world_coordinates
        self.world_rect = pygame.Rect(world_coordinates,(self.rect.w,self.rect.h))


    def collide_rect(self,otherRect):
        return self.world_rect.colliderect(otherRect)

    def toggleDebug(self):
        """ Toggles the debug flag, which signals
            whether to draw debug information to
            the game screen."""
        self.debug = not self.debug

    def draw(self,win):
        win.blit(self.image,self.rect)
        if self.debug:
            pygame.draw.rect(win, pygame.color.THECOLORS['red'], self.rect,1)



