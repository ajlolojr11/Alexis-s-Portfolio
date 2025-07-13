# Final Project
# Program: Pong Clone
# Alexis Varas Ortiz
# Description: A clone of the game pong, a 2D version of ping pong.
#              DON'T LET THE BALL GO PAST YOU!


#test
import pygame, sys
from pygame.locals import *

#Globals
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 90)
pygame.display.set_caption("Pong Clone")
screen = pygame.display.set_mode((1280, 720))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


class Paddles:
    def __init__(self, surface, colr, position = (20,351)):
        self._surface = surface
        self._colr = colr
        self._position = position
        self.rect = pygame.Rect(self._position, (10,70))

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,10)

        if self.rect.top < 50:
            self.rect.top = 50
        if self.rect.bottom > 670:
            self.rect.bottom = 670

    def create(self):
        pygame.draw.rect(self._surface, self._colr, self.rect)

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position
    
    @property
    def colr(self):
        return self._colr
    
    @property
    def surface(self):
        return self._surface


class Ball(Paddles):
    def __init__(self, surface, colr):
        super().__init__(surface, colr)
        self._position = (640,351)
        self._size = 10

    def create(self):
        pygame.draw.circle(self._surface, self._colr, self._position, self._size)

    @property
    def size(self):
        return self._size
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position


def main():
    fps = pygame.time.Clock()
    top_border = pygame.Rect(20, 50, 1240, 1)
    bottom_border = pygame.Rect(20, 670, 1240, 1)
    middle_line = 50
    player1 = Paddles(screen, white)
    player2 = Paddles(screen, white, position=(1250,351))
    ball = Ball(screen, white)
    score1 = 0
    score2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)          

        player1.update()
        player2.update() 

        while middle_line < 670:
            pygame.draw.rect(screen, white, pygame.Rect(637.5, middle_line, 5, 20))
            middle_line += 60
        middle_line = 50

        pygame.draw.rect(screen, white, top_border)
        pygame.draw.rect(screen, white, bottom_border)

        counter(score1, score2)

        player1.create()
        player2.create()
        ball.create()    

        pygame.display.update()
        fps.tick(60)  # limits FPS to 60

    

def counter(score1, score2):
    player1_score = font.render(str(score1), True, white)
    player2_score = font.render(str(score2), True, white)
    screen.blit(player1_score , (550, 70))
    screen.blit(player2_score, (690, 70))


def score_point():
    ...

def bounce():
    ...

if __name__ == "__main__":
    main()


