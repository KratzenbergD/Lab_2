# Names: Jon Munion
# ETGG1802-01
# Lab 2: File I/O

import pygame
import os
from Map import *

# Initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen_size = (800, 600)
bg_color = pygame.color.THECOLORS['black']
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Test Map")
clock = pygame.time.Clock()
map = Map('map.txt','images/ProjectUtumno_full.png',screen_size)

while True:
    # UPDATES
    dt = clock.tick(60) / 1000.0

    # USER INPUT

    e = pygame.event.poll()

    if e.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    # DRAWING
    window.fill(bg_color)
    map.draw(window)
    pygame.display.flip()
