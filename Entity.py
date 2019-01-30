# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

import pygame
import random
from config import *
vec = pygame.math.Vector2


class Entity(pygame.sprite.Sprite):
    """ This is the base class from which
        Game Entities(Player, Enemy, Etc.)
        inherit from."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((default_size,default_size))
        self.image.set_colorkey(pygame.color.THECOLORS['black'])
        self.color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)
                 )
        self.rect = self.image.get_rect()
        self.position = vec(400, 400)
        self.velocity = vec(0, 0)
        self.lateral_accel = vec(1, 0.0)  # accel vector pointing to the right
        self.vertical_accel = vec(0.0, -1) # accel vector pointing upward
        self.max_speed = 1
        self.debug = False

    def toggleDebug(self):
        self.debug = not self.debug

    def move(self, keys, dt):

        hasMoved = False
        if keys[pygame.K_w]:
            self.velocity += self.vertical_accel * dt
            hasMoved = True
        elif keys[pygame.K_s]:
            self.velocity -= self.vertical_accel * dt
            hasMoved = True
        if keys[pygame.K_d]:
            self.velocity += self.lateral_accel * dt
            hasMoved = True
        if keys[pygame.K_a]:
            self.velocity -= self.lateral_accel * dt
            hasMoved = True

        # if the entity is not currently moving, decrease their velocity until it reaches 0
        if not hasMoved:
            self.velocity.x -= self.velocity.x / 20
            self.velocity.y -= self.velocity.y / 20
            if self.velocity.x > -0.1:
                if self.velocity.x < 0.1:
                    self.velocity.x = 0
            if self.velocity.y > -0.1:
                if self.velocity.y < 0.1:
                    self.velocity.y = 0


        # self.velocity.length() returns the Euclidean length of the vector
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.position += self.velocity
        self.rect.center = (int(self.position[0]),int(self.position[1]))

    def update(self, keys, dt):
        self.move(keys, dt)

        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255)
                      )

    def handleCollission(self, wallSprite):
        ### NOT WORKING AS INTENDED YET ###
        #HAVING VERTICAL AND HORIZONTAL VELOCITY AT THE SAME TIME PRODUCES UNEXPECTED RESULTS

        diff_x = wallSprite.rect.center[0] - self.rect.
        # moving right
        if wallSprite.rect.center[0] - self.rect.center[0] > 0 and self.velocity.x > 0:
            self.rect.right = wallSprite.rect.left
            self.position.x = self.rect.center[0]
            self.velocity.x = 0

        # moving left
        elif wallSprite.rect.center[0] - self.rect.center[0] < 0 and self.velocity.x < 0:
            self.rect.left = wallSprite.rect.right
            self.position.x = self.rect.center[0]
            self.velocity.x = 0

        # moving up
        if self.rect.center[1] - wallSprite.rect.center[1] > 0 and self.velocity.y < 0:
            self.velocity.y = 0
            self.rect.top = wallSprite.rect.bottom
            self.position.y = self.rect.center[1]

        # moving down
        elif self.rect.center[1] - wallSprite.rect.center[1] < 0 and self.velocity.y > 0:
            self.velocity.y = 0
            self.rect.bottom = wallSprite.rect.top
            self.position.y = self.rect.center[1]

    def draw(self, win):
        self.image.fill(pygame.color.THECOLORS['black'])
        pygame.draw.circle(self.image, self.color, (default_size // 2, default_size // 2), default_size//2)
        if self.debug:
            pygame.draw.rect(self.image, pygame.color.THECOLORS['red'], (0,0,self.rect.w,self.rect.h),1)
        win.blit(self.image, self.rect)
