import pygame
import os

dirname = os.path.dirname(__file__)

board = pygame.image.load(os.path.join(dirname, "objects", "board1.png"))

class Board(pygame.sprite.Sprite):
	def __init__(self, x=25, y=225):
		super().__init__()
		self.image = board
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y