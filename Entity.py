# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

import pygame
import random
import math
from config import *
vec = pygame.math.Vector2


class Entity(pygame.sprite.Sprite):
    """ This is the base class from which
        Game Entities(Player, Enemy, Etc.)
        inherit from."""

    def __init__(self, sprite_img):
        super().__init__()
        self.image = None
        if type(sprite_img) is str:
            self.image = pygame.Surface((default_size, default_size))
            self.sprite_img = pygame.image.load(sprite_img)
        else:
            self.image = sprite_img
            self.sprite_img = sprite_img

        self.sprite_img = pygame.transform.scale(self.sprite_img, (default_size, default_size))
        self.image.set_colorkey(pygame.color.THECOLORS['black'])
        self.rect = self.sprite_img.get_rect()
        self.prevPos = vec(400, 400)
        self.position = vec(400, 400)
        self.rect.center = (int(self.position.x),int(self.position.y))
        self.velocity = vec(0, 0)
        self.lateral_accel = vec(10, 0.0)  # accel vector pointing to the right
        self.vertical_accel = vec(0.0, -10)  # accel vector pointing upward
        self.max_speed = 10
        self.debug = False
        self.isStuck = False

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

    def handleCollision(self,otherRect):
        """ The generic collision detection method.
            The Entity's previous position is stored
            so that they can be moved back in the event
            of a wall collision."""
        ### CANNOT WALLSLIDE PERFECTLY GETS STUCK IN CORNER
        if self.velocity.length() == 0:
            return
        # Walk back a step
        tempPos = self.prevPos
        tempPos -= self.velocity

        wallPushVector = -self.velocity

        validLocation = self.rect.copy()
        validLocation.center = (int(tempPos.x), int(tempPos.y))

        while otherRect.colliderect(validLocation):
            tempPos += wallPushVector
            validLocation.center = (int(tempPos.x), int(tempPos.y))

        validX, validY = tempPos
        tempRect = validLocation.copy()

        tempRect.center = (int(validX + self.velocity.x), int(validY))

        if otherRect.colliderect(tempRect):
            self.velocity.x = 0
        else:
            validX = tempRect.center[0]

        tempRect.center = (int(validX), int(validY + self.velocity.y))

        if otherRect.colliderect(tempRect):
            self.velocity.y = 0
        else:
            validY = tempRect.center[1]

        self.rect.center = (validX, validY)
        self.position = vec(validX, validY)

        # self.position = self.prevPos
        # self.position -= self.velocity
        # self.velocity = vec(0,0)
        #
        # self.rect.center = (int(self.position.x),int(self.position.y))

    def boundsCheck(self,worldBoundary):
        boundedRect = self.rect.clamp(worldBoundary)
        bX,bY = boundedRect.center
        self.rect = boundedRect

        if bX != int(self.position.x):
            self.position.x = bX
            self.velocity.x = 0

        if bY != int(self.position.y):
            self.position.y = bY
            self.velocity.y = 0

    def draw(self, win, cameraPos):
        """ The generic Entity draw method.
            Will definitely be overridden in derived classes."""
        self.image.fill(pygame.color.THECOLORS['black'])
        self.image.blit(self.sprite_img, (0, 0))
        if self.debug:
            pygame.draw.rect(self.image, pygame.color.THECOLORS['red'], (0, 0, self.rect.w, self.rect.h), 1)
        win.blit(self.image, (self.rect.left - cameraPos[0],self.rect.top - cameraPos[1],self.rect.w,self.rect.h))

    def noLongerStuck(self):
        self.isStuck = False


