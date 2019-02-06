# Names: Jon Munion
# ETGG1802-01
# Lab 2: File I/O

import pygame
import os
from Map import *
from Game import *

# Initialization
pygame.init()
pygame.joystick.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.display.set_caption("Test Map")


game = Game()
game.startGame()
game.runGameLoop()  #GamePlay Loop

pygame.quit()
exit()

