import re
from random import randint

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

TIE = 0
PLAYER1_WIN = 1
MACHINE_WIN = 2


class TicTacToeGame():
    def __init__(self):
        self.board = [None] * 9
        self.turn = _PLAYER
        self.is_game_over = False
        self.winner = None

    def is_over(self):  # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
        player_win = self.verify_player_win()
        machine_win = self.verify_machine_win()
        win = None
        if player_win:
            self.winner = PLAYER1_WIN
            win = True
        elif machine_win:
            self.winner = MACHINE_WIN
            win = True
        elif machine_win == False and player_win == False and self.board.count(None) == 0:
            self.winner = TIE
        else:
            win = False
        return win

    def verify_player_win(self):
        return all(i == _PLAYER_SYMBOL for i in self.board[0:3]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[3:6]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[6:9]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[0:7:3]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[1:8:3]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[2:9:3]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[::4]) or \
               all(i == _PLAYER_SYMBOL for i in self.board[2:7:2])

    def verify_machine_win(self):
        return all(i == _MACHINE_SYMBOL for i in self.board[0:3]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[3:6]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[6:9]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[0:7:3]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[1:8:3]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[2:9:3]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[::4]) or \
               all(i == _MACHINE_SYMBOL for i in self.board[2:7:2])

    def play(self):
        if self.turn == _PLAYER:
            self.player_turn()
            self.turn = _MACHINE
        else:
            self.machine_turn()
            self.turn = _PLAYER

    def player_choose_cell(self):
        print("Input empty cell bewtween 0 and 8")

        player_cell = input().strip()
        match = re.search("\d", player_cell)

        if not match:
            print("Input is not a number, please try again")

            return self.player_choose_cell()

        player_cell = int(player_cell)

        if self.board[player_cell] is not None:
            print("Cell is already taken, try again")

            return self.player_choose_cell()

        return player_cell

    def player_turn(self):
        chosen_cell = self.player_choose_cell()
        self.board[chosen_cell] = _PLAYER_SYMBOL

    def machine_turn(self):  # TODO: Finish this function by making the machine choose a random cell (use random module)
        turn_finish = False

        while not turn_finish:
            i = randint(0, 8)
            if self.board[i] is None:
                self.board[i] = _MACHINE_SYMBOL
                turn_finish = True

    def format_board(self):
        row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
        row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
        row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

        return "\n".join([row0, row1, row2])

    def print(self):
        print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
        print(self.format_board())
        print()

    def print_result(self):  # TODO: Finish this function in order to print the result based on the *winner*
        if self.winner == TIE:
            print("Has been a Tie")
        elif self.winner == PLAYER1_WIN:
            print("Player has Won")
        else:
            print("Machine has Won")
