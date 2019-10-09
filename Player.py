from Board import Board
from Ship import Ship
import utils


class Player:
    def __init__(self, player_number, ships=[]):
        self.__ship = Ship()
        self.__player_number = player_number
        self.__player_board = Board()
        self.__player_name = ""
        self.__ship_coordinates = ships
        self.__player_shots = []
        self.__number_of_hits = 0
        self.__is_turn = False

    def reset_player(self):
        ### Clears all player information ###
        self.player_name = ""
        self.ship_coordinates = self.ship_coordinates.clear()
        self.player_shots = self.player_shots.clear()

    # setter done in constructor
    @property  # getter
    def player_number(self):
        return self.__player_number

    # setter done in constructor
    @property  # getter
    def board(self):
        return self.__player_board

    @property  # getter
    def is_turn(self):
        return self.__is_turn

    @is_turn.setter  # setter
    def is_turn(self, value):
        self.__is_turn = value

    @property  # getter
    def player_name(self):
        return self.__player_name

    @player_name.setter  # setter
    def player_name(self, value):
        self.__player_name = value

    @property  # getter
    def ship_coordinates(self):
        return self.__ship_coordinates

    @ship_coordinates.setter  # setter
    def ship_coordinates(self, value):
        self.__ship_coordinates.append(value)
        print(self.ship_coordinates)

    @property  # getter
    def player_shots(self):
        return self.__player_shots

    @player_shots.setter  # setter
    def player_shots(self, value):
        self.__player_shots.append(value)

    @property  # getter
    def ship(self):
        return self.__ship

    @property  # getter
    def number_of_hits(self):
        return self.__number_of_hits

    @number_of_hits.setter  # setter
    def number_of_hits(self, value):
        self.__number_of_hits = self.__number_of_hits + value

    def get_and_set_players_ship_locations(self):
        ###
        # gets the players ship coords via an input
        # then validates it is correct
        # if correct it passes the coord to the correct function
        ###
        if self.ship_coordinates[0] == None:
            self.ship_coordinates.pop(0)
        while len(self.ship_coordinates) < self.ship.ship_length * 2:
            print("place ship:")
            ship = input("Please enter a coordinate and direction e.g. a1v: ")
            if utils.check_ship_coord_valid(ship) == False:
                print("Invalid coordinates entered, please try again.")
            else:
                formatted_coord = utils.convert_coord(ship)
                if any(d['x'] == formatted_coord['x'] and d['y'] == formatted_coord['y'] for d in self.ship_coordinates):
                    print("There is already a ship in this location, please try again")
                else:
                    self.place_ship_on_players_board(formatted_coord)
                    self.board.print_player_board(
                        self.ship_coordinates, self.player_shots)

    def place_ship_on_players_board(self, formatted_coord):
        ###
        # appends ship coordinates to the ship_coordinates list
        # Keyword arguments:
        # formatted_coord - a dictionary in the {x:x,y:y,d:d} format
        ###
        new_y = formatted_coord['x']
        new_x = formatted_coord['y']
        direction = formatted_coord['d']
        loops = 0
        length = self.ship.ship_length

        # checks the ship direction and generates three coordinates based on
        # supplied coordinate dictionary
        if direction == "v":
            i = new_x
            while loops < length:
                self.ship_coordinates = {
                    "x": i, "y": new_y, "direction": direction
                }
                if new_x >= 3:
                    i -= 1
                else:
                    i += 1
                loops += 1
        else:
            i = new_y
            while loops < length:
                self.ship_coordinates = {
                    "x": new_x, "y": i, "direction": direction
                }
                if new_y >= 3:
                    i -= 1
                else:
                    i += 1
                loops += 1

    def pew_pew(self, opposition_ships):
        ###
        # gets a shot coordinate string via an input, validates it and if
        # valid appends it to the player_shots list.
        # Keyword arguments:
        # opposition_ships - list of all opposition ship coordinates, used
        #   to check if the shot is a miss or hit
        shot = input("please enter a coordinate for your shot e.g a1: ")
        if utils.check_shot_coord_valid(shot):
            formatted_coord = utils.convert_shot_coord(shot)
            y = formatted_coord['x']
            x = formatted_coord['y']
            # check to see if shot already taken
            if not any(d['x'] == x and d['y'] == y for d in self.player_shots):
                self.player_shots = {"x": x, "y": y}
                # check to see if shot is hit or miss
                if any(d['x'] == x and d['y'] == y for d in opposition_ships):
                    self.number_of_hits = 1
                    print("hit")
                else:
                    print("miss")
            else:
                # Shot already taken
                print("You have already taken a shot there, please try again")
                self.pew_pew(opposition_ships)
        else:
            # shot coordinates not valid
            print("Invalid coordinates, please try again")
            self.pew_pew(opposition_ships)
