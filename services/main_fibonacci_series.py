from IndividualProjectPythonTasks.models.input import (
    InputToInt,
    SetInputValue,
    InputCache,
)
from IndividualProjectPythonTasks.models.validation import (
    AllValidation,
    IsInteger,
    NotLessThanZero,
)
from IndividualProjectPythonTasks.models.fibonacci_series import (
    character_limit,
    diapason_limit,
)


def check(value: int) -> bool:
    valid = AllValidation(IsInteger(), NotLessThanZero())
    if valid.validation(value):
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        print("1. Character limit.")
        print("2. Diapason Limit.")
        print("   Put any another button for quit.\n")
        menu_item = InputCache(InputToInt(SetInputValue("Input menu item: ")))
        if menu_item.value() == 1:
            limit = InputCache(InputToInt(SetInputValue("Input limit: ")))
            if check(limit.value()):
                print(character_limit(limit.value()))
        elif menu_item.value() == 2:
            start_limit = InputCache(InputToInt(SetInputValue("Input start limit: ")))
            end_limit = InputCache(InputToInt(SetInputValue("Input end limit: ")))
            if check(start_limit.value()):
                if check(end_limit.value()):
                    print(diapason_limit(start_limit.value(), end_limit.value()))
