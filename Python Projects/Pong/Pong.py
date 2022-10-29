import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Pong:
    def __init__(self):
        self.ball_pos = [50, 50]
        self.ball_speed = [1, 1]

        self.player_1_pos = 45
        self.player_2_pos = 45

        self.player_1_score = 0
        self.player_2_score = 0

    def draw(self, screen):
        margin = 10
        actual_width = SCREEN_WIDTH - margin * 2
        actual_height = SCREEN_HEIGHT - margin * 2

        paddle_height = actual_height * .1
        paddle_width = actual_width * .02
        pygame.draw.rect(screen, (255, 255, 255), pygame.rect(
            margin, actual_height * (self.player_1_pos / 100) + margin,
            paddle_width, paddle_height
            ))
        pygame.draw.rect(screen, (255, 255, 255), pygame.rect(
            SCREEN_WIDTH - margin - paddle_width, actual_height * (self.player_2_pos / 100) + margin,
            paddle_width, paddle_height
            ))

        ball_x = (actual_width - 2 * paddle_width) * (self.ball_pos[0] / 100) + margin + paddle_width
        ball_y = actual_height

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP]:
            self.player_2_pos

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Pong()


