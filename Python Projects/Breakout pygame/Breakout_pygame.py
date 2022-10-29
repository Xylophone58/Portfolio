import pygame
import random

pygame.init()
 
# Define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
 
score = 0
lives = 3
 
class Paddle(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the paddle, its width and height.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
 
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
	    #Check that you are not going too far
        if self.rect.x < 0:
          self.rect.x = 0
 
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far
        if self.rect.x > 700:
          self.rect.x = 700

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [random.randint(4,8), random.randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8,8)

class Brick(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the brick, x and y position, width and height.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
 
all_sprites_list = pygame.sprite.Group()
 
#Creating the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
#Creating the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
# Add the paddle and ball to list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
 
# loop will carry on until user exits game
carryOn = True
 
clock = pygame.time.Clock()
 
#Main Program Loop
while carryOn:
    #Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              carryOn = False 
 
    #Moving the paddle when user uses arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)
 
    all_sprites_list.update()
 
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1

        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
 
    #Detect collisions between ball and paddles
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
 
    #Check if ball collides with any bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
 
    # Drawing code should go here
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display score and number of lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    #draw all the sprites
    all_sprites_list.draw(screen)
 
    #update screen
    pygame.display.flip()
 
    #Limit to 60 FPS
    clock.tick(60)
 
#Stop game engine when done
pygame.quit()