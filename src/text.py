import pygame
from files import screen
import game_loop

yellow = 255, 255, 0
red = 255,0,0

def game_texts():
    bong_font = pygame.font.SysFont("D050000L", 300)
    text = bong_font.render("H", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (375, 250)
    screen.blit(text, text_rect)

    points_font = pygame.font.SysFont("Lobster two", 40)
    p1_points = points_font.render(f"Pelaaja 1: {str(game_loop.board1.points)}", False, yellow)
    p1_rect = p1_points.get_rect()
    p1_rect.center = (750 // 3, 25)
    screen.blit(p1_points, p1_rect)

    p2_points = points_font.render(f"Pelaaja 2: {str(game_loop.board2.points)}", False, yellow)
    p2_rect = p2_points.get_rect()
    p2_rect.center = (550, 25)
    screen.blit(p2_points, p2_rect)

def start_text():
    screen.fill((255, 62, 150))
    bong_font = pygame.font.SysFont("Lobster two", 35)
    second_bong_font = pygame.font.SysFont("Lobster two", 60)
    text = second_bong_font.render("PONG", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (350, 100)
    screen.blit(text, text_rect)
    text1 = bong_font.render("Aloita/jatka: ENTER Poistu: ESC Tauko: p", False, yellow)
    text_rect1 = text1.get_rect()
    text_rect1.center = (350, 300)
    screen.blit(text1, text_rect1)

def end_text():
    screen.fill((255, 62, 150))
    bong_font = pygame.font.SysFont("Lobster two", 45)
    winner = ""
    if game_loop.board1.points > game_loop.board2.points:
        winner = "Pelaaja 1"
    if game_loop.board1.points < game_loop.board2.points:
        winner = "Pelaaja 2"
    text = bong_font.render(f"Voittaja: {winner}!!", False, yellow)
    text_rect = text.get_rect()
    text_rect.center = (350, 100)
    screen.blit(text, text_rect)
    text1 = bong_font.render("Uusi peli: ENTER Poistu: ESC", False, yellow)
    text_rect1 = text1.get_rect()
    text_rect1.center = (350, 300)
    screen.blit(text1, text_rect1)

def pause_text():
    bong_font = pygame.font.SysFont("Lobster two", 90)
    text = bong_font.render("Pause", False, red)
    text_rect = text.get_rect()
    text_rect.center = (375, 250)
    screen.blit(text, text_rect)
