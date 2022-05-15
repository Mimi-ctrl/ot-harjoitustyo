import sys
import pygame
from files import sound, SCREEN
from sprites.board import Board1, Board2
from sprites.ball import Ball
from text import game_texts, end_text, start_text, pause_text

BOARD1 = Board1()
BOARD2 = Board2()
BALL = Ball()
BOARD_SPEED = 50
ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES.add(BOARD1, BOARD2, BALL)

def boards_max_positions():
    """ Determines the maximum positions of the boards.
        If boards coordinate in y axel is bigger than 525 or smaller than 0,
        boards coordinate in y axel not getting bigger or smaller.
    """
    if BOARD1.rect.y <= 0:
        BOARD1.rect.y = 0
    if BOARD2.rect.y <= 0:
        BOARD2.rect.y = 0
    if BOARD1.rect.y >= 525:
        BOARD1.rect.y = 525
    if BOARD2.rect.y >= 525:
        BOARD2.rect.y = 525


def board_get_point():
    """ When the coordinate of the BALL on the x-axis is bigger than 690,
        the BALL moves to the center and board 1 gets a point.
        When the coordinate of the BALL on the x-axis is smaller than 0,
        the BALL moves to the center and board 2 gets a point.
    """
    if BALL.rect.x > 690:
        BALL.rect.x, BALL.rect.y = 375, 250
        BALL.d_x = -1
        BOARD1.points += 1

    if BALL.rect.x < 0:
        BALL.rect.x, BALL.rect.y = 375, 250
        BALL.d_x = 1
        BOARD2.points += 1


def ball_move():
    """ Control the coordinates of the BALL on the playing field by
        changing its x and y coordinates. This is done by multiplying by
        one or minus one the speed of the BALL. If the y-coordinate of the
        BALL is less than or greater than the y-coordinates of the playing area,
        the direction of the BALL with the y-coordinate is reversed by changing
        one to positive or negative. If the coordinate of the BALL on the x-axis
        is the same as on the board then the direction on the x-axis is reversed
        and a sound effect is played.
    """
    BALL.rect.x += BALL.speed * BALL.d_x
    BALL.rect.y += BALL.speed * BALL.d_y

    if BALL.rect.y > 590:
        BALL.d_y = -1

    if BALL.rect.y < 0:
        BALL.d_y = 1

    if BOARD1.rect.colliderect(BALL.rect):
        BALL.d_x = 1
        sound()

    if BOARD2.rect.colliderect(BALL.rect):
        BALL.d_x = -1
        sound()

def keyboard():
    """ Performs the function when the key is pressed.
        For example, pressing the down or up arrow key moves the board.
    """
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        BOARD1.rect.y -= BOARD_SPEED
    if key[pygame.K_s]:
        BOARD1.rect.y += BOARD_SPEED
    if key[pygame.K_UP]:
        BOARD2.rect.y -= BOARD_SPEED
    if key[pygame.K_DOWN]:
        BOARD2.rect.y += BOARD_SPEED
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
    """ When the start is called, the scores on the boards are reset,
        the music is put off and the intro is set to true. The initial
        view is repeated until the player presses enter to start the
        game and the value of the intro becomes false or esc at which point the game window closes.
    """
    BOARD1.points = 0
    BOARD2.points = 0
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
    """ When the end is called, the music goes off and the value of the end is given as true.
        Then repeat the end view until you press enter, at which point the end value becomes
        false and a new game or esc begins to exit the game.
    """
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
    """ Call functions, define the size of the game window, and draw objects in the game view.
    """
    SCREEN.fill((255, 62, 150))
    game_texts()
    ALL_SPRITES.draw(SCREEN)
    pygame.display.update()
    keyboard()
    boards_max_positions()
    ball_move()
    board_get_point()


def game_loop():
    """ Call redraw until one of the two boards has twenty points.
    """
    while BOARD1.points != 20 and BOARD2.points != 20:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        redraw()
        