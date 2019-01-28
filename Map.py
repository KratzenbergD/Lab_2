# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O

from maploader import loadMap
from Entity import Entity
import pygame

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
        self.sprite_sheet = pygame.image.load(image_name)
        self.tiles_wide = self.sprite_sheet.get_width() // self.header_data['tilewidth']
        self.tiles_high = self.sprite_sheet.get_height() // self.header_data['tileheight']
        r,g,b,a = tuple(self.header_data['background_color']) if 'background_color' in self.header_data.keys() else (0,0,0,255)
        self.bg_color = pygame.Color(r,g,b,a)
        self.player = Entity()  # Testing Entity class

    def draw(self,screen):
        tile_width = self.tile_sets_data[1]
        tile_height = self.tile_sets_data[2]
        gap_x = self.tile_sets_data[3]
        gap_y = self.tile_sets_data[4]
        screen.fill(self.bg_color)
        layer = self.layer_data[2]       #iterate through each layer in our map
        for y in range(len(layer)):     #iterate through each row in our map
            row = layer[y]
            for x in range(len(row)):
                index = row[x]
                if index:
                    source_x = (index-1) % self.tiles_wide
                    source_y = index // self.tiles_wide
                    top_x = source_x*tile_width + source_x*gap_x
                    top_y = source_y*tile_height + source_y*gap_y
                    screen.blit(self.sprite_sheet,(x*tile_height,y*tile_width),pygame.Rect(top_x,top_y,tile_width,tile_height))
                    self.player.draw((800, 600), screen)    # draw and update Entity in game loop