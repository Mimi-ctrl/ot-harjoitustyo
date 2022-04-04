import pygame
import os

dirname = os.path.dirname(__file__)

pygame.init()
width = 880
height = 880
screen = pygame.display.set_mode((width,height))

ball = pygame.image.load(os.path.join(dirname, "objects", "red_ball.png"))

x = 0
y = 0
speed = 4
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
			
	screen.fill((118,238,198))
	screen.blit(ball, (x, y))
	pygame.display.flip()

	x += speed
	if speed > 0 and x + ball.get_width() >= 880:
		speed =- speed
	if speed < 0 and x <= 0:
		speed =- speed
		
	clock.tick(60)