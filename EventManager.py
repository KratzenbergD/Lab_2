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
        self.joySticks = []

        # check to see if any game pads are connected
        for x in range(0,pygame.joystick.get_count()):
            game_pad = pygame.joystick.Joystick(x)
            game_pad.init()
            print(game_pad.get_name())
            self.joySticks.append(game_pad)

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

        # check to see if any game pads are connected
        if len(self.joySticks):
            # 360 pad buttons: 0 = 'A', 1 = 'B', 2 = 'X', 3 = 'Y'
            #                : 4 = 'LB', 5 = 'RB', 6 = 'Back', 7 = 'Start'
            #                : 8 = 'L3', 9 = 'R3'
            #   Axes:
            #               0 - left joystick x axis    (1 = right, -1 = left)
            #               1 - left joystick y axis    (1 = right, -1 = left)
            #               2 - right joystick x axis   (1 = right, -1 = left)
            #               3 - right joystick y axis   (1 = right, -1 = left)
            #               4 - right trigger           (1 is pressed, -1 released) Initialized to 0
            #               5 - left trigger            (1 is pressed, -1 released) Initialized to 0
            #
            #   D-Pad:
            #         game_pad.get_hat(0) Tuple: (horizontal,vertical)
            #          (1,0) Right, (-1,0) Left
            #          (0,1) Up,    (0,-1) Down

            temp = [x for x in keys]
            for game_pad in self.joySticks:     #Maybe Handle Multiplayer in the future...


                D_PAD = game_pad.get_hat(0)

                if game_pad.get_axis(0) < -0.25 or D_PAD[0] < 0:
                    temp[pygame.K_a] = True
                elif game_pad.get_axis(0) > 0.25 or D_PAD[0] > 0:
                    temp[pygame.K_d] = True

                #for axis in range(game_pad.get_numaxes()):
                    #print(axis, " ", game_pad.get_axis(axis))

                for hat in range(game_pad.get_numhats()):
                    print(hat, " ", game_pad.get_hat(hat))

                # check vertical axis on left analog stick
                if game_pad.get_axis(1) < -0.25 or D_PAD[1] > 0:
                    temp[pygame.K_w] = True
                elif game_pad.get_axis(1) > 0.25 or D_PAD[1] < 0:
                    temp[pygame.K_s] = True

                for i in range(game_pad.get_numbuttons()):
                    if(game_pad.get_button(i)):
                        print(str(i) + " Pressed")
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
