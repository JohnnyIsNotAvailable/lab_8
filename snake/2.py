import pygame
import time
import random
 
pygame.init()



class Constants:
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    WIDTH = 600
    HEIGHT = 400

    BLOCK_SIZE = 10

    MAX_LEVEL = 2

SCREEN = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    def __init__(self, level):
        self.body = []

        f = open("level{}.txt".format(level), "r")

        #lines = content.split('\n')
        #print(len(lines[0]))
        
        for y in range(0, Constants.HEIGHT//Constants.BLOCK_SIZE + 1):
            for x in range(0, Constants.WIDTH//Constants.BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(Constants.BLOCK_SIZE * point.x, Constants.BLOCK_SIZE * point.y, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)
 

 
dis = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT)) 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, Constants.yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, Constants.red, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [Constants.WIDTH / 6, Constants.HEIGHT / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = Constants.WIDTH / 2
    y1 = Constants.HEIGHT / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, Constants.WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, Constants.HEIGHT - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(Constants.black)
            message("You Lost! Press R-Play Again or Q-Quit", Constants.red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= Constants.WIDTH or x1 < 0 or y1 >= Constants.HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(Constants.black)
        pygame.draw.rect(dis, Constants.green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, Constants.WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, Constants.HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
            
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
gameLoop()