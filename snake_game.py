# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:19:03 2020

@author: MOHANA D
"""

'''Code for a Simple Snake Game'''

#import required libraries

import pygame
import random

# initializing pygame
pygame.init()

# Colors
white = (255, 255, 255) # rgb format
red = (255, 0, 0)
black = (0, 0, 0)

# Creating a window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

# defining the screen text
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# creating a snake by defining it
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(10, screen_width-20)
    food_y = random.randint(50, screen_height -20)
    score = 0
    init_velocity = 3  #speed of snake movement
    snake_size = 30    # snake size
    fps = 100          # fps => frames per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press 'Enter' to Play again", red, 100, 250)
            # this will show the game over screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    
                # Creating the controls to play 
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10: 
                # abs() returns the absolute value in integer or float
                score = score + 1
                food_x = random.randint(10, screen_width - 30)
                food_y = random.randint(50, screen_height - 30)
                snk_length = snk_length + 5

            gameWindow.fill(white) # Gives the total score played by the player
            text_screen("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (0,40), (900,40),5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()