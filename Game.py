import pygame
from Map import *
from config import *
from EventManager import *
class Game:
    def __init__(self):
        """Initialize game variables"""
        self.clock = pygame.time.Clock()
        self.map = Map('map.txt', 'images/ProjectUtumno_full.png', screen_size)
        self.running = False
        self.window = pygame.display.set_mode(screen_size)
        self.player = Entity()
        self.bg_color = (0,0,0)
        self.event_manager = EventManager()
        self.event_manager.addGameObject(self.player)

    def startGame(self):
        self.running = True

    def stopGame(self):
        self.running = False

    def runGameLoop(self):
        while self.running:
            # UPDATES
            dt = self.clock.tick(60) / 1000.0

            # USER INPUT
            self.event_manager.process_menu_input()


            #Game Input
            self.event_manager.process_input(dt)

            #GAME UPDATE

            # DRAWING
            self.window.fill(self.bg_color)
            self.map.draw(self.window)
            self.player.draw(self.window)
            pygame.display.flip()