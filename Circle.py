import pygame
import random

from platform import Platform, Brick

class Circle:
    #инициализация (первоначальное создание объекта круга)
    def __init__(self, color, radius, center):
        self.color = color
        self.radius = radius
        self.x, self.y = center[0], center[1]
        self.is_jumping = False
        self.jump_count = 10
        self.diff_x = 0
        self.diff_y = 0
        while self.diff_x == 0 or self.diff_y == 0:
            self.diff_x = random.randint(-3,3)
            self.diff_y = random.randint(3,5)
    #метод отрисовки: принимает в себя объект "окна (surface)"
    def draw(self, surface1):
        pygame.draw.circle(surface=surface1, color=self.color, center=(self.x, self.y), radius=self.radius)
    
    def move_by_keys(self, keys):
        #Если не в состоянии прыжка, то последующий код должен выполняться
        #Если в состоянии прыжка, то следующик код просто не выполняется
        if self.is_jumping:
            return
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3

    def jump(self, keys):
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        #Если в состоянии прыжка, то меняй координату y
        if self.is_jumping:
            #Пока между 10 и 0 - симулируем прыжок вверх
            if self.jump_count > 0:
                self.y -= 10
                self.jump_count -= 1
            #симулирем приземление
            # self.jump_count in range(-10, 1)
            elif self.jump_count > -10 and self.jump_count <= 0:
                self.y += 10
                self.jump_count -= 1
            #при приземлении должны сказать, что уже не прыгаем и снова можем прыгать
            else:
                self.is_jumping = False
                self.jump_count = 10

    def random_movement(self, width, platform, wall) -> bool:
        #изменяются координаты на diff_x diff_y
        self.wall_collision(wall)
        self.collision(platform)
        self.x += self.diff_x
        self.y += self.diff_y
        #реализовать логику соударения с окном
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.diff_x = -self.diff_x
        if self.y + self.radius >= width or self.y - self.radius <=0:
            self.diff_y = -self.diff_y
        
        if self.y + self.radius >= width:
            #endgame
            return True
        else:
            #continue game
            return False

    def collision(self, brick):
        #TODO
        if ((self.y + self.radius) >= brick.top \
            and (self.y + self. radius) <= brick.bottom \
            and (brick.left <= self.x <= brick.right)) or \
            ((self.y - self.radius) <= brick.bottom \
            and (self.y - self.radius) >= brick.top \
            and (brick.left <= self.x <= brick.right)):
            self.diff_y = -self.diff_y

            if isinstance(brick, Platform):
                return False
            elif isinstance(brick, Brick):
                return True
        return False


    def wall_collision(self, wall):
        for brick in wall.bricks:
            if self.collision(brick):
                wall.collision(brick)