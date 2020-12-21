from enum import Enum, unique, auto

from Board import Board
from Computer import Computer
from Heap import Heap
from Info import Info
from Pip import Pip
from Render import Render
from User import User


@unique
class Player(Enum):
    USER = auto()
    COMPUTER = auto()


class Game:

    def __init__(self):
        self.__heap: Heap = Heap(7)
        self.__info: Info = Info()
        self.__board: Board = Board()
        self.__computer: Computer = Computer(self.__heap, self.__board)
        self.__user: User = User(self.__heap, self.__board, self.__info)
        self.__render: Render = Render(self.__heap, self.__board, self.__info, self.__computer, self.__user)
        self.__user.set_render(self.__render.render)
        self.__computer.set_render(self.__render.render)
        self.__player: Player = self.select_first()

    def run(self) -> None:
        game_end: bool = False

        while not game_end:
            self.__info.set_current_player(self.get_current_player())
            self.__render.render()
            firstActionResult: bool = self.move()
            if self.is_player_done():
                game_end = True
                continue
            self.next()

            self.__info.set_current_player(self.get_current_player())
            self.__render.render()
            secondActionResult: bool = self.move()
            if self.is_player_done():
                game_end = True
                continue
            self.__info.set_current_player(self.get_current_player())
            self.next()

            if not firstActionResult and not secondActionResult:
                game_end = True

        self.__render.render_score()

    def get_current_player(self) -> str:
        if self.__player == Player.COMPUTER:
            return 'Computer'
        elif self.__player == Player.USER:
            return 'You'

    def is_player_done(self) -> bool:
        if self.__player == Player.COMPUTER:
            return self.__computer.pips_count() == 0
        elif self.__player == Player.USER:
            return self.__user.pips_count() == 0

    def next(self) -> None:
        if self.__player == Player.USER:
            self.__player = Player.COMPUTER
        elif self.__player == Player.COMPUTER:
            self.__player = Player.USER

    def move(self) -> bool:
        if self.__player == Player.USER:
            return self.__user.move()
        elif self.__player == Player.COMPUTER:
            return self.__computer.move()

    def select_first(self) -> Player:
        pips: list[Pip] = self.__user.get_pips()
        user_min: int = 13
        user_duplicate_min: int = 7
        for pip in pips:
            if not pip.is_zero():
                if not pip.is_duplicate():
                    user_min = min(user_min, pip.get_score())
                else:
                    user_duplicate_min = min(user_duplicate_min, pip.get_top())

        pips: list[Pip] = self.__computer.get_pips()
        computer_min: int = 13
        computer_duplicate_min: int = 7
        for pip in pips:
            if not pip.is_zero():
                if not pip.is_duplicate():
                    computer_min = min(computer_min, pip.get_score())
                else:
                    computer_duplicate_min = min(computer_duplicate_min, pip.get_top())

        if user_duplicate_min is not 7 and user_duplicate_min < computer_duplicate_min:
            return Player.USER
        elif computer_duplicate_min is not 7 and computer_duplicate_min < user_duplicate_min:
            return Player.COMPUTER
        elif user_min < computer_min:
            return Player.USER
        elif computer_min < user_min:
            return Player.COMPUTER
