from tile import *
from config import *

class WarpTile(Tile):
    def __init__(self, imageSurf, coord, world_coordinates,tile_index):
        super().__init__(imageSurf, coord, world_coordinates)
        self.mapName = WARP_LOCATIONS[tile_index]
