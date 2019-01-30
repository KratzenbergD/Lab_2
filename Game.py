import pygame
from Map import *
from config import *
from EventManager import *
class Game:
    def __init__(self):
        """Initialize game variables"""
        self.clock = pygame.time.Clock()
        self.map = Map('Maps/map.txt', 'images/ProjectUtumno_full.png', screen_size)
        self.running = False
        self.window = pygame.display.set_mode(screen_size)
        self.player = Entity()
        self.bg_color = (0,0,0)
        self.event_manager = EventManager()
        self.event_manager.addGameObject(self.player)
        self.addMapTiles()

    def addMapTiles(self):
        for sprite in self.map.wallSprites.sprites():
            self.event_manager.addGameObject(sprite)

    def startGame(self):
        self.running = True

    def stopGame(self):
        self.running = False

    def runGameLoop(self):
        while self.running:
            # UPDATES
            dt = self.clock.tick(60) / 1000.0

            # USER INPUT
            self.running = self.event_manager.process_menu_input()

            if self.running:
                #GAME UPDATE

                wallCollissions = pygame.sprite.spritecollide(self.player, self.map.wallSprites, False)
                if wallCollissions:
                    self.player.handleCollission()

                # Game Input
                self.event_manager.process_input(dt)

                # DRAWING
                self.window.fill(self.bg_color)
                self.map.draw(self.window)
                self.player.draw(self.window)
                pygame.display.flip()