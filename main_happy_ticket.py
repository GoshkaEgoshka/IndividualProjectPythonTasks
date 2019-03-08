from IndividualProjectPythonTasks.input import InputCache, InputToInt, SetInputValue
from IndividualProjectPythonTasks.validation import (
    IsInteger,
    LessThanMillion,
    AllValidation,
    NotLessThanZero,
)
from IndividualProjectPythonTasks.happy_ticket import LuckyTickets, ShowRes


if __name__ == "__main__":
    min_ticket_number = InputCache(
        InputToInt(SetInputValue("Pls, input min ticket value(6 digits): "))
    )
    max_ticket_number = InputCache(
        InputToInt(SetInputValue("Pls, input input max ticket value(6 digits): "))
    )

    allvalidation = AllValidation(IsInteger(), NotLessThanZero(), LessThanMillion())

    if allvalidation.validation(min_ticket_number.value()):
        if allvalidation.validation(max_ticket_number.value()):
            ticket = LuckyTickets(min_ticket_number.value(), max_ticket_number.value())
            show = ShowRes(ticket.ticket_counter())
            show.show_result()
