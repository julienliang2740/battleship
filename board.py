from colorama import Fore, Style, init
init()
import string

class single_board:
    # int, int, list[tuple(int, int)], dict{?:?} -> single_board
    def __init__(self, length, height, lands, ships):
        self.length = length
        self.height = height

        board = []
        for i in range(0,length):
            vertical_line = []
            for j in range(0,height):
                vertical_line.append(' ')
            board.append(vertical_line)

        self.board = board

        for land in lands:
            board[land[0]][land[1]] = 'L'

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
                sym = self.board[length_coord][height_coord]
                output = ""
                if (sym == 'L'):
                    output = Fore.GREEN + sym + Style.RESET_ALL
                else:
                    output = Fore.RED + sym + Style.RESET_ALL
                line += (' ' + output + ' |')
            print(line)
            print_bar()

        if perspective == "self":
            print_horizontal_coords("self")


if __name__ == "__main__":
    myboard = single_board(6,5,[(0,1), (0,2), (3,4)], {})

    myboard.print_for_testing("opponent")
    myboard.print_for_testing("self")