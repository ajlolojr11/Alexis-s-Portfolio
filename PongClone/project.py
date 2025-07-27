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
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.move_ip(0,-2) #Upward speed
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.move_ip(0,2) #Downward speed

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
        self.yspeed = 0  # default vertical speed

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
    
    def move(self, ball):
        #AI movement logic
        if self.top < ball.top:
            self.move_ip(0, 2) #Upward speed
        if self.bottom > ball.bottom:
            self.move_ip(0, -2) #Downward speed

        #Sets limit on how far up or down they are able to move
        if self.top < 75:
            self.top = 75
        if self.bottom > 685:
            self.bottom = 685


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    fps = pygame.time.Clock()

    # Set up the display and fonts
    pygame.font.init()
    pygame.display.set_caption("Pong Clone")
    font = pygame.font.SysFont(None, 80) 
    font2 = pygame.font.SysFont(None, 16)

    # Colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)

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

    #Sounds/Volume
    pygame.mixer.init()

    soundtrack = pygame.mixer.Sound("Galaxy.mp3")
    soundtrack.set_volume(0.7)
    soundtrack.play(-1)  # Play soundtrack in a loop

    paddle_hit_sound = pygame.mixer.Sound("paddle_hit.mp3")
    paddle_hit_sound.set_volume(0.6)

    wall_hit_sound = pygame.mixer.Sound("wall_hit.mp3")
    wall_hit_sound.set_volume(0.1)

    goal_sound = pygame.mixer.Sound("score_goal.mp3")
    goal_sound.set_volume(0.4)

    game_over_sound = pygame.mixer.Sound("game_over.mp3")
    game_over_sound.set_volume(0.5)

    #Misc.
    reset = True

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed()[K_r]:
                    score1, score2, bounces, reset = reset_game(player1, player2, ball, screen, font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset)
                if pygame.key.get_pressed()[K_SPACE]:
                    reset = pause_game(player1, player2, ball, screen, font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset)
        
        #Draw all game objects
        draw_game(player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font, font2, score1, score2, white, red, black)

        #Check if the ball collides with any objects
        score1, score2, bounces, reset = check_collision(player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font, font2,
                        score1, score2, white, red, black, green, paddle_hit_sound, wall_hit_sound, goal_sound, game_over_sound, bounces, reset)
        
        #Move the paddles and ball
        move_objects(player1, player2, ball)

        #Freeze screen after each game starts
        while reset:
            pygame.time.delay(1000)  # Wait for a second before resetting
            reset = False  # Exit the reset loop after the delay

        fps.tick(120)  #sets fps

def draw_game(player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font, font2, score1, score2, white, red, black):
    #Clears the screen
    screen.fill(black)

    #create the interactable objects
    player1.create()
    player2.create()
    ball.create()   

    #Draws middle dotted line
    middle_line = 70
    while middle_line < 690:
        pygame.draw.rect(screen, white, pygame.Rect(638, middle_line, 4, 20))
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
    screen.blit(font2.render(str("Press SPACE to pause"), True, white) , (450, 700))
    screen.blit(font2.render(str("Press R to Restart"), True, white) , (700, 700))

    #Refresh the screen
    pygame.display.update()


def move_objects(player1, player2, ball):
    #Calls the move method for each object
    player1.move()
    player2.move(ball)
    ball.move()


def check_collision(player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font, font2,
                    score1, score2, white, red, black, green, paddle_hit_sound, wall_hit_sound, goal_sound, game_over_sound, bounces, reset):
    #Ball hits either paddle
    if ball.colliderect(player1) or ball.colliderect(player2):
        paddle_hit_sound.play()
        ball.xspeed = -ball.xspeed #Reverse horizontal direction of the ball when bouncing off a paddle
        ball.yspeed = -(random.randrange(-3, 3)) #Randomize the angle of the ball's bounce from the paddles
        
        #Increase ball speed every 5 paddle hits
        bounces +=1
        if bounces == 5:
            if ball.xspeed > 0:
                ball.xspeed += 1
            else:
                ball.xspeed -= 1
            bounces = 0
                                
    #Ball hits top or bottom border
    elif ball.colliderect(top_border) or ball.colliderect(bottom_border):
        wall_hit_sound.play()
        ball.yspeed = -ball.yspeed   # If the ball hits the top or bottom border, reverse its y direction

    #Ball hits either goal
    elif ball.colliderect(left_border) or ball.colliderect(right_border):
        goal_sound.play()
        score1, score2, bounces, reset = score_goal(ball.center[0], player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font,
                   font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset)
        
    return score1, score2, bounces, reset


