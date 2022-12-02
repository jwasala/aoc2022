from os import PathLike
from typing import Union

from aoc.common.day import Day


class Day2(Day[list[tuple[str, str]]]):
    _move_score_mapping = {"A": 1, "B": 2, "C": 3}
    _beats_mapping = {"A": "C", "B": "A", "C": "B"}
    _beaten_by_mapping = {v: k for k, v in _beats_mapping.items()}

    @classmethod
    def move_to_score(cls, move: str) -> int:
        return cls._move_score_mapping[move]

    @classmethod
    def beats(cls, move: str) -> str:
        return cls._beats_mapping[move]

    @classmethod
    def is_beaten_by(cls, move: str) -> str:
        return cls._beaten_by_mapping[move]

    @classmethod
    def map_xyz_to_abc(cls, move: str) -> str:
        return str(chr(ord(move) - 23))

    @classmethod
    def calc_round_score_part1(cls, m1: str, m2: str) -> int:
        m2 = cls.map_xyz_to_abc(m2)
        if m1 == m2:
            outcome = 3
        elif cls.beats(m1) == m2:
            outcome = 0
        else:
            outcome = 6
        return outcome + cls.move_to_score(m2)

    @classmethod
    def calc_round_score_part2(cls, m1: str, m2: str) -> int:
        if m2 == "X":
            return cls.move_to_score(cls.beats(m1))
        elif m2 == "Y":
            return cls.move_to_score(m1) + 3
        return cls.move_to_score(cls.is_beaten_by(m1)) + 6

    def load_from_file(
        self, input_path: Union[str, bytes, PathLike]
    ) -> list[tuple[str, str]]:
        with open(input_path) as file:
            return [(line[0], line[2]) for line in file.readlines()]

    def part1(self) -> int:
        return sum(self.calc_round_score_part1(m1, m2) for m1, m2 in self.problem)

    def part2(self) -> int:
        return sum(self.calc_round_score_part2(m1, m2) for m1, m2 in self.problem)


if __name__ == "__main__":
    Day2("input.txt").run()
