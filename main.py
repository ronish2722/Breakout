import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Breakout')

run=True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

pygame.quit()
