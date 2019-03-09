from IndividualProjectPythonTasks.input import InputToInt, InputCache, SetInputValue
from IndividualProjectPythonTasks.chess_board import ChessBoard
from IndividualProjectPythonTasks.validation import (
    IsInteger,
    NotLessThanZero,
    AllValidation,
)


if __name__ == "__main__":
    width = InputCache(InputToInt(SetInputValue("Pls, input width: ")))
    height = InputCache(InputToInt(SetInputValue("Pls, input height: ")))
    valid = AllValidation(NotLessThanZero(), IsInteger())

    if valid.validation(width.value()):
        if valid.validation(height.value()):
            chess_board = ChessBoard(width.value(), height.value())
            chess_board.chess_board_display()
