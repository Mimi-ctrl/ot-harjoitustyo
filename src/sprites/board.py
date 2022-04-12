import os
import pygame

dirname = os.path.dirname(__file__)

board = pygame.image.load(os.path.join(dirname, "..", "objects", "board1.png"))

class Board1(pygame.sprite.Sprite):
    def __init__(self, x=15, y=225): # pylint: disable=invalid-name
        super().__init__()
        self.image = board
        self.points = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Board2(pygame.sprite.Sprite):
    def __init__(self, x=715, y=225): # pylint: disable=invalid-name
        super().__init__()
        self.image = board
        self.points = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
