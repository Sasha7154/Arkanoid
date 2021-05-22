import pygame
import random 
from cir import Circle
from platform import Brick, Platform, Wall
pygame.init()

win_size = 500
win = pygame.display.set_mode((win_size,win_size))

background_color = (0,0,0)


clock = pygame.time.Clock()
FPS = 60


def generate_random_color():
    return random.choices(range(256), k=3) 


brick_color = generate_random_color()
platform_color = generate_random_color()

brick = Brick(win, win_size, brick_color, win_size/2, win_size/2, win_size/10)
platform = Platform (win, win_size, platform_color, win_size/2, win_size/2, win_size/8)

center = (win_size/2, win_size/2)
radius = 10
color_ball = (255,255,0)

ball = Circle(radius, color_ball, center, win)

RED = (255,0,0)
wall = Wall(win_size, win,RED)
wall.fill(3,5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill(background_color)
    ball.random_movement(win_size, platform, wall)
    ball.draw()
    wall.draw()


    
    platform.move_by_keys()
    platform.draw()
   
    pygame.display.update()
    clock.tick(FPS)