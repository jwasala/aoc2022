import copy

with open("input.txt") as file:
    lines = file.readlines()


stacks_raw = lines[:9]

stacks = [[] for i in range(9)]

for i in range(7, -1, -1):
    for j in range(1, 34, 4):
        if stacks_raw[i][j] != " ":
            stacks[(j - 1) // 4].append(stacks_raw[i][j])


moves_raw = lines[10:]

moves = []

for move in moves_raw:
    move = move.strip()
    move_parts = move.split(" ")
    moves.append((int(move_parts[1]), int(move_parts[3]), int(move_parts[5])))


def part1():
    _stacks = copy.deepcopy(stacks)
    for count, start, end in moves:
        while count > 0:
            _stacks[end - 1].append(_stacks[start - 1].pop(-1))
            count -= 1
    return "".join(stack[-1] for stack in _stacks)


def part2():
    _stacks = copy.deepcopy(stacks)
    for count, start, end in moves:
        _stacks[end - 1] += _stacks[start - 1][-count:]
        _stacks[start - 1] = _stacks[start - 1][:-count]
    return "".join(stack[-1] for stack in _stacks)


print(part1())
print(part2())
