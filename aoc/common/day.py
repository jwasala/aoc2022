import abc
from os import PathLike
from typing import Union, TypeVar, Generic

T = TypeVar("T")


class Day(abc.ABC, Generic[T]):
    problem: T

    def __init__(self, input_path: Union[str, bytes, PathLike]):
        self.problem = self.load_from_file(input_path)

    @abc.abstractmethod
    def load_from_file(self, input_path: Union[str, bytes, PathLike]) -> T:
        pass

    @abc.abstractmethod
    def part1(self) -> int:
        pass

    @abc.abstractmethod
    def part2(self) -> int:
        pass

    def run(self):
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")
