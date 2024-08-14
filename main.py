from ship import Ship
from board import *
from game import Game

import os
import json


# open json game file
scenario_file = os.path.join("scenarios", "default.json")
with open(scenario_file, 'r') as file:
    scenario_data = json.load(file)


if __name__ == "__main__":
    player_1 = input("Enter name for player 1: ")
    player_2 = input("Enter name for player 2: ")
    gamemode = input("Enter gamemode (just default for now): ")
    gamemode = "default"

    ships_1 = []
    ships_2 = []

    for ship_info in scenario_data["player1_ships"]:
        newship = Ship(ship_info[0], ship_info[1], False)
        ships_1.append(newship)
    for ship_info in scenario_data["player2_ships"]:
        newship = Ship(ship_info[0], ship_info[1], False)
        ships_2.append(newship)

    board_game = Game(player_1, player_2, scenario_data["length"], scenario_data["height"], scenario_data["player1_land"], scenario_data["player2_land"], ships_1, ships_2)

    player_turn = player_1
    #### START GAME LOOP ####
    while True:
        if player_turn == player_1:
            target_player = player_2
        else:
            target_player = player_1

        board_game.print_for_testing(player_turn)
        print(f"Turn: {player_turn}")
        while True:
            attack_coords = input("Enter coordinates in letter-number format (Ex. A6, B12, CK38): ")
            if board_game.process_input(attack_coords, target_player):
                break

        if target_player == player_1:
            if board_game.board1.lost_game():
                print(f"=====Player 2 {player_2} has won=====")
                break
        elif target_player == player_2:
            if board_game.board2.lost_game():
                print(f"=====Player 1 {player_1} has won=====")
                break

        if player_turn == player_1:
            player_turn = player_2
        else:
            player_turn = player_1

        input("Next turn? Press any key to continue:")