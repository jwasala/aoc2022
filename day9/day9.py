moves = [
    (dir_, int(dist))
    for dir_, _, dist in [
        line.partition(" ") for line in open("input.txt").read().splitlines()
    ]
]


def part1():
    visited = {(0, 0)}
    tail = (0, 0)
    head = (0, 0)
    for dir_, dist in moves:
        while dist > 0:
            # Move head in a given direction
            match dir_:
                case "U":
                    head = (head[0] - 1, head[1])
                case "R":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0], head[1] - 1)
            # Check if tail needs to move
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                if head[1] == tail[1]:
                    tail = ((head[0] + tail[0]) // 2, tail[1])
                elif head[0] == tail[0]:
                    tail = (tail[0], (head[1] + tail[1]) // 2)
                elif abs(head[0] - tail[0]) == 2:
                    tail = ((head[0] + tail[0]) // 2, head[1])
                elif abs(head[1] - tail[1]) == 2:
                    tail = (head[0], (head[1] + tail[1]) // 2)
            dist -= 1
            visited.add(tail)
    return len(visited)


def part2():
    visited = {(0, 0)}
    knots = [(0, 0) for _ in range(10)]
    for dir_, dist in moves:
        while dist > 0:
            # Move head in a given direction
            match dir_:
                case "U":
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                case "R":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case "D":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case "L":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
            for head_i, tail_i in zip(range(10), range(1, 10)):
                if (
                    abs(knots[head_i][0] - knots[tail_i][0]) > 1
                    or abs(knots[head_i][1] - knots[tail_i][1]) > 1
                ):
                    if knots[head_i][1] == knots[tail_i][1]:
                        knots[tail_i] = (
                            (knots[head_i][0] + knots[tail_i][0]) // 2,
                            knots[tail_i][1],
                        )
                    elif knots[head_i][0] == knots[tail_i][0]:
                        knots[tail_i] = (
                            knots[tail_i][0],
                            (knots[head_i][1] + knots[tail_i][1]) // 2,
                        )
                    elif (
                        abs(knots[head_i][0] - knots[tail_i][0]) == 2
                        and abs(knots[head_i][1] - knots[tail_i][1]) == 2
                    ):
                        knots[tail_i] = (
                            (knots[head_i][0] + knots[tail_i][0]) // 2,
                            (knots[head_i][1] + knots[tail_i][1]) // 2,
                        )
                    elif abs(knots[head_i][0] - knots[tail_i][0]) == 2:
                        knots[tail_i] = (
                            (knots[head_i][0] + knots[tail_i][0]) // 2,
                            knots[head_i][1],
                        )
                    elif abs(knots[head_i][1] - knots[tail_i][1]) == 2:
                        knots[tail_i] = (
                            knots[head_i][0],
                            (knots[head_i][1] + knots[tail_i][1]) // 2,
                        )
            dist -= 1
            visited.add(knots[-1])
    return len(visited)


print(part1())
print(part2())
