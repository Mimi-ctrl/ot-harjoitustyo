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

font = pygame.font.SysFont("Arial", 24)
text = font.render("Pelaaja1: 0   Pelaaja2: 0", True, (255, 0, 0))
text2 = font.render("ENTER=paussi/aloita ESC=lopeta F2=uusi peli", True, (255, 0, 0))

icon = pygame.image.load(os.path.join(dirname, "objects", "icon.png"))
pygame.display.set_icon(icon)

board_speed = 1
board1 = Board1()
board2 = Board2()
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(board1,board2,ball)

# def draw():
	#text (pisteet, näppäin ohjeet)	
	#lopputeksti jossa näkyy voittaja ja pisteet
	#pelin aloitus enter

#def new_game():

#fed game_ovet():
#kun pisteet ovat 20

def redraw():
	screen.fill((118,238,198))
	all_sprites.draw(screen)
	screen.blit(text, (90, 10))
	screen.blit(text2, (90, 600))
	pygame.display.update()
	key = pygame.key.get_pressed()
	if key[pygame.K_w]:
		board1.rect.y -= board_speed
	if key[pygame.K_s]:
		board1.rect.y += board_speed
	if key[pygame.K_UP]:
		board2.rect.y -= board_speed
	if key[pygame.K_DOWN]:
		board2.rect.y += board_speed
	#if key[pygame.K_F2]:
		#newgame
	if key[pygame.K_ESCAPE]:
		exit()
	#if key[pygame.K_ENTER:
		#pause/start
	ball.rect.x += ball.speed * ball.dx
	ball.rect.y += ball.speed * ball.dy

	if ball.rect.y > 650:
		ball.dy = -1
	if ball.rect.x > 750:
		ball.dx = -1
	if ball.rect.y < 0:
		ball.dy = 1
	if ball.rect.x  < 0:
		ball.dx = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	redraw()