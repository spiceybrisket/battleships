# class name: Game
# author: Adam Spice
# date: September 2019

from Player import Player
import utils


class Game:
    def __init__(self):

        self.__player_1 = Player(1)
        self.__player_2 = Player(2)
        self.__game_won = False
        self.__is_winner = ""

    # setter done in constructor
    @property  # getter
    def player_1(self):
        return self.__player_1

    # setter done in constructor
    @property  # getter
    def player_2(self):
        return self.__player_2

    @property  # getter
    def game_won(self):
        return self.__game_won

    @game_won.setter  # setter
    def game_won(self, value):
        self.__game_won = value

    @property  # getter
    def is_winner(self):
        return self.__is_winner

    @is_winner.setter
    def is_winner(self, value):
        self.__is_winner = value

    #
    def player_turn(self, player, opposition):
        # a players turn
        #
        # Keyword arguments:
        # player - the current player instance
        # opposition - the opposing player instance
        #
        ###
        utils.clear_screen()
        print("%s, it's your turn:" % player.player_name)
        input("Press Enter to continue...")
        utils.clear_screen()
        print("\n")
        print("Your shots")
        player.board.print_opp_board(
            opposition.ship_coordinates, player.player_shots)
        print("Your board")
        player.board.print_player_board(
            player.ship_coordinates, opposition.player_shots)
        print("\n")
        print("%s has %i hits, and %s has %i hits" %
              (self.player_1.player_name, self.player_1.number_of_hits,
               self.player_2.player_name, self.player_2.number_of_hits))
        player.pew_pew(opposition.ship_coordinates)
        if player.number_of_hits > 5:
            self.game_won = True
            self.is_winner = player.player_name
        else:
            player.is_turn = False
            opposition.is_turn = True

    def play_game(self):
        ### plays the game until self.game_won becmes true###
        while not self.game_won:
            if self.player_1.is_turn:
                self.player_turn(self.player_1, self.player_2)
                if self.game_won:
                    break
            else:
                self.player_turn(self.player_2, self.player_1)
                if self.game_won:
                    break
        print("%s wins!!" % self.is_winner)

    def setup_game_player(self, player):
        ### Sets up the player's name and ship locations###
        player.reset_player()
        player.player_name = input(
            "Player %i, please enter you name: " % player.player_number)
        print("\n")
        print("Please place your ships: ")
        player.get_and_set_players_ship_locations()
        player.board.print_player_board(
            player.ship_coordinates, player.player_shots)

    def run_game(self):
        utils.print_instructions()
        input("Press Enter to continue...")
        self.player_1.is_turn = True
        self.setup_game_player(self.player_1)
        input("Press Enter to continue...")
        utils.clear_screen()
        self.setup_game_player(self.player_2)
        input("Press Enter to continue...")
        self.play_game()
