import pygame
import time
import random


class Constants:
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    WIDTH = 400
    HEIGHT = 400

    BLOCK_SIZE = 20
    MAX_LEVEL = 2
 
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, Constants.yellow)
    SCREEN.blit(value, [0, 0])

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(Constants.black)

    

    pygame.display.update()
    CLOCK.tick(12)





main()