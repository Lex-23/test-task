from collections import namedtuple
from collections import Counter


Player = namedtuple('Player', ['name', 'symbol'])


class Game:
    DEFAULT_ELEMENT = "_"
    PLAYERS = []

    def __init__(self, board_size: tuple = (7, 6), players_count: int = 2):
        self.board = [[self.DEFAULT_ELEMENT for _ in range(board_size[0])] for _ in range(board_size[1])]
        self.players_count = players_count
        if self.players_count < 2:
            print("There have to be 2 players at least!")
            raise Exception

    def _print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-------------')

    def _move(self, player: Player):
        column = int(input(f"{player.name} move: "))
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][column] == self.DEFAULT_ELEMENT:
                self.board[row][column] = player.symbol
                break
            else:
                print("It is an impossible move. Retry please")
                self._move(player)

    def _check_board(self, player: Player):
        def is_sublist(sublist, mainlist):
            sublist_str = ''.join(map(str, sublist))
            mainlist_str = ''.join(map(str, mainlist))
            return sublist_str in mainlist_str

        for row in self.board:
            if Counter(row)[player.symbol] == 4 and is_sublist([player.symbol * 4], row):
                print(f'{player.name} has win!')

    def start_game(self):
        for player in range(self.players_count):
            name = input("Input your name: ")
            symbol = input("Input your symbol to play: ")
            self.PLAYERS.append(Player(name, symbol))

        while True:
            for player in self.PLAYERS:
                self._move(player)
                self._check_board(player)
                self._print_board()


game = Game()
game.start_game()
