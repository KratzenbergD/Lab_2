import pygame
from Map import *
from config import *
from EventManager import *
from Entity import *
from Player import *
from Camera import *
from Enemy import *


class Game:
    """ This class contains the main game loop."""
    def __init__(self):
        """Initialize game variables"""
        self.clock = pygame.time.Clock()
        self.current_map_name = "world"
        self.maps = {
            "world":Map('Maps/map0.txt', 'images/ProjectUtumno_full.png', screen_size),
            "shop": Map('Maps/map_shop.txt', 'images/ProjectUtumno_full.png', screen_size),
            "dungeon":Map('Maps/map_dungeon.txt', 'images/ProjectUtumno_full.png', screen_size),
        }

        self.current_map = self.maps[self.current_map_name]

        self.running = False
        self.window = pygame.display.set_mode(screen_size)
        self.player = Player('images/star.png')

        self.bg_color = (0,0,0)
        self.event_manager = EventManager()
        self.event_manager.addGameObject(self.player)
        self.camera = Camera(self.current_map)
        self.event_manager.addGameObject(self.camera)

        # feel free to move this to its own method or wherever, just using for testing
        for enemy in self.current_map.enemy_list.sprites():
            self.event_manager.addGameObject(enemy)

        self.warpCoordinates = {
            "world": [(self.player.position.x,self.player.position.y)],
            "shop": [(320,590),(1360,334)],
            "dungeon": [(2816,1600),(1440,1525)]
        }

    def startGame(self):
        """ Sets the running flag to True, signaling
            the game loop to start."""
        self.running = True

    def stopGame(self):
        """ Sets the running flag to False, signaling
            the game loop to stop."""
        self.running = False

    def collisionDetection(self):

        #boundary checking on world map
        self.player.boundsCheck(self.current_map.boundary)

        for enemy in self.current_map.enemy_list.sprites():
            if enemy.aggro_rect.colliderect(self.player.rect):
                enemy.activateAggro()
                enemy.chasePlayer(self.player)
            else:
                enemy.deactivateAggro()

        for wall in self.camera.focusedWalls.sprites():
            if self.player.rect.colliderect(wall.world_rect):
                self.player.handleCollision(wall.world_rect)
                break

        for wall in self.camera.focusedWalls.sprites():
            for enemy in self.current_map.enemy_list.sprites():
                if enemy.rect.colliderect(wall.world_rect):
                    enemy.handleCollision(wall.world_rect)
                    break

        for warpTile in self.camera.warpTiles.sprites():
            if self.player.rect.colliderect(warpTile.world_rect):
                if self.current_map_name == "world":
                    coords = self.warpCoordinates[warpTile.mapName][0]  # Warp To
                else:
                    coords = self.warpCoordinates[self.current_map_name][1]  # Warp From
                self.player.setPos(coords)
                self.camera.setMap(self.maps[warpTile.mapName])
                self.current_map = self.maps[warpTile.mapName]
                self.current_map_name = warpTile.mapName

        for interactable in self.camera.interactiveTiles.sprites():
            if self.player.rect.colliderect(interactable.world_rect):
                self.player.interact(interactable)
                interactable.updateMap(self.camera.map)


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
                self.collisionDetection()

                #Make Camera Follow the Player
                self.camera.setCameraPosition(self.player.getPos())

                # DRAWING
                self.window.fill(self.bg_color)
                self.camera.draw(self.window)
                self.player.draw(self.window,self.camera.pos)
                for enemy in self.current_map.enemy_list:
                    enemy.draw(self.window, self.camera.pos)
                pygame.display.flip()
