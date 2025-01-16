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


# load player vehicle
car = pygame.image.load('car.png') # loads the car image and stores it as a Surface object
car_loc = car.get_rect() # creates a Rect object that represents the rectangular area of the car image
car_loc.center = (width/2 + road_w/4, # x-coordinate: right lane
                 height * 0.8)        # y-coordinate: bottom of the screen

# load enemy vehicle
car2 = pygame.image.load('otherCar.png') 
car2_loc = car.get_rect()
car2_loc.center = (width/2 - road_w/4, # x-coordinate: left lane
                  height * 0.2)        # y-coordinate: top of the screen

# Event Listeners
while running:
    for event in pygame.event.get(): # The get method fetches all the events (e.g., keyboard input, mouse clicks, window close)
        if event.type == QUIT: # QUIT: the user clicks the close button (x) to execute pygame.quit()
            running = False
        if event.type == KEYDOWN: # selects all the keys of our keybaord
            if event.key == K_ESCAPE:   # The user presses the esc key to execute pygame.quit() - also works in fullscreen mode
                running = False
            # Lane Logic and Edge Cases (prevents the car from moving left if it’s already in the left lane and vice versa)
            if event.key in [K_a, K_LEFT] and car_loc.center == (width/2 + road_w/4, height * 0.8):# if A/LEFT is pressed and car is in right lane, move to the left
                car_loc = car_loc.move([- int(road_w/2), 0])    
            else:        # if A/LEFT is pressed and car is already in left lane, do nothing                                       
                 None                                                
            if event.key in [K_d, K_RIGHT] and car_loc.center == (width/2 - road_w/4, height * 0.8):# if D/RIGHT is pressed and car is in left lane, move to the right
                car_loc = car_loc.move([+ int(road_w/2), 0])
            else:        # # if D/RIGHT is pressed and car is already in right lane, do nothing
                None

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
    
    screen.blit(car, car_loc)   # Draw the player vehicle at its location
    screen.blit(car2, car2_loc) # Draw the enemy vehicle at its location
    pygame.display.update()     # Update the display


# Collapse the application window
pygame.quit()