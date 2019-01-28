# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

import pygame
import random

vec = pygame.math.Vector2


class Entity:
    """ This is the base class from which
        Game Entities(Player, Enemy, Etc.)
        inherit from."""

    def __init__(self):
        self.position = vec(400, 400)
        self.velocity = vec(0, 0)
        self.lateral_accel = vec(0.005, 0.0)  # accel vector pointing to the right
        self.vertical_accel = vec(0.0, -0.005) # accel vector pointing upward
        self.max_speed = 0.025

    def update_pos(self, screen_size):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity += self.vertical_accel
        elif keys[pygame.K_s]:
            self.velocity -= self.vertical_accel
        if keys[pygame.K_d]:
            self.velocity += self.lateral_accel
        if keys[pygame.K_a]:
            self.velocity -= self.lateral_accel

        # self.velocity.length() returns the Euclidean length of the vector
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.position += self.velocity

    def draw(self, screen_size, win):
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)
                 )
        x = self.position.x
        y = self.position.y
        self.update_pos(screen_size)
        pygame.draw.circle(win,
                           color,
                           (int(x), int(y)),
                           10)
