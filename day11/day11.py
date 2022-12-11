from itertools import groupby
from typing import Callable


class Monkey:
    def __init__(
        self,
        monkey_id: int,
        items: list[int],
        test_div: int,
        test_true: int,
        test_false: int,
        operation: Callable[[int], int] | None = None,
    ):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.test_div = test_div
        self.test_true = test_true
        self.test_false = test_false
        self.inspect_count: int = 0

    def _inspect(self) -> None:
        self.items[0] = self.operation(self.items[0])
        # 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
        self.items[0] %= 9699690
        self.inspect_count += 1

    def _get_bored(self) -> None:
        self.items[0] = self.items[0] // 3

    def _test(self) -> int:
        return self.test_true if self.items[0] % self.test_div == 0 else self.test_false

    def pop(self) -> tuple[int, int] | None:
        if not self.items:
            return None
        self._inspect()
        self._get_bored()
        next_monkey_id = self._test()
        return self.items.pop(0), next_monkey_id

    def push(self, item: int) -> None:
        self.items.append(item)


def _load() -> list[Monkey]:
    monkeys: list[Monkey] = []

    monkeys_raw = [
        list(gr) for k, gr in groupby(open("input.txt").read().splitlines(), bool) if k
    ]
    for monkey_raw in monkeys_raw:
        monkeys.append(
            Monkey(
                monkey_id=int(monkey_raw[0].split(" ")[-1][:-1]),
                items=[int(monkey_raw[1].split(": ")[1].split(", ")[0])]
                + list(map(int, monkey_raw[1].split(", ")[1:])),
                test_div=int(monkey_raw[3].split(" ")[-1]),
                test_true=int(monkey_raw[4].split(" ")[-1]),
                test_false=int(monkey_raw[5].split(" ")[-1]),
            )
        )
        # This is absurdly ugly and bad practice, but one line
        exec(f'monkeys[-1].operation = lambda old: {monkey_raw[2].split(" = ")[1]}')

    return monkeys


def _play(monkeys, rounds) -> list[Monkey]:
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                item, receiver = monkey.pop()
                monkeys[receiver].push(item)
    return monkeys


def _get_monkey_business(monkeys) -> int:
    monkeys = sorted(monkeys, key=lambda m: m.inspect_count, reverse=True)
    return monkeys[0].inspect_count * monkeys[1].inspect_count


def part1():
    return _get_monkey_business(_play(_load(), 20))


def part2():
    monkeys = _load()

    for monkey in monkeys:
        # Disable worry division using... monkey patching
        monkey._get_bored = lambda: None

    return _get_monkey_business(_play(monkeys, 10000))


print(part1())
print(part2())
