import os
import pygame


DIRNAME = os.path.dirname(__file__)

BALL = pygame.image.load(os.path.join(
    DIRNAME, "..", "objects", "red_ball.png"))


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=375, y=250):  # pylint: disable=invalid-name
        super().__init__()
        self.image = BALL
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 20
        self.d_x = 1
        self.d_y = 1
