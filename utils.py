from os import system, name


def check_ship_coord_valid(coord):
    ###
    # checks to see if a coordinate string is valid
    #
    # Keyword arguments:
    # coord - a dictionary in the {x:x,y:y,d:d} format
    ###
    is_valid = False
    if len(coord) < 3:
        return is_valid
    elif not coord[0].isalpha():
        return is_valid
    elif not coord[1].isdigit():
        return is_valid
    elif not coord[2].isalpha():
        return is_valid
    else:
        formmated_coord = convert_coord(coord)
        x = formmated_coord['x']
        y = formmated_coord['y']
        direction = formmated_coord['d']
        if x >= 0 and x <= 4:
            if y >= 0 and y <= 4:
                if direction == "v" or direction == "h":
                    is_valid = True
                    return is_valid
                else:
                    return is_valid
            else:
                return is_valid
        else:
            return is_valid


def check_shot_coord_valid(coord):
    ###
    # checks to see if a coordinate string is valid
    #
    # Keyword arguments:
    # coord - a dictionary in the {x:x,y:y} format
    ###
    is_valid = False

    if len(coord) != 2:
        return is_valid
    elif not coord[0].isalpha():
        return is_valid
    elif not coord[1].isdigit():
        return is_valid
    else:
        formmated_coord = convert_shot_coord(coord)
        x = formmated_coord['x']
        y = formmated_coord['y']
        if x >= 0 and x <= 4:
            if y >= 0 and y <= 4:
                is_valid = True
                return is_valid
            else:
                return is_valid
        else:
            return is_valid


def clear_screen():
    ### clears the terminal screen###
        # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def convert_coord(coord):
    ### convert coord string ro dictionary ###
    x = ord(coord[0])-ord('a')
    y = int(coord[1]) - 1
    d = coord[2]
    return {"x": x, "y": y, "d": d}


def convert_shot_coord(coord):
    ### convert coord string ro dictionary ###
    x = ord(coord[0])-ord('a')
    y = int(coord[1]) - 1
    return {"x": x, "y": y}


def print_instructions():
    ### prints the game instructions###
    print(f'''
    Welcome to the Battleships game

    Aim of the game: Sink all of your opponent's ships

    Setup:
        * Pick a player name
        * Place two ships on board horizontally or vertically by using the vertical and horizontal
          axis listed.
        * ABCDE is listed accross the horizontal axis and 12345 is listed accross the vertical axis.
        * By pairing a letter and a number you can pinpoint a square on the board which allows each
          player to pinpoint an exact place to shoot (or place a ship).
        * The two ships are 3 squares long and cannot be left hanging outside of the board space.
        * An example of a ship setup axis is, "a1H" which will place the first 1/3 of the ship in
          square A1 lying horizontally accross the board.
        * However, another example would be "3Ev" will list the first square of the ship in the "3Ev"
          square standing vertically on the board.

          A B C D E
        1 - - - O O
        2 O O O O O
        3 O O O O |
        4 O O O O |
        5 O O O O |

    Basic rules: Take turns shooting at eachother ships, a hit ship will display as "*" whereas a miss with display "."
   ''')
