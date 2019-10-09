from Board import Board


ships = [{'x': 0, 'y': 0, 'direction': 'v'}, {'x': 1, 'y': 0, 'direction': 'v'}, {'x': 2, 'y': 0, 'direction': 'v'}, {
    'x': 4, 'y': 4, 'direction': 'h'}, {'x': 4, 'y': 3, 'direction': 'h'}, {'x': 4, 'y': 2, 'direction': 'h'}]
board_1 = Board()
board_1.print_player_board(ships, [])
