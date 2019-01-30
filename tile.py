import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, imageSurf, coord):
        super().__init__()
        self.image = imageSurf
        self.rect = self.image.get_rect()
        self.rect.topleft = coord
        self.debug = False

    def toggleDebug(self):
        self.debug = not self.debug

    def draw(self,win):
        win.blit(self.image,self.rect)
        if self.debug:
            pygame.draw.rect(win, pygame.color.THECOLORS['red'], self.rect,1)



