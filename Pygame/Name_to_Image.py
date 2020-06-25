# File  :   Name_to_Image.py
# Desc  :   Writting your name to an Image file

import pygame

my_name = "Dominic Miralles"
pygame.init()
my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
pygame.image.save(name_surface, "jjj.jpg")