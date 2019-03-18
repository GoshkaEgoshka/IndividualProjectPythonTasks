def fibonacci(number: int):
    fibonacci_1 = 0
    fibonacci_2 = 1
    if number == 1:
        return 0
    else:
        for i in range(number - 1):
            fibonacci_sum = fibonacci_1 + fibonacci_2
            fibonacci_2 = fibonacci_1
            fibonacci_1 = fibonacci_sum
        return fibonacci_sum


def character_limit(limit: int) -> list:
    fibonacci_series_list = list()
    number = 0

    while True:
        number = number + 1
        buff = len(str(fibonacci(number)))

        if buff < limit:
            continue
        elif buff == limit:
            fibonacci_series_list.append(fibonacci(number))
        else:
            break
    return fibonacci_series_list


def diapason_limit(start_limit: int, end_limit: int) -> list:
    fibonacci_series_list = list()
    number = 0

    while True:
        number += 1
        fibonacci_number = fibonacci(number)

        if fibonacci_number < start_limit:
            continue
        elif fibonacci_number >= start_limit and fibonacci_number <= end_limit:
            fibonacci_series_list.append(fibonacci(number))
        else:
            break
    return fibonacci_series_list
