from functools import reduce


def part1():
    grid = [[(int(j), False) for j in i] for i in open("input.txt").read().splitlines()]

    def traverse():
        for i in range(99):
            highest, _ = grid[i][0]
            grid[i][0] = (highest, True)
            for j in range(99):
                height, _ = grid[i][j]
                if height > highest:
                    highest = height
                    grid[i][j] = (height, True)
                if height == 9:
                    break

    def transpose():
        nonlocal grid
        grid = [list(line) for line in zip(*grid)]

    def reverse():
        nonlocal grid
        grid = [list(reversed(line)) for line in grid]

    for action in (transpose, reverse, transpose, reverse):
        action()
        traverse()

    return sum(int(is_visible) for line in grid for _, is_visible in line)


def part2():
    grid = [[(int(j), False) for j in i] for i in open("input.txt").read().splitlines()]

    def count_score(i, j):
        height = grid[i][j][0]
        count = []
        for i_step, j_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dir_count = 0
            i2, j2 = i, j
            while 0 < i2 < 98 and 0 < j2 < 98:
                i2 += i_step
                j2 += j_step
                current_height = grid[i2][j2][0]
                dir_count += 1
                if current_height >= height:
                    break
            count.append(dir_count)
        return reduce(lambda x, y: x * y, count)

    return max(count_score(i, j) for i in range(99) for j in range(99))


print(part1())
print(part2())
