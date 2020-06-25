# File  :   Vector_movement.py
# Desc  :   Using Vectors for Time-Based Movement

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector import Vector

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector(100.0, 100.0)
speed = 250
heading = Vector()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            destination = Vector(*event.pos) - (Vector(*sprite.get_size())/2)
            heading = Vector.from_positions(position, destination)
            heading.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (position.x, position.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
