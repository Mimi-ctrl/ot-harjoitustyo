import pygame
import os
from sprites.ball import Ball
from sprites.board import Board1, Board2	

def __init__(self):
	self.points = 0

dirname = os.path.dirname(__file__)
pygame.init()

width = 750
height = 650
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

icon = pygame.image.load(os.path.join(dirname, "objects", "icon.png"))
pygame.display.set_icon(icon)

board_speed = 90
board1 = Board1()
board2 = Board2()
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(board1,board2,ball)

def boards_max_positions():
	if board1.rect.y <= 0:
		board1.rect.y = 0
	if board2.rect.y <= 0:
		board2.rect.y = 0
	if board1.rect.y >= 525:
		board1.rect.y = 525
	if board2.rect.y >= 525:
		board2.rect.y = 525

def keyboard():
	key = pygame.key.get_pressed()
	if key[pygame.K_w]:
		board1.rect.y -= board_speed
	if key[pygame.K_s]:
		board1.rect.y += board_speed
	if key[pygame.K_UP]:
		board2.rect.y -= board_speed
	if key[pygame.K_DOWN]:
		board2.rect.y += board_speed
	if key[pygame.K_ESCAPE]:
		exit()

def ball_move():
	ball.rect.x += ball.speed * ball.dx
	ball.rect.y += ball.speed * ball.dy

	if ball.rect.y > 590:
		ball.dy = -1

	if ball.rect.x > 690:
		ball.rect.x, ball.rect.y = 375, 250
		ball.dx = -1
		board1.points += 1

	if ball.rect.y < 0:
		ball.dy = 1

	if ball.rect.x  < 0:
		ball.rect.x, ball.rect.y = 375, 250
		ball.dx = 1
		board2.points += 1
	
	if board1.rect.colliderect(ball.rect):
		ball.dx = 1
	
	if board2.rect.colliderect(ball.rect):
		ball.dx = -1

def redraw():
	screen.fill((118,238,198))
	all_sprites.draw(screen)
	pygame.display.update()
	keyboard()
	boards_max_positions()
	ball_move()


while True:
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	redraw()