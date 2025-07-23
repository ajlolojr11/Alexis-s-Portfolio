# Final Project
# Program: Pong Clone
# Alexis Varas Ortiz
# Description: A clone of the game pong, a 2D version of ping pong.

import pygame, sys
from pygame.locals import *

#Globals
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 80)
font2 = pygame.font.SysFont(None, 16)
pygame.display.set_caption("Pong Clone")
screen = pygame.display.set_mode((1280, 720))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)


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

class Player2(Paddles):
    def __init__(self, surface, colr, position=(20, 351)):
        super().__init__(surface, colr, position)

    def update(self):
        ...


def main():
    fps = pygame.time.Clock()
    player1 = Paddles(screen, white)
    player2 = Player2(screen, white, position=(1250,351))
    ball = Ball(screen, white)
    score1 = 0
    score2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)  
        draw_game(player1, player2, ball, score1, score2)        

        player1.update()
        player2.update() 
        ball.update() 

        pygame.display.update()
        fps.tick(60)  #sets fps

    

def draw_game(p1, p2, b, s1, s2):
    #create the interactable objects
    p1.create()
    p2.create()
    b.create()   

    #Draws middle dotted line
    middle_line = 70
    while middle_line < 690:
        pygame.draw.rect(screen, white, pygame.Rect(637.5, middle_line, 5, 20))
        middle_line += 60
    middle_line = 70

    #Draw borders
    pygame.draw.rect(screen, white, pygame.Rect(15, 70, 1250, 1)) #top border
    pygame.draw.rect(screen, white, pygame.Rect(15, 690, 1250, 1)) #bottom border
    pygame.draw.rect(screen, red, pygame.Rect(15, 70, 1, 620)) #left border
    pygame.draw.rect(screen, red, pygame.Rect(1265, 70, 1, 620)) #right border
    
    #Draw Title and scores
    screen.blit(font.render(str("Pong"), True, white) , (570, 5))
    screen.blit(font2.render(str("Clone"), True, white) , (710, 50))
    screen.blit(font.render(str(s1), True, white) , (550, 90))
    screen.blit(font.render(str(s2), True, white), (690, 90))

def score_point():
    ...

def bounce():
    ...

if __name__ == "__main__":
    main()


