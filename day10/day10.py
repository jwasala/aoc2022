operations = [
    (op, int(val) if val else None)
    for op, _, val in [
        line.partition(" ") for line in open("input.txt").read().splitlines()
    ]
]


def _get_register_history():
    cycle = 1
    register_at = {1: 1}

    for op, val in operations:
        register_at[cycle + 1] = register_at[cycle]
        if op == "noop":
            cycle += 1
        elif op == "addx":
            register_at[cycle + 2] = register_at[cycle + 1] + val
            cycle += 2

    return register_at


def part1():
    reg_history = _get_register_history()
    return sum(reg_history[i] * i for i in (20, 60, 100, 140, 180, 220))


def part2():
    reg_history = _get_register_history()
    lines = [["." for _ in range(40)] for _ in range(6)]

    for cycle in range(240):
        i, j = cycle // 40, cycle % 40
        lines[i][j] = "#" if abs(reg_history[cycle + 1] - j) <= 1 else "."

    return "\n".join("".join(line) for line in lines)


print(part1())
print(part2())
