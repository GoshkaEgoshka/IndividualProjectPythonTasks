from abc import ABC, abstractmethod
from typing import Any


class Valid(ABC):
    @abstractmethod
    def validation(self, value: Any) -> Any:
        pass


class IsInteger(Valid):
    def validation(self, value) -> bool:
        return isinstance(value, int)


class NotLessThanZero(Valid):
    def validation(self, value) -> bool:
        return value >= 0


class LessThanMillion(Valid):
    def validation(self, value: Any) -> bool:
        return value <= 999999


class AllValidation(Valid):
    def __init__(self, *rules: Valid):
        self._checks = rules

    def validation(self, value) -> bool:
        for rule in self._checks:
            if not rule.validation(value):
                print(f"{rule.__class__.__name__} is failed")
                return False
        return True
