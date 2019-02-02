# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

from maploader import loadMap
import pygame
from config import *
from tile import Tile


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
        self.totalMapWidth = self.header_data['width'] * 32
        self.totalMapHeight = self.header_data['height'] * 32
        self.sprite_sheet = pygame.image.load(image_name)
        self.tiles_wide = self.sprite_sheet.get_width() // self.header_data['tilewidth']
        self.tiles_high = self.sprite_sheet.get_height() // self.header_data['tileheight']
        r,g,b,a = tuple(self.header_data['background_color']) if 'background_color' in self.header_data.keys() else (0,0,0,255)
    #    self.bg_color = pygame.Color(r,g,b,a)
    #     self.tileSprites = pygame.sprite.Group()
    #     self.wallSprites = pygame.sprite.Group()
    #     self.addSprites()
    #
    # def addSprites(self):
    #     """ This method adds all the map data into a
    #         Sprite group."""
    #     tile_width = self.tile_sets_data[1]
    #     tile_height = self.tile_sets_data[2]
    #     gap_x = self.tile_sets_data[3]
    #     gap_y = self.tile_sets_data[4]
    #     for i in range(1,len(self.layer_data)):
    #         layer = self.layer_data[i]
    #         for y in range(len(layer)):
    #             row = layer[y]
    #             for x in range(len(row)):
    #                 index = row[x]
    #                 if index:
    #                     source_x = (index - 1) % self.tiles_wide
    #                     source_y = index // self.tiles_wide
    #                     top_x = source_x * tile_width + source_x * gap_x
    #                     top_y = source_y * tile_height + source_y * gap_y
    #                     tileImage = pygame.Surface((tile_width,tile_height))
    #                     tileImage.blit(self.sprite_sheet, (0,0),
    #                                 pygame.Rect(top_x, top_y, tile_width, tile_height))
    #
    #                     tile = Tile(tileImage,(int(x*tile_width),int(y*tile_height)))
    #                     if index in WALL_SPRITES:
    #                         self.wallSprites.add(tile)
    #                     self.tileSprites.add(tile)
    #
    # def draw(self, screen):
    #     """ This method handles drawing each Tile
    #         contained in the Map's Tile list."""
    #     screen.fill(self.bg_color)
    #
    #     # self.tileSprites.draw(screen)
    #     for sprite in self.tileSprites.sprites():
    #         sprite.draw(screen)
