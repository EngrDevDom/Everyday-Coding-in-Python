background_image_filename = 'jennie.jpg'

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("i♥Jennie")

background = pygame.image.load(background_image_filename).convert()

while True:

      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  exit()

            screen.blit(background, (0,0))

            pygame.display.update()
