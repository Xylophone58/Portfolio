# You'll need to install pygame. To do so, find out where python is installed
# import sys
# print(sys.executable)
#
# Then, open CMD (you can search for it from the start menu) and then run:
# "<the location printed above>" -m pip install pygame
#
# For example, on the lab machines, you run:
# "C:\Program Files\Python38\python.exe" -m pip install pygame
import math
import random
import pygame
# We store the window size in constants so we can make our layout logic relative
# to it and also so we can change it easier later.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Breakout:
    def __init__(self):
        """
        Constructor for the Breakout class. Sets up the initial values for all
        the properties of the object.
        """
        
        # Rect describing the ball's position
        # To do: Set this to a reasonable default
        self.ball_pos = pygame.Rect(0, 0, 0, 0)
        
        # Rect describing the paddle's position
        # To do: Set this to a reasonable default
        self.ball_pos = pygame.Rect(0, 0, 0, 0)
        
        # Create a list of pygame.Rects to represent the bricks. You can
        # manually create this list or you can fill it out with a loop
        self.bricks = [
        ]
    def draw(self, screen):
        "Draws the game pieces to the screen"
        # We're pulling in a little bit from the edges of the screen when
        # drawing, so calculate the screen size less the margins.
        margin = 10
        actual_width = SCREEN_WIDTH - margin * 2
        actual_height = SCREEN_HEIGHT - margin * 2
        paddle_height = actual_width * .02
        paddle_width = actual_height * (self.paddle_size / 100)
        
        # Draw the paddle
        pygame.draw.rect(screen, self.player_1_color, pygame.Rect(
            margin, actual_height * (self.player_1_pos / 100) + margin,
            paddle_width, paddle_height
        ))
        pygame.draw.rect(screen, self.player_2_color, pygame.Rect(
            SCREEN_WIDTH - margin - paddle_width, actual_height * (self.player_2_pos / 100) + margin,
            paddle_width, paddle_height
        ))
        # Draw the bricks
        screen.blit(self.player_1_text, pygame.Rect(SCREEN_WIDTH / 2 - self.player_1_text.get_rect().width - 50, 100, 0, 0))
        screen.blit(self.player_2_text, pygame.Rect(actual_width / 2 + 50, 100, 0, 0))
        # Draw the ball
        ball_x = (actual_width - 2 * paddle_width) * (self.ball_pos[0] / 100) + margin + paddle_width
        ball_y = actual_height * (self.ball_pos[1] / 100) + margin
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), actual_width * .02)
        # Draw the text (score, balls remaining)
    def update(self):
        "Updates the game's state once per frame."
        # Update the ball's location
        
        # Move the paddle based on what keys the user has pressed.
        
        # Check for collisions
        # You can use self.ball_pos.collidelist(self.bricks) to check
        # which if any brick you've hit
        
        # To figure out if you've hit the top/bottom or left/right of a brick,
        # you can use self.ball_pos.clip(collided_brick). That returns a new
        # Rect representing the overlap between the two. If the overlap is wider
        # than tall, the ball hit the top or bottom. If the overlap is taller
        # than wide, the ball it the left or right. If it's equal, you can
        # assume it hit a corner.
        # You can implement the ball bouncing off by negating it's speed in the
        # x or y direction depending on how it has bounced.
        
        # Check if the ball has hit the paddle and bounce it off as appropriate.
        # As above, you reverse the balls y speed to represent the ball bouncing
        # off.
        
        # If the ball missed the paddle, decrease the number of balls remaining
        # and reset the ball's position.
        
# The main method can be left unmodified
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Breakout()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update()
        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()
        # Limit us to 60 fps
        clock.tick(60)
    pygame.quit()
main()
