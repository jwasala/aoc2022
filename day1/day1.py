from pathlib import Path


inventories = [
    [int(item) for item in inventory.split("\n")]
    for inventory in Path("input.txt").read_text().split("\n\n")
]


def part1() -> int:
    return max(sum(inv) for inv in inventories)


def part2() -> int:
    return sum(sorted([sum(inv) for inv in inventories], reverse=True)[:3])


print(part1())
print(part2())
