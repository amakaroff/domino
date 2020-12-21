class Info:

    def __init__(self):
        self.__error = ''
        self.__is_game_end = False
        self.__current_player = 'Computer'

    def get_error(self) -> str:
        return self.__error

    def set_error(self, error: str) -> None:
        self.__error = error

    def is_game_end(self) -> bool:
        return self.__is_game_end

    def complete_game(self) -> None:
        self.__is_game_end = True

    def get_current_player(self) -> str:
        return self.__current_player

    def set_current_player(self, player: str) -> None:
        self.__current_player = player
