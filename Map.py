# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

from maploader import loadMap
import pygame
from config import *
from tile import Tile
from Enemy import *


class Map:
    """ This class generates a tile-based map
        from a Flare text file created in the
        Tiled program."""

    def __init__(self, file_name, image_name, screen_res):
        """ Param: file_name is a string containing the name of
                   the Flare text file with the map data"""

        parsed = loadMap(file_name)             # returns map containing header data, tileset data, and layer data
        self.header_data = parsed['header']         # keys: width , height, tilewidth, tileheight, background_color
        self.tile_sets_data = parsed['tileset']     # fname,tile_width,tile_height,gap_x,gap_y
        self.layer_data = parsed['layers']          # array of multidimensional arrays for layer data
        self.currentScene = None                    # contains a list of active sprites
        self.totalMapWidth = self.header_data['width'] * self.header_data['tilewidth']
        self.totalMapHeight = self.header_data['height'] * self.header_data['tileheight']
        self.sprite_sheet = pygame.image.load(image_name)
        self.tiles_wide = self.sprite_sheet.get_width() // self.header_data['tilewidth']
        self.tiles_high = self.sprite_sheet.get_height() // self.header_data['tileheight']
        r,g,b,a = tuple(self.header_data['background_color']) if 'background_color' in self.header_data.keys() else (0,0,0,255)
        self.bg_color = pygame.Color(r, g, b, a)
        self.boundary = pygame.Rect(0,0,self.totalMapWidth,self.totalMapHeight)
        tilewidth = self.header_data['tilewidth']
        tileheight = self.header_data['tileheight']
        gap_x = self.tile_sets_data[3]
        gap_y = self.tile_sets_data[4]
        self.enemy_list = pygame.sprite.Group()

        for i in range(len(self.layer_data)):
            layer = self.layer_data[i]
            for y in range(len(layer)):
                col = layer[y]
                for x in range(len(col)):
                    tilecode = col[x]
                    if tilecode in ENEMY_SPRITES:
                        source_x = (tilecode) % self.tiles_wide
                        source_y = (tilecode) // self.tiles_wide
                        top_x = (source_x * tilewidth + source_x * gap_x)
                        top_y = source_y * tileheight + source_y * gap_y
                        enemyImage = pygame.Surface((tilewidth, tileheight))

                        enemyImage.blit(self.sprite_sheet, (0, 0),
                                       pygame.Rect(top_x, top_y, tilewidth, tileheight))
                        enemyImage.set_colorkey(self.bg_color)
                        enemy = Enemy(enemyImage)
                        enemy.placeEnemy((x*tilewidth+enemy.rect.w/2),(y*tileheight + enemy.rect.h/2))
                        self.layer_data[i][y][x] = 0
                        self.enemy_list.add(enemy)
