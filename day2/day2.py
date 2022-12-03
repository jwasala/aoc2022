with open("input.txt") as file:
    lines = [(line[0], line[2]) for line in file.readlines()]


beats = {"A": "C", "B": "A", "C": "B"}
beaten_by = {v: k for k, v in beats.items()}


def part1():
    score = 0
    for m1, m2 in lines:
        m2 = chr(ord(m2) - 23)
        if m1 == m2:
            score += 3
        elif beaten_by[m1] == m2:
            score += 6
        score += ord(m2) - 64
    return score


def part2():
    score = 0
    for m1, m2 in lines:
        if m2 == "X":
            score += ord(beats[m1]) - 64
        elif m2 == "Y":
            score += ord(m1) - 64 + 3
        else:
            score += ord(beaten_by[m1]) - 64 + 6

    return score


print(part1())
print(part2())
