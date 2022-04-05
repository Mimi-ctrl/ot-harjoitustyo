import pygame
import os
from sprites.ball import Ball
from sprites.board import Board1, Board2	

dirname = os.path.dirname(__file__)
pygame.init()

width = 750
height = 650
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

icon = pygame.image.load(os.path.join(dirname, "objects", "icon.png"))
pygame.display.set_icon(icon)

board1 = Board1()
board2 = Board2()
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(board1,board2,ball)

def redraw():
	screen.fill((118,238,198))
	all_sprites.draw(screen)
	pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	redraw()