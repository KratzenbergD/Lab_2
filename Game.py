import pygame
from Map import *
from config import *
from EventManager import *
from Entity import *
from Player import *
from Camera import *


class Game:
    """ This class contains the main game loop."""
    def __init__(self):
        """Initialize game variables"""
        self.clock = pygame.time.Clock()
        self.map = Map('Maps/test_map5.txt', 'images/ProjectUtumno_full.png', screen_size)
        self.running = False
        self.window = pygame.display.set_mode(screen_size)
        self.player = Player('images/star.png')
        self.bg_color = (0,0,0)
        self.event_manager = EventManager()
        self.event_manager.addGameObject(self.player)
        self.camera = Camera(self.map)

    # def addMapTiles(self):
    #     """ This method adds map tile objects to
    #         the event_manager's object list"""
    #     for sprite in self.map.wallSprites.sprites():
    #         self.event_manager.addGameObject(sprite)

    def startGame(self):
        """ Sets the running flag to True, signaling
            the game loop to start."""
        self.running = True

    def stopGame(self):
        """ Sets the running flag to False, signaling
            the game loop to stop."""
        self.running = False

    def runGameLoop(self):
        """ This method handles the main game loop."""
        while self.running:
            # UPDATES
            dt = self.clock.tick(60) / 1000.0

            # USER INPUT
            self.running = self.event_manager.process_menu_input()

            if self.running:
                #GAME UPDATE

                # Game Input
                self.event_manager.process_input(dt)

                #Collision Detection
                for sprite in self.camera.focusedWalls.sprites():
                    if sprite.collide_rect(self.player.rect):
                        self.player.handleCollision()

                #Make Camera Follow the Player
                self.camera.setCameraPosition(self.player.getPos())



                # DRAWING
                self.window.fill(self.bg_color)
                self.camera.draw(self.window)
                self.player.draw(self.window,self.camera.pos)
                pygame.display.flip()