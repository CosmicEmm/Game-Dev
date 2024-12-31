import pygame
from pygame.locals import *


# initializing the pygame application
pygame.init()
running = True
screen = pygame.display.set_mode((800, 800)) # Method Args: (width, height)

while running:
    for event in pygame.event.get(): # fetching all events from the pygame.event module with the get method and iterating over them
        if event.type == QUIT:
            running = False


# collapsing the application window
pygame.quit()