# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *


class Enemy(Entity):
    """ This class handles all things
        enemy-related."""

    def __init__(self, sprite_img):
        super().__init__(sprite_img)
        self.max_hp = 10
        self.cur_hp = self.max_hp
        self.aggro_rect = pygame.rect.Rect(self.rect.left - 200, self.rect.top - 200, 400, 400)

        #self.rect = pygame.rect.Rect(self.world_rect)

    def move(self, keys, dt):
        """ Enemy will remain stationary until player
            approaches close enough to trigger movement."""

    def handleCollision(self):
        super().handleCollision()
        print("Close enough to aggro")

    def update(self, keys, dt):
        self.move(keys, dt)

    def draw(self, win, cameraPos):
        super().draw(win, cameraPos)
        win.blit(self.image, (self.rect.left - cameraPos[0], self.rect.top - cameraPos[1], self.rect.w, self.rect.h))
        screenRect = pygame.Rect(
            self.aggro_rect.left - cameraPos[0],
            self.aggro_rect.top - cameraPos[1],
            self.aggro_rect.w,
            self.aggro_rect.h
        )
        pygame.draw.rect(win,pygame.color.THECOLORS['red'],screenRect,1)
