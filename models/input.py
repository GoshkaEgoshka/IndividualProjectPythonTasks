from abc import ABC, abstractmethod
from typing import Any


class Input(ABC):
    @abstractmethod
    def value(self) -> Any:
        pass


class SetInputValue(Input):
    def __init__(self, input_text: str):
        self._text = input_text

    def value(self) -> Any:
        return input(self._text)


class InputToInt(Input):
    def __init__(self, some_value: Any):
        self._value = some_value

    def value(self) -> Any:
        return int(self._value.value())


class InputCache(Input):
    def __init__(self, ask: Input):
        self._ask = ask
        self._data = []

    def value(self) -> Any:
        if not self._data:
            self._data.append(self._ask.value())
        return self._data[0]