def score_goal(position, player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font,
               font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset):
    # Clear the screen before displaying the score message
    screen.fill(black)

    # Display the score when a goal is scored
    if position < 640: 
        #If ball is on the left side of the screen display "Opponent Scored"
        screen.blit(font.render("Opponent", True, red), (400, 360))
        screen.blit(font.render("Scored", True, white), (700, 360))
        score2 += 1 #Update score for opponent

        # Reset horizontal speed and serve from opponent's side
        ball.center = (960, 351)       
        ball.xspeed = -3 
    else:
        #If ball is on the left side of the screen display "You Scored"
        screen.blit(font.render("You", True, green), (470, 360))
        screen.blit(font.render("Scored", True, white), (590, 360))
        score1 += 1 #Update score for player

        # Reset horizontal speed and serve from your side
        ball.center = (320, 351) 
        ball.xspeed = 3  

    # Check if either player has reached the score limit
    if score1 >= 5 or score2 >= 5:
         score1, score2, bounces, reset = reset_game(player1, player2, ball, screen,font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset)

    #Reset paddles, bounce count, and randomize serve angle
    player1.top = 316
    player2.top = 316
    ball.yspeed = random.randrange(-2, 2)  # Random serve angle  
    bounces = 0 

    #Display scoring message and pause for two seconds
    pygame.display.update()
    pygame.time.delay(2000)
    
    #Redaw game and pause for a second to show ball starting position
    draw_game(player1, player2, ball, screen, top_border, bottom_border, left_border, right_border, font, font2, score1, score2, white, red, black)
    pygame.time.delay(1000)

    return score1, score2, bounces, reset


def reset_game(player1, player2, ball, screen,font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset):
    game_over_sound.play()
    screen.fill(black) #Clear screen

    #Only show "game over" message if either player has reached the score limit
    #(Prevents from running if game is reset prematurely)
    if score1 >= 5 or score2 >= 5:
        # Display game over message and winner
        if score1 > score2:
            screen.blit(font.render("You", True, green), (575, 260))
            screen.blit(font.render("Win!", True, white), (570, 340))
        else:
            screen.blit(font.render("Opponent", True, red), (500, 260))
            screen.blit(font.render("Wins", True, white), (570, 340))

        screen.blit(font.render(f"{score1} - {score2}", True, white), (580, 450))
        screen.blit(font2.render("Try again? Y/N", True, white), (600, 600))
        pygame.display.update()

        #Waiting for user input to continue
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]: #Quit if escape is pressed
                        pygame.quit()
                        sys.exit()
                    if pygame.key.get_pressed()[K_y]: #Restart the game if 'y' is pressed
                        waiting = False
                    elif pygame.key.get_pressed()[K_n]: #Quit the game if 'n' is pressed
                        pygame.quit()
                        sys.exit()

    
    #Reset paddles, bounces, scores, ball position, ball speed, and reset flag
    player1.top = 316
    player2.top = 316
    bounces = 0
    score1 = 0
    score2 = 0
    ball.center = (640, 351)
    ball.xspeed = random.choice([-3, 3])
    ball.yspeed = 0
    reset = True

    return score1, score2, bounces, reset

def pause_game(player1, player2, ball, screen, font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset):
    screen.blit(font2.render("Paused - Press SPACE to continue or 'R' to reset", True, white), (360, 300))
    pygame.display.update()

    #Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_ESCAPE]: #Quit if escape is pressed
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed()[K_r]: #Reset the game if 'r' is pressed
                    score1, score2, bounces, reset = reset_game(player1, player2, ball, screen,font, font2, score1, score2, white, red, black, green, game_over_sound, bounces, reset)
                    reset = True
                    return reset
                if pygame.key.get_pressed()[K_SPACE]: #Resume the game if space is pressed
                    return


if __name__ == "__main__":
    main()


