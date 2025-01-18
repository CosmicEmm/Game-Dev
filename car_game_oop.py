import pygame
from pygame.locals import *
import random

class Window:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((1, 115, 92))
        pygame.display.set_caption('Cosmic Speed')

        self.road_w = int(self.width/1.6)
        self.roadmark_w = int(self.width/80)
        self.right_lane = self.width/2 + self.road_w/4
        self.left_lane = self.width/2 - self.road_w/4


    def draw_background(self):
        pygame.draw.rect(
            self.window,
            (50, 50, 50),
            (self.width/2-self.road_w/2, 0, self.road_w, self.height))
        pygame.draw.rect(
            self.window,
            (255, 240, 60),
            (self.width/2 - self.roadmark_w/2, 0, self.roadmark_w, self.height))
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 - self.road_w/2 + self.roadmark_w*2, 0, self.roadmark_w, self.height))
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 + self.road_w/2 - self.roadmark_w*3, 0, self.roadmark_w, self.height))


class Game:
    def __init__(self):
        self.running = True
        self.counter = 0
        self.player = PlayerVehicle('car.png')
        self.enemy = EnemyVehicle('otherCar.png')
        self.gameloop()


    def level_up(self):
        if self.counter == 5000:
            self.enemy.speed += 0.15
            self.counter = 0
            print("Level up", self.enemy.speed)


    def random_enemy(self):
        if self.enemy.vehicle_rect[1] > window.height:
            if random.randint(0, 1) == 0:
                self.enemy.vehicle_rect.center = window.right_lane, -200
            else:
                self.enemy.vehicle_rect.center = window.left_lane, -200

    
    def event_listeners(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:      
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key in [K_a, K_LEFT] and self.player.vehicle_rect.center == (window.right_lane, window.height * 0.8): 
                    self.player.vehicle_rect = self.player.vehicle_rect.move([- int(window.road_w/2), 0])   
                else:                                                                                
                    None                                                
                if event.key in [K_d, K_RIGHT] and self.player.vehicle_rect.center == (window.left_lane, window.height * 0.8): 
                    self.player.vehicle_rect = self.player.vehicle_rect.move([+ int(window.road_w/2), 0])
                else:                                                
                    None


    def gameloop(self):
        while self.running:
            self.counter += 1
            self.level_up()
            self.enemy.vehicle_rect[1] += self.enemy.speed
            self.random_enemy()
            if self.player.vehicle_rect.colliderect(self.enemy.vehicle_rect):
                print("GAME OVER! YOU LOST!")
                break
            self.event_listeners()
            window.draw_background()
            window.window.blit(self.player.vehicle, self.player.vehicle_rect) 
            window.window.blit(self.enemy.vehicle, self.enemy.vehicle_rect)
            pygame.display.update()

        pygame.quit()


class Vehicle:
    def __init__(self, img_path):
        self.vehicle = pygame.image.load(img_path)
        self.vehicle_rect = self.vehicle.get_rect()


class PlayerVehicle(Vehicle):
    def __init__(self, img_path):
        super().__init__(img_path)
        self.vehicle_rect.center = window.right_lane, window.height * 0.8


class EnemyVehicle(Vehicle):
    def __init__(self, img_path):
        super().__init__(img_path)
        self.vehicle_rect.center = window.left_lane, window.height * 0.2
        self.speed = 1
        

pygame.init()
window = Window()
game = Game()
