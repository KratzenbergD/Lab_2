# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *


class Player(Entity):
    """ This class handles all things
        player-related."""

    def __init__(self, max_hp):
        super().__init__()
        self.max_hp = max_hp
        self.cur_hp = self.max_hp

    def draw(self):
        """ The Player draw class.
            Things like HP bar, Player sprite, etc.
            will be handled here."""
        super().draw()
