import os
import sys
import pygame
from sprites.ball import Ball
from sprites.board import Board1, Board2
from pygame import mixer


def __init__(self):
    self.points = 0


dirname = os.path.dirname(__file__)  
pygame.init()

screen = pygame.display.set_mode((750, 650))
pygame.display.set_caption("Pong")

icon = pygame.image.load(os.path.join(dirname, "objects", "icon.png"))
pygame.display.set_icon(icon)

BOARD_SPEED = 50
board1 = Board1()
board2 = Board2()
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(board1, board2, ball)

mixer.music.load(os.path.join(dirname, "sounds","background_music.mp3"))  
pygame.mixer.music.set_volume(0.3) 
pongSound = mixer.Sound(os.path.join(dirname, "sounds", "pong_sound.wav"))  


def boards_max_positions(): 
    """ Determines the maximum positions of the boards.
        If boards coordinate in y axel is bigger than 525 or smaller than 0,
        boards coordinate in y axel not getting bigger or smaller.
    """
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
        board1.rect.y -= BOARD_SPEED
    if key[pygame.K_s]:
        board1.rect.y += BOARD_SPEED
    if key[pygame.K_UP]:
        board2.rect.y -= BOARD_SPEED
    if key[pygame.K_DOWN]:
        board2.rect.y += BOARD_SPEED
    if key[pygame.K_ESCAPE]:
        sys.exit()
    if key[pygame.K_p]:
        pause()


def game_texts():
    yellow = 255, 255, 0

    bong_font = pygame.font.SysFont("D050000L", 300)
    text = bong_font.render("H", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (375, 250)
    screen.blit(text, text_rect)

    points_font = pygame.font.SysFont("Lobster two", 40)
    p1_points = points_font.render(f"Pelaaja 1: {str(board1.points)}", False, yellow)
    p1_rect = p1_points.get_rect()
    p1_rect.center = (750 // 3, 25)
    screen.blit(p1_points, p1_rect)

    p2_points = points_font.render(f"Pelaaja 2: {str(board2.points)}", False, yellow)
    p2_rect = p2_points.get_rect()
    p2_rect.center = (550, 25)
    screen.blit(p2_points, p2_rect)

def start_text():
    yellow = 255, 255, 0
    screen.fill((255, 62, 150)) 
    bong_font = pygame.font.SysFont("Lobster two", 35)
    second_bong_font = pygame.font.SysFont("Lobster two", 60)
    text = second_bong_font.render("PONG", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (350, 100)
    screen.blit(text, text_rect)
    text1 = bong_font.render("Aloita/jatka: ENTER", False, yellow)
    text_rect1 = text1.get_rect()
    text_rect1.center = (350, 300)
    screen.blit(text1, text_rect1)
    text2 = bong_font.render("Poistu: ESC", False, yellow)
    text_rect2 = text2.get_rect()
    text_rect2.center = (350, 400)
    screen.blit(text2, text_rect2)
    text3 = bong_font.render("Tauko: p", False, yellow)
    text_rect3 = text3.get_rect()
    text_rect3.center = (350, 500)
    screen.blit(text3, text_rect3)


def end_text():
    yellow = 255, 255, 0
    screen.fill((255, 62, 150)) 
    bong_font = pygame.font.SysFont("Lobster two", 45)
    winner = ""
    if board1.points > board2.points:
        winner = "Pelaaja 1"
    if board1.points < board2.points:
        winner = "Pelaaja 2"
    text = bong_font.render(f"Voittaja: {winner}!!", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (350, 100)
    screen.blit(text, text_rect)
    text1 = bong_font.render("Uusi peli: ENTER", False, yellow)
    text_rect1 = text1.get_rect()
    text_rect1.center = (350, 300)
    screen.blit(text1, text_rect1)
    text2 = bong_font.render("Poistu: ESC", False, yellow)
    text_rect2 = text2.get_rect()
    text_rect2.center = (350, 400)
    screen.blit(text2, text_rect2)


def pause_text():
    red = (255,0,0)
    bong_font = pygame.font.SysFont("Lobster two", 90)
    text = bong_font.render("Pause", False, red)
    text_rect = text.get_rect()
    text_rect.center = (375, 250)
    screen.blit(text, text_rect)


def board1_get_point(): 
    """ When the coordinate of the ball on the x-axis is bigger than 690, 
        the ball moves to the center and board 1 gets a point.
    """ 
    if ball.rect.x > 690:
        ball.rect.x, ball.rect.y = 375, 250
        ball.d_x = -1
        board1.points += 1


def board2_get_point(): 
    """ When the coordinate of the ball on the x-axis is smaller than 0, 
        the ball moves to the center and board 2 gets a point.
    """ 
    if ball.rect.x < 0:
        ball.rect.x, ball.rect.y = 375, 250
        ball.d_x = 1
        board2.points += 1


def ball_move():  
    ball.rect.x += ball.speed * ball.d_x
    ball.rect.y += ball.speed * ball.d_y

    if ball.rect.y > 590:
        ball.d_y = -1

    if ball.rect.y < 0:
        ball.d_y = 1

    if board1.rect.colliderect(ball.rect):
        ball.d_x = 1
        mixer.Sound.play(pongSound)

    if board2.rect.colliderect(ball.rect):
        ball.d_x = -1
        mixer.Sound.play(pongSound)


def pause():
    paused = True
    pygame.mixer.music.stop()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        pause_text()
        pygame.display.update()


def start():
    pygame.mixer.music.stop()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        start_text()
        pygame.display.update()


def end():
    pygame.mixer.music.stop()
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        end_text()
        pygame.display.update()


def redraw():  
    screen.fill((255, 62, 150))
    game_texts()
    all_sprites.draw(screen)
    pygame.display.update()
    keyboard()
    boards_max_positions()
    ball_move()
    board1_get_point()
    board2_get_point()

def game_loop():   
    while board1.points != 20 and board2.points != 20:  
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        redraw()

while True:
    board1.points = 0
    board2.points = 0
    start()
    game_loop()
    end()
