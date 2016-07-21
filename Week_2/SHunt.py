import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.draw.line(screen,RED,[100,200],[200,300],1)


