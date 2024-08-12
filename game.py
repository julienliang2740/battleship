from board import *
import string

class Game:
    def __init__(self, player1, player2, length, height, player1_lands, player2_lands, player1_ships, player2_ships):
        self.length = length
        self.height = height
        self.player1 = player1
        self.player2 = player2
        self.board1 = single_board(length, height, player1_lands, player1_ships)
        self.board2 = single_board(length, height, player2_lands, player2_ships)

    def print_for_testing(self, perspective):
        name_adjust = "    "
        if perspective == self.player1:
            print(name_adjust + self.player2.center(4*self.length+1, "-"))
            self.board2.print_for_testing("opponent")
            self.board1.print_for_testing("self")
            print(name_adjust + self.player1.center(4*self.length+1, "-"))
        elif perspective == self.player2:
            print(name_adjust + self.player1.center(4*self.length+1, "-"))
            self.board1.print_for_testing("opponent")
            self.board2.print_for_testing("self")
            print(name_adjust + self.player2.center(4*self.length+1, "-"))
        else:
            print("input error")



if __name__ == "__main__":
    mygame = Game("Briar", "Bramble", 8, 6, [(1,1),(2,2),(3,3)], [(1,0),(2,0),(3,0)], {}, {})

    mygame.print_for_testing("Briar")