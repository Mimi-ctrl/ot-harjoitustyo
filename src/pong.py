import pygame
from others import music, icon
from game_loop import start, game_loop, end

pygame.init()
pygame.display.set_caption("Pong")
music()
icon()

while True:
    start()
    game_loop()
    end()
    