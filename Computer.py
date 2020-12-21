import time
from typing import Optional

from Board import Board
from Heap import Heap
from Pip import Pip


class Computer:

    def __init__(self, heap: Heap, board: Board):
        self.__pips: list[Pip] = heap.take_initial()
        self.__heap: Heap = heap
        self.__board: Board = board
        self.__render = lambda: None

    def move(self) -> bool:
        head_number: int = self.__board.get_head_number()
        tail_number: int = self.__board.get_tail_number()

        pip: Optional[Pip] = None
        while pip is None:
            pip = self.__select_pip(head_number, tail_number)
            time.sleep(2)
            if pip is not None:
                self.__board.put(pip)
                self.__pips.remove(pip)
                return True
            else:
                if not self.__take():
                    return False
            self.__render()

    def __take(self) -> bool:
        pip: Pip = self.__heap.take()
        if pip is None:
            return False
        else:
            self.__pips.append(pip)
            return True

    def set_render(self, render) -> None:
        self.__render = render

    def __select_pip(self, head_number: int, tail_number: int) -> Optional[Pip]:
        if head_number is -1 and tail_number is -1:
            return self.__pips[0]

        for pip in self.__pips:
            if pip.get_top() is head_number or pip.get_top() is tail_number or \
                    pip.get_bottom() is head_number or pip.get_bottom() is tail_number:
                return pip

        return None

    def get_pips(self) -> list[Pip]:
        return self.__pips

    def pips_count(self) -> int:
        return len(self.get_pips())

    def get_score(self) -> int:
        score: int = 0

        if self.pips_count() is 1 and self.__pips[0].is_zero():
            score += 25

        for pip in self.get_pips():
            score += pip.get_score()

        return score
