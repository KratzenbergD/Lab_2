# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


import pygame


class EventManager:
    """ This class processes all user input
        events."""
    def __init__(self):
        self.game_objects = {
            'game_objects':[],
            'game_windows':[],
        }

    def addGameObject(self, obj):
        self.game_objects['game_objects'].append(obj)

    def removeGameObject(self,obj):
        self.game_objects['game_objects'].remove(obj)

    def addGameWindow(self, obj):
        self.game_objects['game_windows'].append(obj)

    def removeGameWindow(self, obj):
        self.game_objects['game_windows'].remove(obj)

    def process_input(self, dt):
        """ This method processes user input."""
        keys = pygame.key.get_pressed()

        for key in self.game_objects:
            list = self.game_objects[key]
            for obj in list:
                obj.update(keys, dt)

    def process_menu_input(self):
        e = pygame.event.poll()

        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                self.stopGame()
