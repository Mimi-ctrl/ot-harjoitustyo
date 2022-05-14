import sys
import pygame
from files import sound, screen
from sprites.board import Board1, Board2
from sprites.ball import Ball
from text import game_texts, end_text, start_text, pause_text

board1 = Board1()
board2 = Board2()
ball = Ball()
BOARD_SPEED = 50
all_sprites = pygame.sprite.Group()
all_sprites.add(board1, board2, ball)


def __init__(self):
    self.points = 0

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


def board_get_point():
    """ When the coordinate of the ball on the x-axis is bigger than 690,
        the ball moves to the center and board 1 gets a point.
        When the coordinate of the ball on the x-axis is smaller than 0,
        the ball moves to the center and board 2 gets a point.
    """
    if ball.rect.x > 690:
        ball.rect.x, ball.rect.y = 375, 250
        ball.d_x = -1
        board1.points += 1

    if ball.rect.x < 0:
        ball.rect.x, ball.rect.y = 375, 250
        ball.d_x = 1
        board2.points += 1


def ball_move():
    """ Control the coordinates of the ball on the playing field by
        changing its x and y coordinates. This is done by multiplying by
        one or minus one the speed of the ball. If the y-coordinate of the
        ball is less than or greater than the y-coordinates of the playing area,
        the direction of the ball with the y-coordinate is reversed by changing
        one to positive or negative. If the coordinate of the ball on the x-axis
        is the same as on the board then the direction on the x-axis is reversed
        and a sound effect is played.
    """
    ball.rect.x += ball.speed * ball.d_x
    ball.rect.y += ball.speed * ball.d_y

    if ball.rect.y > 590:
        ball.d_y = -1

    if ball.rect.y < 0:
        ball.d_y = 1

    if board1.rect.colliderect(ball.rect):
        ball.d_x = 1
        sound()

    if board2.rect.colliderect(ball.rect):
        ball.d_x = -1
        sound()

def keyboard():
    """ Performs the function when the key is pressed.
        For example, pressing the down or up arrow key moves the board.
    """
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

def pause():
    """ When calling a pause, the pause mode is set to true and the pause text
        is displayed until ENTER is pressed and the pause mode is false.
    """
    paused = True
    pygame.mixer.music.stop()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pause_text()
        pygame.display.update()


def start():
    board1.points = 0
    board2.points = 0
    pygame.mixer.music.stop()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        start_text()
        pygame.display.update()


def end():
    pygame.mixer.music.stop()
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
    board_get_point()


def game_loop():
    while board1.points != 20 and board2.points != 20:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        redraw()
        