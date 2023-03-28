import pygame
from data import *
def is_game_over():
    return game_close
game_close = False
def event():
    global game_close
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_close = True
def simulation():
    pass
def display():
    pygame.draw.rect(dis, (255, 255, 255), (100, 100, 100, 100))
    pygame.display.update()
def quit_game():
    quit()

