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
        if self.debug:
            pygame.draw.rect(self.image, pygame.color.THECOLORS['red'], (0,0,self.rect.w,self.rect.h),1)
        win.blit(self.image,self.rect)



