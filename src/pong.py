import pygame
import os

dirname = os.path.dirname(__file__)

pygame.init()
width = 1200
height = 880
screen = pygame.display.set_mode((width,height))

ball = pygame.image.load(os.path.join(dirname, "objects", "red_ball.png"))

screen.fill((118,238,198))
screen.blit(ball, (100, 80))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()