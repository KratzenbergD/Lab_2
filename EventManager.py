# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


import pygame


class EventManager:
    """ This class processes all user input
        events."""
    def __init__(self):
        self.game_objects = []

    def process_input(self, dt):
        """ This method processes user input."""

        keys = pygame.key.get_pressed()

        for obj in self.game_objects:
            obj.update(keys, dt)
