# Final Project
# Program: Test PongClone/project.py
# Alexis Varas Ortiz
# Description: test the functions/output in project.py

import pygame, pytest
from project import move_objects, reset_game, score_goal, Paddles, Player2, Ball



def test_move_objects():
    screen = pygame.display.set_mode((1280, 720))
    white = pygame.Color(255, 255, 255)

    player1 = Paddles(screen, white, (20,250))
    player2 = Player2(screen, white, (1250, 320))
    ball = Ball(screen, white, (640, 351))

    move_objects(player1, player2, ball)

    assert player1.center == (25, 285) #Does not move without input
    assert player2.center == (1255, 353) #Moves towards ball. Center is originally at (1255, 355)
    assert ball.center == (637, 351) or ball.center == (643, 351) #Movement is initially set randomly left or right 3 pixels per frame

def test_reset_game():
    pygame.font.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1280, 720))
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    font = pygame.font.SysFont(None, 80)
    font2 = pygame.font.SysFont(None, 16)
    green = pygame.Color(0, 255, 0)
    score1 = 2
    score2 = 1
    bounces = 1
    reset = False

    player1 = Paddles(screen, white, (20, 160))
    player2 = Player2(screen, white, (1250, 400))
    ball = Ball(screen, white, (122, 504))


    score1, score2, bounces, reset = reset_game(player1, player2, ball, screen,font, font2,
               score1, score2, white, red, black, green, bounces, reset)


    assert score1 == 0
    assert score2 == 0
    assert bounces == 0
    assert reset == True
    assert player1.center == (25, 351)
    assert player2.center == (1255, 351)
    assert ball.center == (640, 351)
    assert ball.xspeed == 3 or ball.xspeed == -3
    assert ball.yspeed == 0

def test_score_goal():
    pygame.font.init()
    screen = pygame.display.set_mode((1280, 720))
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    font = pygame.font.SysFont(None, 80)
    font2 = pygame.font.SysFont(None, 16)
    green = pygame.Color(0, 255, 0)
    score1 = 2
    score2 = 3
    bounces = 3
    reset = False

    top_border = pygame.Rect(15, 67, 1250, 3)
    bottom_border = pygame.Rect(15, 690, 1250,3)
    left_border = pygame.Rect(15, 70, 1, 620)
    right_border = pygame.Rect(1265, 70, 1, 620)
    player1 = Paddles(screen, white, (20, 160))
    player2 = Player2(screen, white, (1250, 400))
    ball = Ball(screen, white, (15, 504))

    score_goal(ball.center[0], player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font,
               font2, score1, score2, white, red, black, green, bounces, reset)

    assert score1 == 2
    assert score2 == 4
    assert bounces == 0
    assert reset == True
    assert player1.top == 316
    assert player2.top == 316
    assert ball.center == (960, 351)
    assert ball.xspeed == -3
    assert ball.yspeed == 0
    assert reset == True


'''def test_check_collision():
    ...'''
