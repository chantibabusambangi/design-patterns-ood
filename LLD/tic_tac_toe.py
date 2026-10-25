from typing import List

#this contains three classes
#player and tictactoegame related by aggragation(1: 2...n)
#and board and tictactoegame related by composition(1: 2...n)
# ---------------- Player ----------------
class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol


# ---------------- Board ----------------
class Board:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[""] * size for _ in range(size)]

        # O(1) winner detection helpers
        self.row_counts = {}
        self.col_counts = {}
        self.diag_counts = {}
        self.anti_diag_counts = {}

    def is_valid_move(self, row: int, col: int) -> bool:
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        return self.grid[row][col] == ""

    def place_move(self, row: int, col: int, player: Player) -> bool:
        if not self.is_valid_move(row, col):
            return False

        symbol = player.symbol
        self.grid[row][col] = symbol

        # Initialize counters for symbol if not present
        self.row_counts.setdefault(symbol, [0] * self.size)
        self.col_counts.setdefault(symbol, [0] * self.size)
        self.diag_counts.setdefault(symbol, 0)
        self.anti_diag_counts.setdefault(symbol, 0)

        # Update counts
        self.row_counts[symbol][row] += 1
        self.col_counts[symbol][col] += 1

        if row == col:
            self.diag_counts[symbol] += 1

        if row + col == self.size - 1:
            self.anti_diag_counts[symbol] += 1

        return True

    def check_winner(self, row: int, col: int, player: Player) -> bool:
        symbol = player.symbol

        return (
            self.row_counts[symbol][row] == self.size
            or self.col_counts[symbol][col] == self.size
            or self.diag_counts[symbol] == self.size
            or self.anti_diag_counts[symbol] == self.size
        )

    def display(self):
        for row in self.grid:
            print(row)
        print()
# ---------------- Game Controller ----------------
class TicTacToeGame:
    def __init__(self, size: int, players: List[Player]):
        self.board = Board(size)
        self.players = players
        self.current_turn = 0
        self.total_moves = 0
        self.max_moves = size * size

    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def play_move(self, row: int, col: int) -> bool:
        player = self.players[self.current_turn]

        if not self.board.place_move(row, col, player):
            print("Invalid Move!")
            return False

        self.total_moves += 1
        self.board.display()

        if self.board.check_winner(row, col, player):
            print(f"{player.name} wins!")
            return True

        if self.total_moves == self.max_moves:
            print("Game Draw!")
            return True

        self.switch_turn()
        return False

    def start_game(self):
        print("Game Started!\n")
        self.board.display()

        while True:
            player = self.players[self.current_turn]
            row, col = map(int, input(f"{player.name} ({player.symbol}) move: ").split())

            if self.play_move(row, col):
                break
player1 = Player("Player1", "X")
player2 = Player("Player2", "O")

game = TicTacToeGame(3, [player1, player2])
game.start_game()
