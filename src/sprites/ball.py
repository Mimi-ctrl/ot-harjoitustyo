import pygame
import os

dirname = os.path.dirname(__file__)

ball = pygame.image.load(os.path.join(dirname, "..", "objects", "red_ball.png"))

class Ball(pygame.sprite.Sprite):
	def __init__(self, x=375, y=250):
		super().__init__()
		self.image = ball
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
