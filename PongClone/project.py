# Final Project
# Program: Pong Clone
# Alexis Varas Ortiz
# Description: A clone of the game Pong, a 2D version of ping pong.

import pygame, sys, random
from pygame.locals import *

class Paddles(pygame.Rect):
    def __init__(self, surface, colr, position = (20,316)):
        super().__init__(position, (10, 70))  # Initialize the Rect with position and size
        self._surface = surface
        self._colr = colr

    def move(self):
        #Sets keys to move paddles
        #Will only move vertically
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.move_ip(0,-2)
        if pressed_keys[K_DOWN]:
            self.move_ip(0,2)

        #Sets limit on how far up or down they are able to move
        if self.top < 75:
            self.top = 75
        if self.bottom > 685:
            self.bottom = 685

    def create(self):
        pygame.draw.rect(self._surface, self._colr, self)

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
    def __init__(self, surface, colr, position=(640, 351)):
        super().__init__(surface, colr)
        self.center = (640, 351)
        self._size = 10
        self._position = position
        self.xspeed = random.choice([-3, 3])  # horizontal speed
        self.yspeed = 0  # vertical speed

    def move(self):
        self.move_ip(self.xspeed, self.yspeed)
        
    def create(self):
        pygame.draw.circle(self._surface, self._colr, self.center, self._size)

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
    def __init__(self, surface, colr, position=(1250, 316)):
        super().__init__(surface, colr, position)
    
    def move(self):
        #Try to follow the ball
        if self.top < ball.top:
            self.move_ip(0, 2)
        if self.bottom > ball.bottom:
            self.move_ip(0, -2)

        #Sets limit on how far up or down they are able to move
        if self.top < 75:
            self.top = 75
        if self.bottom > 685:
            self.bottom = 685


# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up the display and fonts
pygame.display.set_caption("Pong Clone")
font = pygame.font.SysFont(None, 80) 
font2 = pygame.font.SysFont(None, 16)
screen = pygame.display.set_mode((1280, 720))
fps = pygame.time.Clock()

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Create game objects
player1 = Paddles(screen, white)
player2 = Player2(screen, white)
ball = Ball(screen, white)
top_border = pygame.Rect(15, 67, 1250, 3) 
bottom_border = pygame.Rect(15, 690, 1250,3) 
left_border = pygame.Rect(15, 70, 1, 620) 
right_border = pygame.Rect(1265, 70, 1, 620)

# Initialize scores and bouces
score1 = 0
score2 = 0
bounces = 0


def main():

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)  
          
        check_collision()
        move_objects()
        draw_game()   
        
        pygame.display.update()
        fps.tick(120)  #sets fps

def draw_game():

    #create the interactable objects
    player1.create()
    player2.create()
    ball.create()   

    #Draws middle dotted line
    middle_line = 70
    while middle_line < 690:
        pygame.draw.rect(screen, white, pygame.Rect(637.5, middle_line, 5, 20))
        middle_line += 60
    middle_line = 70

    #Draw borders
    pygame.draw.rect(screen, white, top_border) #top border
    pygame.draw.rect(screen, white, bottom_border) #bottom border
    pygame.draw.rect(screen, red, left_border) #left border
    pygame.draw.rect(screen, red, right_border) #right border
    
    #Draw Title and scores
    screen.blit(font.render(str("Pong"), True, white) , (570, 5))
    screen.blit(font2.render(str("Clone"), True, white) , (710, 50))
    screen.blit(font.render(str(score1), True, white) , (550, 90))
    screen.blit(font.render(str(score2), True, white), (690, 90))

def check_collision():
    global score1, score2, bounces

    # Check for collisions with paddles and borders
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball.xspeed = -ball.xspeed
        #Randomize the angle of the ball's bounce
        ball.yspeed = -(random.randrange(-3, 3))
        #Increase ball speed every 5 bounces without scoring
        bounces +=1
        if bounces == 5:
            if ball.xspeed > 0:
                ball.xspeed += 1
            else:
                ball.xspeed -= 1
            bounces = 0
                                

    elif ball.colliderect(top_border) or ball.colliderect(bottom_border):
        # If the ball hits the top or bottom border, reverse its y direction
        ball.yspeed = -ball.yspeed

    elif ball.colliderect(left_border):
        score_goal(ball.center[0])

    elif ball.colliderect(right_border):
        score_goal(ball.center[0])

def move_objects():
    player1.move()
    player2.move()
    ball.move()

def score_goal(position):
    global bounces, score1, score2

    # Display the score when a goal is scored
    if position < 640:
        screen.blit(font.render("Player 2 Scored!", True, white), (400, 350))
        score2 += 1
        ball.center = (960, 351)       
        ball.xspeed = -3  # Reset horizontal speed
    else:
        screen.blit(font.render("Player 1 Scored!", True, white), (400, 350))
        score1 += 1
        ball.center = (320, 351) 
        ball.xspeed = 3  # Reset horizontal speed

    # Check if either player has reached the score limit
    if score1 >= 5 or score2 >= 5:
        reset_game()
        return

    #Reset paddles, bounce count, and randomize serve angle
    player1.top = 316
    player2.top = 316
    ball.yspeed = random.randrange(-2, 2)  # Random serve angle  
    bounces = 0 


    #Display scoring message and pause for a second
    pygame.display.update()
    pygame.time.delay(1000)
    
    #Redaw game and pause for a second to show ball starting position
    screen.fill(black)  # Clear the screen
    draw_game()  # Redraw the game objects
    pygame.display.update()
    pygame.time.delay(1000)

def reset_game():
    global score1, score2, bounces

    score1 = 0
    score2 = 0
    ball.center = (640, 351)
    ball.xspeed = random.choice([-3, 3])
    ball.yspeed = 0

    if score1 >= 5:
        screen.blit(font.render("Winner!", True, white), (400, 350))
        screen.blit(font.render("Player 1", True, white), (400, 450))
    else:
        screen.blit(font.render("Winner!", True, white), (400, 350))
        screen.blit(font.render("Player 1", True, white), (400, 450))

    pygame.time.delay(2000)
    

if __name__ == "__main__":
    main()


