import pygame
import random
from platform import Brick

class Circle:
    def __init__(self, radius, color, center, surface):
        self.radius = radius
        self.color = color
        self.x, self.y = center[0], center[1]
        self.surface = surface
        self.diff = 3
        self.is_jumping = False
        self.jump_number = 10
        #на сколько будет изменяться по х и у
        self.diff_x = 0
        self.diff_y = 0
        while self.diff_x == 0 or self.diff_y == 0:
            self.diff_x = random.randint(-5,5)
            self.diff_y = random.randint(-5,5)


    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
        def move_by_keys(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= self.diif
            elif keys[pygame.K_RIGHT]:
                self.x += self.diff
            elif keys[pygame.K_UP]:
                self.y -= self.diff
            elif keys[pyhame.K_DOWN]:
                self.y += self.diff

    def __collision(self, brick):
        top_border = (self.y + self.radius >= brick.top) \
            and (self.y + self.radius <= brick.bottom)
        bottom_border = (self.y - self.radius <= brick.bottom) \
            and (self.y - self.radius >= brick.top)
        left_right_border = brick.left <= self.x <= brick.right

        if (top_border or bottom_border) and left_right_border:
            self.diff_y = -self.diff_y
            if isinstance(brick, Brick):
                return True

        return False
        

    



    def random_movement(self, width, brick, wall):
        for brick1 in wall.bricks:
            self.__collision(brick1)
        self.__collision(brick)
        
        self.x += self.diff_x
        self.y += self.diff_y
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.diff_x = -self.diff_x
        if self.y + self.radius >= width or self.y - self.radius <= 0:
            self.diff_y = -self.diff_y

    