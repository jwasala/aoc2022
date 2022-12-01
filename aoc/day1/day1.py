from os import PathLike
from typing import Union

from aoc.common.day import Day


class Day1(Day[list[list[int]]]):
    def load_from_file(
        self, input_path: Union[str, bytes, PathLike]
    ) -> list[list[int]]:
        with open(input_path) as file:
            inventories = [[]]
            for line in file:
                if line == "\n":
                    inventories.append([])
                else:
                    inventories[-1].append(int(line))
            return inventories

    def part1(self) -> int:
        return max([sum(inv) for inv in self.problem])

    def part2(self) -> int:
        top_3 = [0, 0, 0]

        for inventory_sum in [sum(inv) for inv in self.problem]:
            # Find the smallest element in top_3.
            min_top_3_i, min_top_3 = min(
                [(i, val) for i, val in enumerate(top_3)], key=lambda tup: tup[1]
            )
            if min_top_3 < inventory_sum:
                top_3[min_top_3_i] = inventory_sum

        return sum(top_3)


if __name__ == "__main__":
    Day1("input.txt").run()
