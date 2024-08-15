from ship import *

from colorama import Fore, Style, init
init()
import string

class single_board:
    # int, int, list[list[int, int]], list[ship] -> single_board
    def __init__(self, length, height, lands, ships):
        self.length = length
        self.height = height

        board = []
        for i in range(0,length):
            vertical_line = []
            for j in range(0,height):
                vertical_line.append([' ', 'placeholder'])
            board.append(vertical_line)

        for land in lands:
            board[land[0]][land[1]] = ['L', 'placeholder']

        for ship in ships:
            for coords_hit_list in ship.ship_array:
                board[coords_hit_list[0][0]][coords_hit_list[0][1]] = [str(ship.id), coords_hit_list[1]]

        self.board = board
        self.lands = lands
        self.ships = ships

        self.hit_list = [] # list of coords that have already been shot at

    # list[int, int] -> bool
    def process_hit(self, coords):
        if self.board[coords[0]][coords[1]][0] == 'L':
            return "land"
        if coords in self.hit_list:
            return "repeat"
        self.hit_list.append(coords)

        for ship in self.ships:
            result = ship.process_hit(coords)
            # print(result)
            if result != "miss":
                break

        if result == "miss" and self.board[coords[0]][coords[1]][0] != 'L':
            self.board[coords[0]][coords[1]] = ['O', 'placeholder']
        if "hit" in result:
            self.board[coords[0]][coords[1]][1] = True
        #     self.board[coords[0]][coords[1]] = ['X', 'placeholder']

        return result

    # -> bool
    def lost_game(self):
        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True

    # string -> void
    def print_for_testing(self, perspective):
        def print_bar():
            bar = "    #"
            for i in range(0, self.length):
                bar += "---#"
            print(bar)
        def print_horizontal_coords(perspective):
            letters = []
            alphabet = string.ascii_uppercase
            for i in range(self.length): # NOTE: only goes up to 702 chars (from A to ZZ)
                quotient, remainder = divmod(i, 26)
                if quotient == 0:
                    letters.append(alphabet[remainder])
                else:
                    letters.append(alphabet[quotient - 1] + alphabet[remainder])
            if perspective != "self":
                letters.reverse()

            output = "     "
            for letter in letters:
                output += letter.center(3, " ") + " "
            print(output)

        if perspective != "self":
            print_horizontal_coords("opponent")
        print_bar()
        for i in range(0, self.height):
            coord_num = 0
            if perspective == "self":
                coord_num = self.height - i
            else:
                coord_num = i + 1
            line = (str(coord_num)).ljust(3, ' ') + " |"
            for j in range(0, self.length):
                height_coord = 0
                length_coord = 0
                if perspective == "self":
                    height_coord = self.height - i - 1
                    length_coord = j
                else:
                    height_coord = i
                    length_coord = self.length - j - 1
                sym = self.board[length_coord][height_coord][0]
                data = self.board[length_coord][height_coord][1]
                output = ""
                if sym == 'L': # for land
                    output = Fore.GREEN + sym + Style.RESET_ALL
                elif sym.isnumeric(): # for ships
                    if data == True: # hit -> show
                        output = Fore.RED + sym + Style.RESET_ALL
                    elif data == False and perspective == "self": # not hit && self board -> show
                        output = Fore.WHITE + sym + Style.RESET_ALL
                    else: # not hit && opponent board -> no show
                        output = ' '
                elif sym == 'O':
                    output = Fore.WHITE + sym + Style.RESET_ALL
                else:
                    output = Fore.WHITE + sym + Style.RESET_ALL
                line += (' ' + output + ' |')
            print(line)
            print_bar()

        if perspective == "self":
            print_horizontal_coords("self")


if __name__ == "__main__":
    ship1 = Ship([[0,0], [1,0], [2,0], [3,0]], 1, False)
    ship1.process_hit([0,0])
    ship1.process_hit([1,0])

    myboard = single_board(6,5,[[0,1], [0,2], [3,4]], [ship1])

    myboard.print_for_testing("opponent")
    myboard.print_for_testing("self")