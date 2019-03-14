from IndividualProjectPythonTasks.models.input import (
    InputToInt,
    InputCache,
    SetInputValue,
)
from IndividualProjectPythonTasks.models.validation import (
    IsInteger,
    NotLessThanZero,
    AllValidation,
)
from IndividualProjectPythonTasks.models.chess_board import ChessBoard

if __name__ == "__main__":
    width = InputCache(InputToInt(SetInputValue("Pls, input width: ")))
    height = InputCache(InputToInt(SetInputValue("Pls, input height: ")))
    valid = AllValidation(NotLessThanZero(), IsInteger())

    if valid.validation(width.value()):
        if valid.validation(height.value()):
            chess_board = ChessBoard(width.value(), height.value())
            chess_board.chess_board_display()
