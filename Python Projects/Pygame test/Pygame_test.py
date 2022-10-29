import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class TicTacToe:
    def __init__(self):
        self.grid = [[0] * 3, [0] * 3, [0] * 3]

        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        self.x_test = font.render("x", True, (255, 255, 255))
        self.o_test = font.render("x", True, (255, 255, 255))

        self.current_turn = 1

    def draw(self, screen):
        #draw vertical lines
        pygame.draw.rect(
            )

    def handle_mouse_click(self, pos):
        x, y = pos
        x = int(x / (WINDOW_WIDTH / 3))
        y = int(y / (WINDOW_WIDTH / 3))
        self.grid[y][x] = 1

        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1



def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    tictactoe = TicTacToe()

    background_color - [0, 0, 0]
    running = True
