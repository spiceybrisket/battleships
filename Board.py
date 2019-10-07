

class Board:
    def __init__(self):
        self._board_size = int = 5
        self._vertical_ship = str = '|'
        self._horizontal_ship = str = '-'
        self._empty_tile = str = 'O'
        self._miss_tile = str = '.'
        self._hit_tile = str = '*'
        self._sunk_tile = str = '#'

    def print_opp_board(self, ship_coordinates, shot_coordinates):
        if ship_coordinates[0] == None:
            ship_coordinates.pop(0)
        board = [[self._empty_tile] *
                 self._board_size for _ in range(self._board_size)]
        print("   " + " ".join([chr(c)
                                for c in range(ord('A'), ord('A') + self._board_size)]))
        for shot in shot_coordinates:
            y = shot["y"]
            x = shot["x"]
            if not any(d['x'] == x and d['y'] == y for d in ship_coordinates):
                board[x][y] = self._miss_tile
            else:
                board[x][y] = self._hit_tile

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def print_player_board(self, ship_coordinates, shot_coordinates):
        if ship_coordinates[0] == None:
            ship_coordinates.pop(0)
        board = [[self._empty_tile] *
                 self._board_size for _ in range(self._board_size)]
        print("   " + " ".join([chr(c)
                                for c in range(ord('A'), ord('A') + self._board_size)]))
        for coord in ship_coordinates:
            y = coord["y"]
            x = coord["x"]
            # update the board at this position
            board[x][y] = self._vertical_ship if coord["direction"] == 'v' else self._horizontal_ship

        # update board with hits and misses
        for shot in shot_coordinates:
            y = shot["y"]
            x = shot["x"]
            if not any(d['x'] == x and d['y'] == y for d in ship_coordinates):
                board[x][y] = self._miss_tile
            else:
                board[x][y] = self._hit_tile

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
        self.print_key()

    def print_key(self):
        multiline_key_str = """
        %s = Vertical Ship, %s = Horizontal Ship, %s = Empty Tile, %s = Miss, %s = Hit
        """ % (self._vertical_ship,
               self._horizontal_ship,
               self._empty_tile,
               self._miss_tile,
               self._hit_tile)

        print(multiline_key_str)

        return multiline_key_str
