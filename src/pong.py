import pygame
from files import music, icon
from game_loop import start, game_loop, end

pygame.init()
pygame.display.set_caption("Pong")
music()
icon()

while True:
    """ Called a function.
    """
    start()
    game_loop()
    end()
    