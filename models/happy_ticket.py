class LuckyTickets:
    def __init__(self, min, max):
        self._min_ticket_number = min
        self._max_ticket_number = max

    def easy_way_happy_ticket(self, ticket_number: int) -> bool:
        sum_right_numbers = 0
        sum_left_numbers = 0
        counter_for_middle = 0
        ticket_number = str(ticket_number)
        ticket_number = str.zfill(ticket_number, 6)

        for i in ticket_number:
            if counter_for_middle < 3:
                sum_left_numbers += int(i)
                counter_for_middle += 1
            else:
                sum_right_numbers += int(i)
        return True if sum_right_numbers == sum_left_numbers else False

    def hard_way_happy_ticket(self, ticket_number: int) -> bool:
        sum_of_odd_numbers = 0
        sum_of_even_numbers = 0

        for _ in range(6):
            current_numeric_in_ticket = ticket_number % 10
            if current_numeric_in_ticket % 2 > 0:
                sum_of_odd_numbers = sum_of_odd_numbers + current_numeric_in_ticket
            else:
                sum_of_even_numbers = sum_of_even_numbers + current_numeric_in_ticket
            ticket_number = int(ticket_number / 10)
        return True if sum_of_odd_numbers == sum_of_even_numbers else False

    def ticket_counter(self) -> tuple:
        counter_for_hard_way = 0
        counter_for_easy_way = 0

        while self._min_ticket_number != self._max_ticket_number + 1:
            if self.easy_way_happy_ticket(self._min_ticket_number):
                counter_for_easy_way += 1
            if self.hard_way_happy_ticket(self._min_ticket_number):
                counter_for_hard_way += 1
            self._min_ticket_number += 1
        return (
            counter_for_easy_way - counter_for_hard_way,
            counter_for_easy_way,
            counter_for_hard_way,
        )


class ShowRes:
    def __init__(self, result: tuple):
        self._result = result

    def show_result(self) -> None:
        if self._result[0] > 0:
            print(
                f"Easy way win! "
                f"Easy:  {self._result[1]} "
                f"Hard:   {self._result[2]}"
            )
        elif self._result[0] < 0:
            print(
                f"Hard way win! "
                f"Easy: {self._result[1]} "
                f"Hard: {self._result[2]} "
            )
        else:
            print(f"Equal! " f"Easy: {self._result[1]} " f"Hard: {self._result[2]} ")
