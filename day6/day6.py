with open("input.txt") as file:
    text = file.readlines()[0]


def part1():
    marker_length = 4
    for i in range(len(text) - marker_length - 1):
        if len({text[i + j] for j in range(marker_length)}) == marker_length:
            return i + marker_length


def part2():
    marker_length = 14
    for i in range(len(text) - marker_length - 1):
        if len({text[i + j] for j in range(marker_length)}) == marker_length:
            return i + marker_length


print(part1())
print(part2())
