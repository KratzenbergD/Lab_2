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

    def turnOnDebugMode(self):
        for obj in self.game_objects['game_objects']:
            obj.toggleDebug()

    def process_input(self, dt):
        """ This method processes user input."""
        keys = pygame.key.get_pressed()
        temp = None
        # initialize game_pad to None
        game_pad = None

        # check to see if any game pads are connected
        if pygame.joystick.get_count() > 0:
            game_pad = pygame.joystick.Joystick(0)
            # 360 pad buttons: 0 = 'A', 1 = 'B', 2 = 'X', 3 = 'Y'
            #                : 4 = 'LB', 5 = 'RB', 6 = 'Back', 7 = 'Start'
            #                : 8 = 'L3', 9 = 'R3'

        if game_pad is not None:
            temp = [x for x in keys]
            # check horizontal axis on left analog stick
            if game_pad.get_axis(0) < -0.25:
                temp[pygame.K_a] = True
            elif game_pad.get_axis(0) > 0.25:
                temp[pygame.K_d] = True

            # check vertical axis on left analog stick
            if game_pad.get_axis(1) < -0.25:
                temp[pygame.K_w] = True
            elif game_pad.get_axis(1) > 0.25:
                temp[pygame.K_s] = True

            # check status of buttons
            if game_pad.get_button(0):
                # fill out later
                pass
            if game_pad.get_button(1):
                pass
            if game_pad.get_button(2):
                pass
            if game_pad.get_button(3):
                pass
            if game_pad.get_button(5):
                pass
            if game_pad.get_button(6):
                pass
            if game_pad.get_button(7):
                pass
            if game_pad.get_button(8):
                pass
            if game_pad.get_button(9):
                pass

            keys = tuple(temp)

        for key in self.game_objects:
            list = self.game_objects[key]
            for obj in list:
                obj.update(keys, dt)

    def process_menu_input(self):
        e = pygame.event.poll()

        if e.type == pygame.QUIT:
            return False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                return False
            elif e.key == pygame.K_F1:
                self.turnOnDebugMode()

        return True
