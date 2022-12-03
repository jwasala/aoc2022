with open("input.txt") as file:
    rucksacks = [line.strip() for line in file.readlines()]
    rucksacks_comp = [
        (line[: len(line) // 2], line[len(line) // 2 :]) for line in rucksacks
    ]


def part1():
    _sum = 0
    for comp1, comp2 in rucksacks_comp:
        (item,) = set(comp1) & set(comp2)
        if "a" <= item <= "z":
            _sum += ord(item) - 96
        else:
            _sum += ord(item) - 38
    return _sum


def part2():
    _sum = 0
    for i, (r1, r2, r3) in enumerate(zip(rucksacks, rucksacks[1:], rucksacks[2:])):
        if i % 3 != 0:
            continue
        (item,) = set(r1) & set(r2) & set(r3)
        if "a" <= item <= "z":
            _sum += ord(item) - 96
        else:
            _sum += ord(item) - 38
    return _sum


print(part1())
print(part2())
