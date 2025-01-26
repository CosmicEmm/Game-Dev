import pygame
from pygame.locals import *
import random

class Window:
    """ Application Window Object """
    def __init__(self):
        # set window parameters
        self.width = 800
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((1, 115, 92))
        pygame.display.set_caption('Cosmic Speed')

        # set background parameters
        self.road_w = int(self.width/1.6)
        self.roadmark_w = int(self.width/80)
        self.right_lane = self.width/2 + self.road_w/4
        self.left_lane = self.width/2 - self.road_w/4


    def draw_background(self):
        """
        a method that draws the background
        """
        # draw road
        pygame.draw.rect(
            self.window,
            (50, 50, 50),
            (self.width/2-self.road_w/2, 0, self.road_w, self.height))
        # draw centre line
        pygame.draw.rect(
            self.window,
            (255, 240, 60),
            (self.width/2 - self.roadmark_w/2, 0, self.roadmark_w, self.height))
        # draw left road marking
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 - self.road_w/2 + self.roadmark_w*2, 0, self.roadmark_w, self.height))
        # draw right road marking
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 + self.road_w/2 - self.roadmark_w*3, 0, self.roadmark_w, self.height))


class Game:
    """ Game Loop and Logic """
    def __init__(self):
        self.running = True
        self.level = 0
        self.counter = 0
        self.player = PlayerVehicle('car.png')
        self.enemy = EnemyVehicle('otherCar.png')
        self.gameloop()


    def level_up(self):
        """
        a method that increases game difficulty overtime
        """
        # start counting
        self.counter += 1

        # increase game speed as count increases
        if self.counter == 5000:
            self.enemy.speed += 0.15
            self.level += 1
            # reset counter
            self.counter = 0
            print(f'Level {self.level}!')


    def randomize_enemy(self):
        """
        a method that makes the enemy vehicle appear on random lanes
        """
        # if enemy vehicle has moved beyond the window's height
        if self.enemy.vehicle_rect[1] > window.height:
            # randomly select lane
            if random.randint(0, 1) == 0:
                self.enemy.vehicle_rect.center = window.right_lane, -200
            else:
                self.enemy.vehicle_rect.center = window.left_lane, -200

    
    def event_listeners(self):
        """
        a method that stores key controls logic
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                # collapse the application
                self.running = False
            if event.type == KEYDOWN:      
                if event.key == K_ESCAPE:
                    self.running = False
                # move player vehicle to the left + edge case
                if event.key in [K_a, K_LEFT] and self.player.vehicle_rect.center == (window.right_lane, window.height * 0.8):
                    self.player.vehicle_rect = self.player.vehicle_rect.move([- int(window.road_w/2), 0])   
                else:                                                                                
                    None
                # move player vehicle to the right + edge case                                            
                if event.key in [K_d, K_RIGHT] and self.player.vehicle_rect.center == (window.left_lane, window.height * 0.8): 
                    self.player.vehicle_rect = self.player.vehicle_rect.move([+ int(window.road_w/2), 0])
                else:                                                
                    None


    def gameloop(self):
        """
        a method that initializes the game loop
        """
        # start game loop
        while self.running:
            # level up logic
            self.level_up()
            # animate enemy vehicle
            self.enemy.vehicle_rect[1] += self.enemy.speed
            # randomize enemy appearance
            self.randomize_enemy()
            # game over logic
            if self.player.vehicle_rect.colliderect(self.enemy.vehicle_rect):
                print("GAME OVER! YOU LOST!")
                break
            # initialize key controls
            self.event_listeners()
            # draw background
            window.draw_background()
            # place player vehicle
            window.window.blit(self.player.vehicle, self.player.vehicle_rect)
            # place enemy vehicle
            window.window.blit(self.enemy.vehicle, self.enemy.vehicle_rect)
            # apply changes
            pygame.display.update()

        #collapse application window if game over
        pygame.quit()


class Vehicle:
    """ Vehicle Object --> Parent"""
    def __init__(self, img_path):
        self.vehicle = pygame.image.load(img_path)
        self.vehicle_rect = self.vehicle.get_rect()


class PlayerVehicle(Vehicle):
    """ Player Vehicle Object --> Child"""
    def __init__(self, img_path):
        super().__init__(img_path)
        self.vehicle_rect.center = window.right_lane, window.height * 0.8


class EnemyVehicle(Vehicle):
    """ Enemy Vehicle Object --> Child"""
    def __init__(self, img_path):
        super().__init__(img_path)
        self.vehicle_rect.center = window.left_lane, window.height * 0.2
        self.speed = 1
        

# initialize the application window
pygame.init()
window = Window()
# run the game
Game()
