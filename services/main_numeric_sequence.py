from IndividualProjectPythonTasks.models.input import (
    InputCache,
    InputToInt,
    SetInputValue,
)
from IndividualProjectPythonTasks.models.validation import (
    IsInteger,
    LessThanMillion,
    AllValidation,
    NotLessThanZero,
)
from IndividualProjectPythonTasks.models.numeric_sequence import NumericSequence

if __name__ == "__main__":
    min_sqr = InputCache(InputToInt(SetInputValue("Please, input min sqr: ")))
    length = InputCache(InputToInt(SetInputValue("Please, input length of sequence: ")))
    valid = AllValidation(IsInteger(), LessThanMillion(), NotLessThanZero())

    if valid.validation(min_sqr.value()):
        if valid.validation(length.value()):
            numeric_sequence = NumericSequence(length.value(), min_sqr.value())
            numeric_sequence.create_sequence()
            numeric_sequence.show_sequence()
