BOARD_SIZE = 5

SHIP_INFO = [
    ("Battleship", 3),
    ("Submarine", 3),
]

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()


class Player():
    def __init__(self, name):
        self.board = Board()
        self.ships = []
        self.guesses = []


class Board:
    def __init__(self):
        self.board = []
        self.guesses = []

    board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def add_ship(self, name, size, player, coords, direction):
        for coord in coords:
            # convert string like "a1" to x,y coordinates
            y = ord(coord[0])-ord('a')
            x = int(coord[1:])-1
            # update the board at this position
            self.board = board[x][y]
        print("   " + " ".join([chr(c)
                                for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
        self.board.append(Ship(coords, player, name, size, direction))


class Ship:

    def __init__(self, ship_name, size, coords, player, direction):
        self.ship_name = ship_name
        self.size = size
        self.player = player
        self.coords = coords
        self.direction = direction
