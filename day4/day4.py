with open("input.txt") as file:
    pairs_of_ranges = [
        [[int(num) for num in pair.split("-")] for pair in line.split(",")]
        for line in file.readlines()
    ]


def part1():
    count = 0
    for ((x1, x2), (y1, y2)) in pairs_of_ranges:
        if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
            count += 1
    return count


def part2():
    count = 0
    for ((x1, x2), (y1, y2)) in pairs_of_ranges:
        if (x2 >= y1 >= x1) or (x2 >= y2 >= x1) or (y2 >= x1 >= y1) or (y2 >= x2 >= y1):
            count += 1
    return count


print(part1())
print(part2())
