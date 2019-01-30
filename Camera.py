import pygame
from config import *
from tile import *

class Camera():

    def __init__(self,map):
        self.pos = (0,0)
        self.map = map
        self.tileWidth = map.tile_sets_data[1]
        self.tileHeight = map.tile_sets_data[2]
        self.layers = map.layer_data
        r, g, b, a = tuple(map.header_data['background_color']) if 'background_color' in map.header_data.keys() else (
        0, 0, 0, 255)
        self.bg_color = pygame.Color(r, g, b, a)
        self.focusedTiles = pygame.sprite.Group()
        self.focusedWalls = pygame.sprite.Group()

    def setCameraPosition(self,playerPos):
        """Updates camera position based on location of player"""

        topLeftX = playerPos[0] - (screen_size[0] >> 1)
        topLeftY = playerPos[1] - (screen_size[1] >> 1)

        if topLeftX + screen_size[0] > self.map.totalMapWidth:
            topLeftX = self.map.totalMapWidth - screen_size[0]

        if topLeftX < 0:
            topLeftX = 0

        if topLeftY + screen_size[1] > self.map.totalMapHeight:
            topLeftY = self.map.totalMapHeight - screen_size[1]

        if topLeftY < 0:
            topLeftY = 0

        self.pos = (topLeftX, topLeftY)
        print(self.pos)
        #possibly only call this when the player has moved enough to scroll
        self.updateMap()

    def updateMap(self):
        tile_width = self.map.tile_sets_data[2]
        tile_height = self.map.tile_sets_data[3]
        map_width = self.map.header_data['width']
        map_height = self.map.header_data['height']
        col = self.pos[0] // tile_width
        row = self.pos[1] // tile_height

        num_tiles_x = screen_size[0] // tile_width
        num_tiles_y = screen_size[1] // tile_height

        x_offset = self.pos[0] % tile_width
        y_offset = self.pos[1] % tile_height

        #x_offset and y_offset need to be handled
        for layer in self.map.layer_data:
            for y_index in range(row,row+num_tiles_y):
                if y_index >= 0 and y_index < map_height:
                    row = layer[y_index]
                    for x_index in range(col,col+num_tiles_x):
                        if x_index >= 0 and x_index < map_width:
                            tile_code = row[x_index]
                            print(tile_code)


    def draw(self,screen):
        screen.fill(self.bg_color)

        #self.tileSprites.draw(screen)
        for sprite in self.focusedTiles.sprites():
            sprite.draw(screen)