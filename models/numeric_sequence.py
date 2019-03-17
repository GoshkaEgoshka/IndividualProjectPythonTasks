from math import sqrt


class NumericSequence:
    def __init__(self, length: int, min_sqr: int):
        self._length = length
        self._min_sqr = min_sqr
        self._numeric_sequence = list()

    def create_sequence(self) -> None:
        root_value = sqrt(self._min_sqr)
        if root_value.is_integer():
            for root_value in range(int(root_value), int(root_value) + self._length):
                self._numeric_sequence.append(root_value)
        else:
            root_value = int(root_value) + 1
            for root_value in range(int(root_value), root_value + self._length):
                self._numeric_sequence.append(root_value)

    def show_sequence(self):
        print(self._numeric_sequence)
