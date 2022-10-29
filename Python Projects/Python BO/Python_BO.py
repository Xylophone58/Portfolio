import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def random_angle(speed):
    if random.random() > 0.5:
        y_neg = -1
    else:
        y_neg = 1
    angle = random.random() * 50 + 25
    angle = math.radians(angle)
    vec = [math.cos(angle), math.sin(angle)]
    mag = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
    return [vec[0] / mag * speed, vec[1] / mag * speed * y_neg]

class Pong:
    def __init__(self):
        self.ball_pos = [25, 50]
        # self.ball_speed = [.5, 1]
        self.ball_speed = random_angle(1.25)
        
        self.player_1_pos = 45
        self.player_2_pos = 45
        
        self.player_1_score = 0
        self.player_2_score = 0
        
        self.player_1_font = pygame.font.Font(pygame.font.get_default_font(), 128)
        self.player_2_font = pygame.font.Font(pygame.font.get_default_font(), 128)
        self.player_1_text = self.player_1_font.render("0", True, (128, 128, 128))
        self.player_2_text = self.player_2_font.render("0", True, (128, 128, 128))
        
        self.paddle_size = 25
        self.bounce_count = 0
    
    def draw(self, screen):
        margin = 10
        actual_width = SCREEN_WIDTH - margin * 2
        actual_height = SCREEN_HEIGHT - margin * 2
        
        paddle_height = actual_height * (self.paddle_size / 100)
        paddle_width = actual_width * .02
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            margin, actual_height * (self.player_1_pos / 100) + margin,
            paddle_width, paddle_height
        ))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            SCREEN_WIDTH - margin - paddle_width, actual_height * (self.player_2_pos / 100) + margin,
            paddle_width, paddle_height
        ))
        
        screen.blit(self.player_1_text, pygame.Rect(SCREEN_WIDTH / 2 - self.player_1_text.get_rect().width - 50, 100, 0, 0))
        screen.blit(self.player_2_text, pygame.Rect(actual_width / 2 + 50, 100, 0, 0))
        

        def newball():
            ball_x = (actual_width - 2 * paddle_width) * (self.ball_pos[0] / 100) + margin + paddle_width
            ball_y = actual_height * (self.ball_pos[1] / 100) + margin
            pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), actual_width * .02)

        newball()
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_UP]:
            self.player_2_pos -= 1
        if pressed_keys[pygame.K_DOWN]:
            self.player_2_pos += 1
        self.player_2_pos = max(self.player_2_pos, 0)
        self.player_2_pos = min(self.player_2_pos, 100 - self.paddle_size)
            
        if pressed_keys[pygame.K_w]:
            self.player_1_pos -= 1
        if pressed_keys[pygame.K_s]:
            self.player_1_pos += 1
        self.player_1_pos = max(self.player_1_pos, 0)
        self.player_1_pos = min(self.player_1_pos, 100 - self.paddle_size)
        
        self.ball_pos[0] += self.ball_speed[0]
        self.ball_pos[1] += self.ball_speed[1]
        
        if self.ball_pos[1] <= 2:
            self.ball_pos[1] = 2
            self.ball_speed[1] *= -1
        elif self.ball_pos[1] >= 98:
            self.ball_pos[1] = 98
            self.ball_speed[1] *= -1
            
        if self.ball_pos[0] <= 2:
            paddle_ball_dist = abs(self.ball_pos[1] - (self.player_1_pos + self.paddle_size / 2))
            if paddle_ball_dist <= self.paddle_size / 2 + 1:
                self.ball_pos[0] = 2
                # TODO: This is not a very interesting way to implement how the ball
                # bounces off a paddle...
                self.ball_speed[0] *= -1
                self.bounce_count += 1
                if self.bounce_count == 2:
                    self.paddle_size -= 1
                    self.bounce_count = 0
                    Pong
            else:
                self.player_2_score += 1
                self.player_2_font = pygame.font.Font(pygame.font.get_default_font(), 128 + self.player_2_score * 4)
                self.player_2_text = self.player_2_font.render(f"{self.player_2_score}", True, (128, 128, 128))
                self.ball_pos = [25, 50]
                self.ball_speed = random_angle(1.25)
                self.paddle_size = 25
        elif self.ball_pos[0] >= 98:
            paddle_ball_dist = abs(self.ball_pos[1] - (self.player_2_pos + self.paddle_size / 2))
            if paddle_ball_dist <= self.paddle_size / 2 + 1:
                self.ball_pos[0] = 98
                # TODO: This is not a very interesting way to implement how the ball
                # bounces off a paddle...
                self.ball_speed[0] *= -1
                self.bounce_count += 1
                if self.bounce_count == 2:
                    self.paddle_size -= 1
                    self.bounce_count = 0
            else:
                self.player_1_score += 1
                self.player_1_font = pygame.font.Font(pygame.font.get_default_font(), 128 + self.player_1_score * 4)
                self.player_1_text = self.player_1_font.render(f"{self.player_1_score}", True, (128, 128, 128))
                self.ball_pos = [75, 50]
                self.ball_speed = random_angle(1.25)
                self.ball_speed[0] *= -1
                self.paddle_size = 25

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Pong()
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
