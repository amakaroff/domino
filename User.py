import re
from re import Match
from typing import Optional, Sequence, AnyStr

from Board import Board
from Heap import Heap
from Info import Info
from Pip import Pip


class User:

    def __init__(self, heap: Heap, board: Board, info: Info):
        self.__pips: list[Pip] = heap.take_initial()
        self.__heap: Heap = heap
        self.__board: Board = board
        self.__info: Info = info
        self.__render = lambda: None

    def move(self) -> bool:
        is_done: bool = False
        is_complete: bool = False

        while not is_done:
            self.__info.set_error('')
            command: str = input()

            # You can take even if have move
            if command == "take":
                if not self.__take():
                    self.__info.set_error('Heap is empty, you cannot take new pips')
                self.__render()
                continue

            if command == "done":
                is_done = True
                self.__render()
                continue

            try:
                match: Optional[Match] = re.search("put\\s+(left\\s+|right\\s+)?(\\d+)", command)
                if match is not None:
                    direction: str = 'all'
                    groups: Sequence[AnyStr] = match.groups()

                    if groups[0] is not None:
                        direction: str = groups[0].strip()

                    pip_number: int = int(groups[1]) - 1
                    if self.pips_count() > pip_number >= 0:
                        pip: Pip = self.__pips[pip_number]
                        self.__board.put(pip, direction)
                        self.__pips.remove(pip)
                        is_done = True
                        is_complete = True
                        self.__render()
                    else:
                        raise Exception("Illegal number of pip")
                else:
                    raise Exception("Unexpected command")
            except Exception as error:
                self.__info.set_error(str(error))
                self.__render()

        return is_complete

    def set_render(self, render) -> None:
        self.__render = render

    def __take(self) -> bool:
        pip: Pip = self.__heap.take()
        if pip is None:
            return False
        else:
            self.__pips.append(pip)
            return True

    def get_pips(self) -> list[Pip]:
        return self.__pips

    def pips_count(self) -> int:
        return len(self.get_pips())

    def get_score(self) -> int:
        score: int = 0

        if self.pips_count() == 1 and self.__pips[0].is_zero():
            score += 25

        for pip in self.get_pips():
            score += pip.get_score()

        return score
