import os

from Board import Board
from Computer import Computer
from Heap import Heap
from Info import Info
from Pip import Pip
from User import User
from os import name


class Render:

    def __init__(self, heap: Heap, board: Board, info: Info, computer: Computer, user: User):
        self.__heap: Heap = heap
        self.__board: Board = board
        self.__info: Info = info
        self.__computer: Computer = computer
        self.__user: User = user

    def render(self) -> None:
        table: str = f"""
|---------------------Commands---------------------
| done - finish current move
| take - take pip from heap
| put (left or right) N - put pip into board, where N is number of your pip, direction is optional
|--------------------------------------------------
|  Player: {self.__info.get_current_player()}
|---------------------Computer---------------------
| {self.__render_pips(self.__computer.get_pips(), True)}
|--------------------------------------------------
| Heap [{self.__heap.count()}]
|
| {self.__render_board()}
|-----------------------User-----------------------
| {self.__render_pips(self.__user.get_pips())}
|--------------------------------------------------
| {self.__info.get_error()}
>> """
        self.__clear()
        print(table, end='')

    def __render_board(self) -> str:
        return '-'.join(list(map(lambda pip: self.__render_pip(pip), self.__board.get_pips())))

    def __render_pips(self, pips: list[Pip], hidden: bool = False) -> str:
        rendered_pips: str = ''
        for pip in pips:
            rendered_pips += self.__render_pip(pip, hidden) + ' '

        return rendered_pips

    @staticmethod
    def __render_pip(pip, hidden: bool = False) -> str:
        if hidden:
            return '[X|X]'
        else:
            return str(pip)

    @staticmethod
    def __clear() -> None:
        if name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def render_score(self) -> None:
        fish: str = ''
        if self.__user.pips_count() > 0 and self.__computer.pips_count() > 0 \
                and self.__board.get_head_number() == self.__board.get_tail_number():
            fish = 'FISH!'

        user_score: int = self.__user.get_score()
        computer_score: int = self.__computer.get_score()
        winner: str = 'Draw!'
        if user_score < computer_score:
            winner = 'You win!'
        elif computer_score < user_score:
            winner = 'Computer win!'

        table: str = f"""
|-----------------------------
| You score: {user_score}
|-----------------------------
| Computer score: {computer_score} 
|-----------------------------
| {winner} {fish}
|-----------------------------
"""
        self.__clear()
        print(table)
