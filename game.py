import pygame
from platform import Platform
from platform import Wall
from Circle import Circle 
ENDGAME_TEXT = 'Game Over'
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Menu:
    pygame.init()
    win_size = 700
    win = pygame.display.set_mode((win_size,win_size))
    background_color = (255,255,255)

'''
Инициализация шрифта
'''
font0 = pygame.font.SysFont('arial', 64)
red = (255,0,0)
'''
Функция отрисовки текста. Передаём туда (в таком же порядке)
строку текста, шрифт, его цвет, surface, на которой хотим его отображать и
координаты x, y левого верхнего угла.
'''
def draw_text(text, font, color, frame, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    frame.blit(textobj, textrect)  

menu_color = (0,0,0)
def menu(win):
    #цикл меню
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        win.fill(menu_color)
        draw_text('Menu', font0, red, win, 320, 320)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu(win)

            win.fill(background_color)
    #code

    pygame.display.update()

#win - Surface
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
background_color = (0,0,0)
platform_color = (255,0,0)

font = pygame.font.SysFont('calibri', 32)
endgame_text = font.render(ENDGAME_TEXT, 1, RED, BLUE)

platform = Platform(win, win_size, platform_color)
ball_center = (win_size/2, win_size/2)
ball_radius = win_size/50
ball_color = (255,0,0)
ball = Circle(ball_color, ball_radius, ball_center)
wall = Wall(win, win_size, platform_color)
bricks_rows = 3
bricks_cols = 5
wall.fill_bricks(bricks_rows, bricks_cols, 2)
FPS = 60
clock = pygame.time.Clock()

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    if not game_over:
        #code
        game_over = ball.random_movement(win_size, platform, wall)
        wall.draw()
        ball.draw(win)
        platform.move_by_keys()
        platform.draw()
    else:
        text_left = (win_size - endgame_text.get_width())/2
        text_top = (win_size - endgame_text.get_height())/2
        win.blit(endgame_text, (text_left, text_top))

    pygame.display.update()
    clock.tick(FPS)