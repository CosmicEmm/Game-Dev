import pygame
from pygame.locals import *


size = width, height = (800, 800) # Unpacking the tuple into width and height of the screen
road_w = int(width/1.6) # Set road width to 500 pixels (800/1.6), also convert the resulting floating point to an integer

# Initialize the pygame application
pygame.init()
running = True
# Set window size
screen = pygame.display.set_mode(size)
# Set title
pygame.display.set_caption('Hot Wheels')
# Set background color
screen.fill((20,50,20)) # (red, green, blue)
pygame.draw.rect(
    screen,               # Drawing surface
    (50, 50, 50),         # Color: Dark Grey
    (width/2 - road_w/2,  # x-coordinate: Centered horizontally
     0,                   # y-coordinate: Starts at the top of the screen
     road_w,              # Width of the rectangle
     height)              # Height of the rectangle (full screen height)
)
# Apply the changes on the screen
pygame.display.update()

 
while running:
    for event in pygame.event.get(): # The get method fetches all the events (e.g., keyboard input, mouse clicks, window close)
        if event.type == QUIT: # QUIT: the user clicks the close button (x) to execute pygame.quit()
            running = False
        if event.type == KEYDOWN:
            K_ESCAPE   # The user presses the esc key to execute pygame.quit() - also works in fullscreen mode
            running = False


# Collapse the application window
pygame.quit()