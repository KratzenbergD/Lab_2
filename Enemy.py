# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *


class Enemy(Entity):
    """ This class handles all things
        enemy-related."""

    def __init__(self, sprite_img):
        super().__init__(sprite_img)
        self.max_hp = 10
        self.cur_hp = self.max_hp

    def move(self, keys, dt):
        pass

    def update(self, keys, dt):
        self.move(keys, dt)
