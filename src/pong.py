import pygame
import os	

dirname = os.path.dirname(__file__)
pygame.init()

width = 880
height = 880
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

icon = pygame.image.load(os.path.join(dirname, "objects", "icon.png"))
pygame.display.set_icon(icon)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill((118,238,198))
	pygame.display.update()