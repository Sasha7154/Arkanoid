import pygame

class Brick:
    def __init__(self, surface, win_size, color, left = 0, top=0, width=100):
        self.surface = surface
        self.win_size = win_size
        self.color = color

        self.width = width
        self.height = self.width/10
        self.left = left
        self.right = self.left + self.width
        self.top = top
        self.bottom = self.top + self.height

    def draw(self):
        self.rect = (self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, width=1)


class Platform(Brick):
    def __init__(self, surface, win_size, color):
        super().__init__(surface, win_size, color)
        self.width = win_size / 5
        self.height = win_size / 50
        self.left = (win_size / 2) - (self.width / 2)
        self.right = self.left + self.width
        self.top = 4 / 5 * win_size
        self.bottom = self.top + self.height 
    
    def move_by_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if (self.left - 3) < 0:
                pass
            else:
                self.left -= 3
                self.right = self.left + self.width
        elif keys[pygame.K_RIGHT]:
            if (self.right + 3) > self.win_size:
                pass
            else:   
                self.left += 3
                self.right = self.left + self.width
    
    def draw(self):
        self.rect = (self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, width=3, border_radius=int(self.height/2))

class Wall:
    def __init__(self, surface, win_size, color):
        self.bricks = []
        self.surface = surface
        self.win_size = win_size
        self.color = color
        self.fills = {
            1: lambda rows, cols: self.__fill_without_distance(rows, cols),
            2: lambda rows, cols: self.__fill_with_distance(rows, cols)
        }
        #TODO
    def fill_bricks(self, n_rows, n_bricks, type_f:int):
        self.fills[type_f](n_rows, n_bricks)

    def __fill_without_distance(self, n_rows, n_bricks):
        brick_left = 0
        brick_top = 0
        brick_width = int(self.win_size/n_bricks)
        brick_height = int(brick_width/10)
        for i in range(n_rows):
            for j in range(n_bricks):
                brick = Brick(self.surface, self.win_size, self.color,
                brick_left, brick_top, brick_width)
                self.bricks.append(brick)
                brick_left += brick_width
            brick_left = 0
            brick_top += brick_height

    def __fill_with_distance(self, n_rows, n_bricks):
        brick_left = 0
        brick_top = 0
        brick_width = int(self.win_size/n_bricks)
        brick_height = int(brick_width/10)
        for i in range(n_rows):
            for j in range(n_bricks):
                brick = Brick(self.surface, self.win_size, self.color,
                brick_left, brick_top, brick_width)
                self.bricks.append(brick)
                brick_left += brick_width
            brick_left = 0
            brick_top += 2 * brick_height

    def collision(self, brick):
        if brick in self.bricks:
            self.bricks.remove(brick)
        else:
            raise Exception('Brick isnt in bricks!')
        
    def draw(self):
        for brick in self.bricks:
            brick.draw()