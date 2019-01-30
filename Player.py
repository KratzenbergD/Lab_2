# Names: Jon Munion, Daniel Kratzenberg
# ETGG1802-01
# Lab 2: File I/O


from Entity import *


class Player(Entity):
    """ This class handles all things
        player-related."""

    def __init__(self, sprite_img):
        super().__init__(sprite_img)
        self.max_hp = 20
        self.cur_hp = self.max_hp
        self.hp_bar_width = 80
        self.hp_rect = pygame.rect.Rect(10, 10, self.hp_bar_width, 15)
        self.hp_rect_frame = pygame.rect.Rect(10, 10, self.hp_bar_width, 15)

    def draw(self, win):
        """ The Player draw method.
            Things like HP bar, Player sprite, etc.
            will be handled here."""
        super().draw(win)
        pygame.draw.rect(win, (0, 0, 255), self.hp_rect)
        pygame.draw.rect(win, (255, 255, 255), self.hp_rect_frame, 2)

    def update(self, keys, dt):
        """ The Player update method.
            Things like Player movement, changes to
            Player HP, etc. will be handled here."""
        super().update(keys, dt)

        ### FOR TESTING PURPOSES ONLY
        if keys[pygame.K_q]:
            self.take_damage()
        elif keys[pygame.K_e]:
            self.restore_hp()

    def take_damage(self):
        """ This method decrements the Player's
            current hp."""
        if self.cur_hp > 0:
            self.cur_hp -= 1
            self.hp_rect.width = (self.cur_hp / self.max_hp) * self.hp_bar_width

    def restore_hp(self):
        """ This method restores the Player;s
            current hp."""
        if self.cur_hp < self.max_hp:
            self.cur_hp += 1
            self.hp_rect.width = (self.cur_hp / self.max_hp) * self.hp_bar_width
