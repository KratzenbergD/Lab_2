import pygame
from config import *
from tile import *
import math

class Camera():

    def __init__(self,map):
        self.pos = (0,0)
        self.prevPos = (0,0)
        self.map = map
        self.view = pygame.Surface(screen_size)
        self.rect = self.view.get_rect()
        self.tileWidth = map.header_data['width']
        self.tileHeight = map.header_data['height']
        self.layers = map.layer_data
        r, g, b, a = tuple(map.header_data['background_color']) if 'background_color' in map.header_data.keys() else (
        0, 0, 0, 255)
        self.bg_color = pygame.Color(r, g, b, a)
        self.focusedTiles = pygame.sprite.Group()
        self.focusedWalls = pygame.sprite.Group()

    def setCameraPosition(self,playerPos):
        """Updates camera position based on location of player"""

        topLeftX = playerPos[0] - (screen_size[0] / 2)
        topLeftY = playerPos[1] - (screen_size[1] / 2)
        if topLeftX + screen_size[0] > self.map.totalMapWidth:
            topLeftX = self.pos[0]

        if topLeftX < 0:
            topLeftX = 0

        if topLeftY + screen_size[1] > self.map.totalMapHeight:
            topLeftY = self.pos[1]

        if topLeftY < 0:
            topLeftY = 0


        self.pos = (topLeftX, topLeftY)
        #possibly only call this when the player has moved enough to scroll
        self.updateMapView()

        self.prevPos = self.pos

    def updateMapView(self):
        """Grabs tiles out of map and blits them to the camera viewing surface"""

        self.focusedWalls.empty()
        self.focusedTiles.empty()

        tile_width = self.map.tile_sets_data[1]
        tile_height = self.map.tile_sets_data[2]
        map_width = self.map.header_data['width']
        map_height = self.map.header_data['height']
        col = int(self.pos[0] / tile_width)
        row = int(self.pos[1] / tile_height)
        gap_x = self.map.tile_sets_data[3]
        gap_y = self.map.tile_sets_data[4]

        num_tiles_x = int(math.ceil(screen_size[0] / tile_width))
        num_tiles_y = int(math.ceil(screen_size[1] / tile_height))

        x_offset = int(self.pos[0]) % tile_width
        y_offset = int(self.pos[1]) % tile_height

        self.view.fill(self.bg_color)
        #x_offset and y_offset need to be handled y = -yo_offset, x = -x_offset
        y = -y_offset
        x = -x_offset
        for i in range(len(self.map.layer_data)):
            layer = self.map.layer_data[i]
            for y_index in range(row,int(row+num_tiles_y)):
                if y_index >= 0 and y_index < map_height-1:
                    current_row = layer[y_index]
                    for x_index in range(col,col + num_tiles_x):
                        if x_index >= 0 and x_index < map_width:
                            tile_code = current_row[x_index]
                            if tile_code:
                                source_x = (tile_code - 1) % self.map.tiles_wide
                                source_y = tile_code // self.map.tiles_wide
                                top_x = (source_x * tile_width + source_x * gap_x)
                                top_y = source_y * tile_height + source_y * gap_y
                                tileImage = pygame.Surface((tile_width, tile_height))
                                tileImage.blit(self.map.sprite_sheet, (0, 0),
                                               pygame.Rect(top_x, top_y, tile_width, tile_height))

                                screen_x = x_index*tile_width - self.pos[0]
                                screen_y = y_index*tile_width - self.pos[1]
                                tile = Tile(tileImage, (int(screen_x), int(screen_y)),(x_index*tile_width,y_index*tile_height))
                                self.view.blit(tile.image,tile.rect)
                                if tile_code in WALL_SPRITES:
                                    self.focusedWalls.add(tile)
                                self.focusedTiles.add(tile)
                        else:
                            break
                else:
                    break




    def draw(self,screen):
        for tile in self.focusedTiles.sprites():
            tile.draw(screen)
        #screen.blit(self.view,(0,0))
        #self.tileSprites.draw(screen)
        #for sprite in self.focusedTiles.sprites():
        #    sprite.draw(screen)