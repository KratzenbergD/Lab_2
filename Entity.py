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

    def __init__(self, sprite_img):
        super().__init__()
        self.image = pygame.Surface((default_size, default_size))
        self.sprite_img = pygame.image.load(sprite_img)
        self.sprite_img = pygame.transform.scale(self.sprite_img, (default_size, default_size))
        self.image.set_colorkey(pygame.color.THECOLORS['black'])
        self.rect = self.image.get_rect()
        self.prevPos = vec(400, 400)
        self.position = vec(400, 400)
        self.rect.center = (int(self.position.x),int(self.position.y))
        self.velocity = vec(0, 0)
        self.lateral_accel = vec(3, 0.0)  # accel vector pointing to the right
        self.vertical_accel = vec(0.0, -3)  # accel vector pointing upward
        self.max_speed = 10
        self.debug = False

    def toggleDebug(self):
        """ This method toggles debug mode
            for the Entity."""
        self.debug = not self.debug

    def move(self, keys, dt):
        """ This is the generic movement method used by Entities.
            Will most likely be overridden in derived classes."""
        hasMoved = False
        movedHorizontal = False
        movedVertical = False
        if keys[pygame.K_w]:
            self.velocity += self.vertical_accel * dt
            movedVertical = True
        if keys[pygame.K_s]:
            self.velocity -= self.vertical_accel * dt
            movedVertical = True
        if keys[pygame.K_d]:
            self.velocity += self.lateral_accel * dt
            movedHorizontal = True
        elif keys[pygame.K_a]:
            self.velocity -= self.lateral_accel * dt
            movedHorizontal = True


        # if the entity is not currently moving, decrease their velocity until it reaches 0
        if movedHorizontal or movedVertical:
            self.prevPos = self.position

            # self.velocity.length() returns the Euclidean length of the vector
            if self.velocity.length() > self.max_speed:
                self.velocity.scale_to_length(self.max_speed)

            self.position += self.velocity
            self.rect.center = (int(self.position.x),int(self.position.y))

        if not movedHorizontal:
            self.velocity.x /= 50
            if abs(self.velocity.x) < 0.1:
                self.velocity.x = 0

        if not movedVertical:
            self.velocity.y /= 50
            if abs(self.velocity.y) < 0.1:
                self.velocity.y = 0

    def update(self, keys, dt):
        """ The generic Entity update method.
            Will most likely be overridden by derived classes."""
        self.move(keys, dt)

    def handleCollision(self):
        """ The generic collision detection method.
            The Entity's previous position is stored
            so that they can be moved back in the event
            of a wall collision."""
        ### CANNOT WALLSLIDE PERFECTLY

        self.position = self.prevPos - self.velocity
        self.velocity.x = 0
        self.velocity.y = 0
        self.rect.center = (int(self.position.x), int(self.position.y))

    def draw(self, win, cameraPos):
        """ The generic Entity draw method.
            Will definitely be overridden in derived classes."""
        self.image.fill(pygame.color.THECOLORS['black'])
        self.image.blit(self.sprite_img, (0, 0))
        if self.debug:
            pygame.draw.rect(self.image, pygame.color.THECOLORS['red'], (0, 0, self.rect.w, self.rect.h), 1)
        win.blit(self.image, (self.rect.left - cameraPos[0],self.rect.top - cameraPos[1],self.rect.w,self.rect.h))



