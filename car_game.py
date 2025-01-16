import pygame
from pygame.locals import *
import random

# Shape Parameters
size = width, height = (800, 800)  # Unpacking the tuple into width and height of the screen
road_w = int(width/1.6)            # Set road width to 500 pixels (800/1.6), also convert the resulting floating point to an integer
roadmark_w = int(width/80)         # Set roadmarking width to 10 pixels (800/80)
# Location Parameters
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# Animation Parameters
speed = 1

# Initialize the Application
pygame.init()
running = True
# Set Window Size
screen = pygame.display.set_mode(size)
# Set Window Title
pygame.display.set_caption('Cosmic Speed')
# Set Background Color
screen.fill((1, 115, 92)) # (red, green, blue)

# Load Player Vehicle
car = pygame.image.load('car.png')          # loads the car image and stores it as a Surface object
car_rec = car.get_rect()                    # creates a Rect object that represents the rectangular area of the car image
car_rec.center = right_lane, height * 0.8   # y-coordinate: bottom of the screen

# Load Enemy Vehicle
car2 = pygame.image.load('otherCar.png')
car2_rec = car.get_rect()
car2_rec.center = left_lane, height * 0.2   # y-coordinate: 'height * 0.2' means top of the screen

counter = 0

# Game Loop
while running:
    counter += 1
    # Increase Game Difficulty Overtime
    if counter == 5000:                     # 5000 are the number of iterations of the while loop before the game levels up
        speed += 0.15                       # increase speed by 0.15px
        counter = 0                         # reset the counter back to 0 after 5000 iterations
        print("Level up", speed)
    # Animate Enemy Vehicle 
    car2_rec[1] += speed                    # move the enemy vehicle downward and out of sight
    if car2_rec[1] > height:
        # Randomnly Select Lane
        if random.randint(0, 1) == 0:
            car2_rec.center = right_lane, -200 # place the enemy vehicle's center 200px above the top edge of the right lane, creating a looping effect
        else:
            car2_rec.center = left_lane, -200
    
    # End Game Logic
    if car_rec[0] == car2_rec[0] and car2_rec[1] > car_rec[1] - 250: # reduce 250px because our vehicle is 250px all the way around to make collision more realistic
        print("GAME OVER! YOU LOST!")
        break
    
    # Event Listeners
    for event in pygame.event.get():    # The get method fetches all the events (e.g., keyboard input, mouse clicks, window close)
        if event.type == QUIT:          # QUIT: the user clicks the close button (x) to execute pygame.quit()
            running = False
        if event.type == KEYDOWN:       # selects all the keys of our keybaord
            if event.key == K_ESCAPE:   # The user presses the esc key to execute pygame.quit() - also works in fullscreen mode
                running = False
            # Lane Logic and Edge Cases (prevents the car from moving left if it’s already in the left lane and vice versa)
            if event.key in [K_a, K_LEFT] and car_rec.center == (right_lane, height * 0.8): 
                car_rec = car_rec.move([- int(road_w/2), 0])   # Move User Car to the Left
            else:                                              # Edge Case: if A/LEFT is pressed and car is already in left lane, do nothing                                       
                None                                                
            if event.key in [K_d, K_RIGHT] and car_rec.center == (left_lane, height * 0.8): 
                car_rec = car_rec.move([+ int(road_w/2), 0])   # Move User Car to the Right
            else:                                              # Edge Case: if D/RIGHT is pressed and car is already in right lane, do nothing
                None

    # Graphics - Draw the Road
    pygame.draw.rect(
        screen,                   # Drawing surface
        (50, 50, 50),             # Color: Dark Grey
        (width/2 - road_w/2,      # x-coordinate: Centered horizontally
        0,                        # y-coordinate: Starts at the top of the screen
        road_w,                   # Width of the road
        height)                   # Height of the road (full screen height)
    )
    # Draw the Central Road Marking
    pygame.draw.rect(
        screen,
        (255, 240, 60),           # Color: Yellow
        (width/2 - roadmark_w/2,  # x-coordinate: Centered horizontally
        0,                        # y-coordinate: Starts at the top of the screen
        roadmark_w,               # Width of the roadmark
        height)                   # Height of the roadmark
    )
    # Draw the Left Road Marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),                      # Color: White
        (width/2 - road_w/2 + roadmark_w * 2, # (width/2 - road_w/2) starts from the left edge of the road and (+ roadmark_w * 2) takes it 20 px away from that edge
        0,                                    # y-coordinate: Starts at the top of the screen
        roadmark_w,                           # Width of the roadmark
        height)                               # Height of the roadmark
    )
    # Draw the Right Road Marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),                      # Color: White
        (width/2 + road_w/2 - roadmark_w * 3, # reverse the signs to mirror the effect on the other side
        0,                                    # y-coordinate: Starts at the top of the screen
        roadmark_w,                           # Width of the roadmark
        height)                               # Height of the roadmark
    )
    
    # Draw the Car Images on the Screen
    screen.blit(car, car_rec) 
    screen.blit(car2, car2_rec)
    # Update the Display Window
    pygame.display.update()

# Collapse the Application Window
pygame.quit()