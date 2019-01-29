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

    def move(self,keys, dt):

        if keys[pygame.K_w]:
            self.velocity += self.vertical_accel * dt
        elif keys[pygame.K_s]:
            self.velocity -= self.vertical_accel  * dt
        if keys[pygame.K_d]:
            self.velocity += self.lateral_accel * dt
        if keys[pygame.K_a]:
            self.velocity -= self.lateral_accel * dt


        # self.velocity.length() returns the Euclidean length of the vector
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.position += self.velocity
        self.rect.center = (int(self.position[0]),int(self.position[1]))

    def update(self, keys, dt):
        self.move(keys,dt)

        self.color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)
                 )



    def draw(self, win):
        pygame.draw.circle(self.image, self.color, (default_size // 2, default_size // 2), default_size//2)
        win.blit(self.image,self.rect)
