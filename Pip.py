class Pip:

    def __init__(self, top: int, bottom: int):
        self.__top: int = top
        self.__bottom: int = bottom

    def revert(self) -> None:
        top: int = self.get_top()
        self.__top = self.get_bottom()
        self.__bottom = top

    def get_top(self) -> int:
        return self.__top

    def get_bottom(self) -> int:
        return self.__bottom

    def get_score(self) -> int:
        if self.get_top() is 6 and self.get_bottom() is 6:
            return 50

        return self.get_top() + self.get_bottom()

    def is_zero(self) -> bool:
        return self.get_top() is 0 and self.get_bottom() is 0

    def is_duplicate(self) -> bool:
        return self.get_top() is self.get_bottom()

    def __str__(self):
        return f'[{self.get_top()}|{self.get_bottom()}]'
