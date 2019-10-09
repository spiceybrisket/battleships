from os import system, name


def check_ship_coord_valid(coord):
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


def check_shot_coord_valid(coord): a
  is_valid = False

   if len(coord) != 2:
        return is_valid
    elif not coord[0].isalpha():
        return is_valid
    elif not coord[1].isdigit():
        return is_valid
    else:
        y = ord(coord[0].lower())-ord('a')
        x = int(coord[1]) - 1
        if x >= 0 and x <= 4:
            if y >= 0 and y <= 4:
                is_valid = True
                return is_valid
            else:
                return is_valid
        else:
            return is_valid


def clear_screen():
        # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def convert_coord(coord):
    # convert string like "a1v" to x, y coordinates and the direction
    x = ord(coord[0])-ord('a')
    y = int(coord[1]) - 1
    d = coord[2]
    return {"x": x, "y": y, "d": d}


def convert_ship_coord(coord):
    x = ord(coord[0])-ord('a')
    y = int(coord[1]) - 1
    return {"x": x, "y": y}
