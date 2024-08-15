from board import *
import string
import re

class Game:
    def __init__(self, player1, player2, length, height, player1_lands, player2_lands, player1_ships, player2_ships):
        self.length = length
        self.height = height
        self.player1 = player1
        self.player2 = player2
        self.board1 = single_board(length, height, player1_lands, player1_ships)
        self.board2 = single_board(length, height, player2_lands, player2_ships)

    # input format: "A1", "Z99", "AM138" etc
    # str -> str ("bad_input", "miss", "hit", "repeat", "land")
    def process_input(self, input, target_player):
        ## check if it's valid first
        length_coord = 0
        height_coord = 0
        length_str = ""
        height_str = ""

        pattern  = r'^[A-Z]+\d+$'
        if not bool(re.match(pattern, input)):
            print("invalid input - formatting problem")
            return "bad_input"

        for ch in input:
            if ch not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                break
            length_str += ch
        height_str = input.replace(length_str, "")

        factor = 26 ** (len(length_str)-1)
        for ch in length_str:
            length_coord += (ord(ch) - 64) * factor
            factor /= 26
        length_coord -= 1

        height_coord = int(height_str) - 1

        if length_coord > (self.length-1) or length_coord < 0 or height_coord < 0 or height_coord > (self.height-1):
            print("invalid input - out of bounds")
            return "bad_input"
        # print(f"({length_coord}, {height_coord})")

        ## putting the input through to the game
        target_coords = [length_coord, height_coord]
        if target_player == self.player1:
            result = self.board1.process_hit(target_coords)
            self.print_for_testing(self.player2)
        elif target_player == self.player2:
            result = self.board2.process_hit(target_coords)
            self.print_for_testing(self.player1)
        print(f"====={result}=====")

        return result

    def print_for_testing(self, perspective):
        name_adjust = "    "
        if perspective == self.player1:
            print(name_adjust + self.player2.center(4*self.length+1, "-"))
            self.board2.print_for_testing("opponent")
            print(name_adjust + "".center(4*self.length+1, "="))
            self.board1.print_for_testing("self")
            print(name_adjust + self.player1.center(4*self.length+1, "-"))
        elif perspective == self.player2:
            print(name_adjust + self.player1.center(4*self.length+1, "-"))
            self.board1.print_for_testing("opponent")
            print(name_adjust + "".center(4*self.length+1, "="))
            self.board2.print_for_testing("self")
            print(name_adjust + self.player2.center(4*self.length+1, "-"))
        else:
            print("input error")



if __name__ == "__main__":
    ship1_briar = Ship([[0,0], [1,0], [2,0], [3,0]], 1, False)
    ship1_bramble = Ship([[0,0], [1,0], [2,0], [3,0]], 1, False)
    mygame = Game("Briar", "Bramble", 8, 6, [[1,1],[2,2],[3,3]], [[1,1],[2,1],[3,1]], {ship1_briar}, {ship1_bramble})

    mygame.print_for_testing("Bramble")
    mygame.process_input("H6")
    