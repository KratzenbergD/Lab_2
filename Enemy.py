# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *


class Enemy(Entity):
    """ This class handles all things
        enemy-related."""

    def __init__(self, max_hp):
        super().__init__()
        self.max_hp = max_hp
        self.cur_hp = self.max_hp

    def move(self, keys, dt):
        pass

    def update(self, keys, dt):
        self.move(keys, dt)
