from Pip import Pip


class Board:

    def __init__(self):
        self.__board: list[Pip] = list[Pip]()

    def put(self, pip: Pip, direction: str = "all") -> None:
        if len(self.__board) == 0:
            if pip.is_zero():
                raise Exception("You can't put pip [0|0] on empty board")
            else:
                self.__board.append(pip)
                return

        if direction == "all" or direction == "left":
            head_number: int = self.get_head_number()
            if head_number is pip.get_top():
                pip.revert()
                self.__board.insert(0, pip)
                return
            elif head_number is pip.get_bottom():
                self.__board.insert(0, pip)
                return

        if direction == "all" or direction == "right":
            tail_number: int = self.get_tail_number()
            if tail_number is pip.get_bottom():
                pip.revert()
                self.__board.append(pip)
                return
            elif tail_number is pip.get_top():
                self.__board.append(pip)
                return

        raise Exception(f"Illegal pip [{pip.get_top()}|{pip.get_bottom()}] put into board")

    def get_head_number(self) -> int:
        if len(self.__board) > 0:
            return self.__board[0].get_top()
        else:
            return -1

    def get_tail_number(self) -> int:
        if len(self.__board) > 0:
            return self.__board[len(self.__board) - 1].get_bottom()
        else:
            return -1

    def get_pips(self) -> list[Pip]:
        return self.__board
