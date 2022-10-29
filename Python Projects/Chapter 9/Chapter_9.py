'''
# Because of dynamic typing, we can use any types of values for this functions
# arguments as long as they support +
def add(a, b):
    # if type(a) is dict and type(b) is dict:
    if isinstance(a, dict) and isinstance(b, dict):
        # To handle dictionaries, we'd have to create a special case
        tmp = dict(a)
        tmp.update(b)
        return tmp
    return a + b    
def main():
    print(add(1, 2))
    print(add(1.5, 2.5))
    print(add('1', '2'))
    print(add([1], [2]))
    print(add({'a': 1}, {'b': 2}))
    
main()
'''
class TicTacToe:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2        
        
        self.current_turn = 1
        # 3x3 grid of 0s
        self.grid = [[0] * 3 for _ in range(3)]
        
    def print_grid(self):
        for y in range(3):
            for x in range(3):
                if self.grid[y][x] == 0:
                    print(' ', end='')
                elif self.grid[y][x] == 1:
                    print('X', end='')
                elif self.grid[y][x] == 2:
                    print('O', end='')
                if x != 2:
                    print('|', end='')
            print()
            if y != 2:
                print('-+-+-')
    
    def update(self):
        if self.current_turn == 1:
            x, y = self.player_1.move(self.grid, self.current_turn)
            self.grid[y][x] = self.current_turn
            self.current_turn = 2
        else:
            x, y = self.player_2.move(self.grid, self.current_turn)
            self.grid[y][x] = self.current_turn
            self.current_turn = 1
            
    def status(self):
        """
        Return 1 or 2 if player 1 or 2 respectively as won the game
        Return 0 if no one has won yet
        Return -1 if the game is a tie
        """
        for player in [1, 2]:
            # Check if this player has 3 in a row in any row
            for y in range(3):
                if all(self.grid[y][x] == player for x in range(3)):
                    return player
            # Check if this player has 3 in a row in any column
            for x in range(3):
                if all(self.grid[y][x] == player for y in range(3)):
                    return player
            # Check diagonals
            if all(self.grid[i][i] == player for i in range(3)):
                return player
            if all(self.grid[i][2 - i] == player for i in range(3)):
                return player
        
        # If there is no winner check if there's a tie
        board_full = True
        for y in range(3):
            for x in range(3):
                if self.grid[y][x] == 0:
                    board_full = False
                    break
        if board_full:
            return -1
        else:
            return 0
class HumanPlayer:
    def __init__(self, name):
        self.name = name
    
    def move(self, grid, player_number):
        symbol = "X" if player_number == 1 else "O"
        while True:
            resp = input(f"{self.name}, where do you want to place your {symbol}? ")
            x, y = [int(s) for s in resp.split()]
            if grid[y][x] == 0:
                return x, y
            print("That spot already as a symbol in it!")
    
class AiPlayer:
    def move(self, grid, player_number):
        for y in range(3):
            for x in range(3):
                if grid[y][x] == 0:
                    return x, y
import random
class RandomAiPlayer:
    def move(self, grid, player_number):
        count = 0
        for y in range(3):
            for x in range(3):
                if grid[y][x] == 0:
                    count += 1
        idx = random.randint(0, count - 1)
        count = 0
        for y in range(3):
            for x in range(3):
                if grid[y][x] == 0:
                    if idx == count:
                        return x, y
                    count += 1
        
        '''
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if grid[y][x] == 0:
                return x, y
                '''
def get_selection(options):
    while True:
        print(f"Your options are: {', '.join(options.keys())}")
        resp = input("Which one do you want? ")
        resp = resp.lower().strip() 
        if resp in options:
            return options[resp]
        print("That isn't a valid option")
def main():
    players = {
        'human': HumanPlayer("A"),
        'simple_ai': AiPlayer(),
        'random_ai': RandomAiPlayer(),
    }
    print("Who should player 1 be?")
    player_1 = get_selection(players)
    
    players['human'] = HumanPlayer("B")
    print("Who should player 2 be?")
    player_2 = get_selection(players)
    
    game = TicTacToe(player_1, player_2)
    
    while game.status() == 0:
        game.print_grid()
        game.update()
    
    game.print_grid()
    if game.status() == 1:
        print("Player 1 won")
    elif game.status() == 2:
        print("Player 2 won")
    elif game.status() == -1:
        print("Tie")
main()