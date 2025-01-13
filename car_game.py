import pygame
from pygame.locals import *


size = width, height = (800, 800) # Unpacking the tuple into width and height of the screen
road_w = int(width/1.6) # Set road width to 500 pixels (800/1.6), also convert the resulting floating point to an integer
roadmark_w = int(width/80) # Set roadmarking width to 10 pixels (800/80)

# Initialize the pygame application
pygame.init()
running = True
# Set window size
screen = pygame.display.set_mode(size)
# Set title
pygame.display.set_caption('Hot Wheels')
# Set background color
screen.fill((1, 115, 92)) # (red, green, blue)

# Graphics - Draw the road
pygame.draw.rect(
    screen,               # Drawing surface
    (50, 50, 50),         # Color: Dark Grey
    (width/2 - road_w/2,  # x-coordinate: Centered horizontally
     0,                   # y-coordinate: Starts at the top of the screen
     road_w,              # Width of the road
     height)              # Height of the road (full screen height)
)
#Draw the central yellowish road marking
pygame.draw.rect(
    screen,
    (255, 240, 60),           # Color: Yellow
    (width/2 - roadmark_w/2,  # x-coordinate: Centered horizontally
      0,                      # y-coordinate: Starts at the top of the screen
      roadmark_w,             # Width of the roadmark
      height)                 # Height of the roadmark
)
# Draw the white markings on both edges of the road
pygame.draw.rect( # left white marking
    screen,
    (255, 255, 255),                      # Color: White
    (width/2 - road_w/2 + roadmark_w * 2, # (width/2 - road_w/2) starts from the left edge of the road and (+ roadmark_w * 2) takes it 20 px away from that edge
      0,                                  # y-coordinate: Starts at the top of the screen
      roadmark_w,                         # Width of the roadmark
      height)                             # Height of the roadmark
)
pygame.draw.rect( # right white marking
    screen,
    (255, 255, 255),                      # Color: White
    (width/2 + road_w/2 - roadmark_w * 3, # reverse the signs to mirror the effect on the other side
      0,                                  # y-coordinate: Starts at the top of the screen
      roadmark_w,                         # Width of the roadmark
      height)                             # Height of the roadmark
)
# Apply the changes on the screen
pygame.display.update()

# Event Listeners
while running:
    for event in pygame.event.get(): # The get method fetches all the events (e.g., keyboard input, mouse clicks, window close)
        if event.type == QUIT: # QUIT: the user clicks the close button (x) to execute pygame.quit()
            running = False
        if event.type == KEYDOWN:
            K_ESCAPE   # The user presses the esc key to execute pygame.quit() - also works in fullscreen mode
            running = False


# Collapse the application window
pygame.quit()