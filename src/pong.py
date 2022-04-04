import pygame

pygame.init()
width = 1200
height = 990
screen = pygame.display.set_mode((width,height))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
