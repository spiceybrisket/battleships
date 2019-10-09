from Player import Player


player_1_num = 1
player_2_num = 2

player_1 = Player(player_1_num)
player_1.player_name = "Adam"
print(("Player %i's name is %s") % (player_1_num, player_1.player_name))

player_2 = Player(player_2_num)
player_2.player_name = "jasper"
print(("Player %i's name is %s") % (player_2_num, player_2.player_name))

print(player_1)
print(player_2)
