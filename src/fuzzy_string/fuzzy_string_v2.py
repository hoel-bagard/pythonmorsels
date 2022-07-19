"""Solution for the FuzzyString exercise."""
import unicodedata
from abc import ABC, abstractmethod
from collections import UserString
from functools import total_ordering
from typing import TypeVar

T = TypeVar('T')
TFuzzyString = TypeVar("TFuzzyString", bound="FuzzyString")


@total_ordering
class Ordered(ABC):
    """Mixin class which defines <=, >, >= based on < and ==."""
    @abstractmethod
    def __lt__(self, other: str | TFuzzyString) -> bool:
        """Child class must implement __lt__."""

    @abstractmethod
    def __eq__(self, other: str | TFuzzyString) -> bool:
        """Child class must implement __eq__."""


class FuzzyString(Ordered, UserString):
    @staticmethod
    def _preprocess_str(string: str | TFuzzyString) -> str:
        return unicodedata.normalize("NFKD", str(string.casefold()))

    def __lt__(self, other: str | TFuzzyString) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) < self._preprocess_str(str(other))
        return NotImplemented

    def __eq__(self, other: str | TFuzzyString) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) == self._preprocess_str(str(other))
        return NotImplemented

    def __contains__(self, other: str | TFuzzyString) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(other) in self._preprocess_str(self.data)
        return NotImplemented
