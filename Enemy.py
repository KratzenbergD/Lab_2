# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *
import pygame
import math

class Enemy(Entity):
    """ This class handles all things
        enemy-related."""

    def __init__(self, sprite_img):
        super().__init__(sprite_img)
        self.max_hp = 10
        self.cur_hp = self.max_hp
        self.aggro_rect = pygame.Rect(0,0, 400, 400)
        self.aggro_rect.center = self.rect.center
        self.aggro_active = False
        self.heading = vec(0,0)
        self.speed = 2

        #self.rect = pygame.rect.Rect(self.world_rect)

    def placeEnemy(self,x,y):
        self.position.x = x
        self.position.y = y
        self.prevPos.x = x
        self.prevPos.y = y
        self.rect.center = (int(x),int(y))
        self.aggro_rect.center = self.rect.center

    def move(self, keys, dt):
        if self.heading.length() > 0:
            self.prevPos = self.position
            self.velocity = self.heading
            if self.velocity.length() > self.max_speed:
                self.velocity.scale_to_length(self.speed)
            self.position += self.velocity
            self.rect.center = (int(self.position.x), int(self.position.y))
            self.aggro_rect.center = self.rect.center

    def setHeading(self,playerPos):
        dy = playerPos[1] - self.position.y
        dx = playerPos[0] - self.position.x
        heading = math.atan2(dy,dx)
        chaseVector = vec(math.cos(heading),math.sin(heading))
        chaseVector.scale_to_length(self.speed)
        self.heading = chaseVector

    def chasePlayer(self, player):
        """ Enemy will remain stationary until player
            approaches close enough to trigger movement."""
        if self.aggro_active:
            # testing
            self.setHeading(player.getPos())
            #self.aggro_rect = pygame.rect.Rect(self.rect.left - 200, self.rect.top - 200, 400, 400)

    def activateAggro(self):
        self.aggro_active = True

    def deactivateAggro(self):
        self.aggro_active = False
        self.velocity = vec(0,0)
        self.heading = vec(0,0)

    def handleCollision(self,otherRect):
        self.heading = vec(0,0)
        super().handleCollision(otherRect)

    def update(self, keys, dt):
        self.move(keys, dt)

    def draw(self, win, cameraPos):
        super().draw(win, cameraPos)
        win.blit(self.image, (self.rect.left - cameraPos[0], self.rect.top - cameraPos[1], self.rect.w, self.rect.h))
        if self.debug:
            screenRect = pygame.Rect(
                self.aggro_rect.left - cameraPos[0],
                self.aggro_rect.top - cameraPos[1],
                self.aggro_rect.w,
                self.aggro_rect.h
            )
            pygame.draw.rect(win,pygame.color.THECOLORS['red'], screenRect, 1)
