import pygame
from tile import *
import random
from config import *

class PickUp(Tile):

    def __init__(self, imageSurf, coord, world_coordinates,collectable=None,amount=None):
        """Interactive chest, random amount of random collectable assigned if no values passed for collectable"""
        super().__init__(imageSurf, coord, world_coordinates)
        self.contents = collectable if collectable != None and amount != None else random.choice(list(COLLECTABLES.keys()))
        self.amount = amount if collectable != None and amount != None else random.randint(COLLECTABLES[self.contents][0],COLLECTABLES[self.contents][1])
        self.opened = False

    def updateMap(self,map):
        """Adds contents of interactive tile to player's inventory, then reveals it's opened/revealed version"""
        if not self.opened:
            col = int( self.world_rect.left / map.header_data['tilewidth'])
            row = int( self.world_rect.top / map.header_data['tileheight'])
            layerIndex = len(map.layer_data)-1
            while(layerIndex > 0):
                layer = map.layer_data[layerIndex]
                if(layer[row][col] > 1):
                    layer[row][col] = 0
                    break
                layerIndex -= 1
            for g in self.groups():
                g.remove(self)
