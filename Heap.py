import random
from typing import Optional

from Pip import Pip


class Heap:

    def __init__(self, initial_pips_count):
        self.__heap: list[Pip] = list[Pip]()
        self.__initial_pips_count: int = initial_pips_count

        for i in reversed(range(7)):
            for j in range(i + 1):
                self.__heap.append(Pip(j, i))

        random.shuffle(self.__heap)

    def take_initial(self) -> list[Pip]:
        initial: list[Pip] = list[Pip]()

        for _ in range(self.__initial_pips_count):
            initial.append(self.take())

        return initial

    def take(self) -> Optional[Pip]:
        if len(self.__heap) > 0:
            return self.__heap.pop()
        else:
            return None

    def count(self) -> int:
        return len(self.__heap)
