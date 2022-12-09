"""Advent of Code 2022 Day 9 solution
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger


def move_head(direction, position):
    match direction:
        case "U":
            position[1] += 1
            return position
        case "D":
            position[1] -= 1
            return position
        case "L":
            position[0] -= 1
            return position
        case "R":
            position[0] += 1
            return position


def move_tail(head_pos, tail_pos):
    diff_x, diff_y = list(map(int.__sub__, head_pos, tail_pos))

    if abs(diff_x) <= 1 and abs(diff_y) <= 1:
        return tail_pos

    if diff_x >= 1:
        tail_pos[0] += 1
    if diff_x <= -1:
        tail_pos[0] -= 1
    if diff_y >= 1:
        tail_pos[1] += 1
    if diff_y <= -1:
        tail_pos[1] -= 1

    return tail_pos


class RopeBridge():

    __slots__ = (
        "input",
        "rope"
    )

    def __init__(self, input):
        self.input = input
        self.rope = [[0, 0] for _ in range(10)]

    @timelogger(2022, 9, part=1)
    def part1(self):
        head_pos = [0, 0]
        tail_pos = [0, 0]
        visited = []

        for instruction in self.input:
            dir, steps = instruction.split()

            for _ in range(int(steps)):
                head_pos = move_head(dir, head_pos)
                tail_pos = move_tail(head_pos, tail_pos)
                visited.append(tail_pos.copy())

        visited_once = [list(x) for x in set(tuple(x) for x in visited)]

        return len(visited_once)

    @timelogger(2022, 9, part=2)
    def part2(self):
        visited = []

        for instruction in self.input:
            dir, steps = instruction.split()

            for _ in range(int(steps)):
                self.rope[0] = move_head(dir, self.rope[0])

                for knot, _ in enumerate(self.rope[1:]):
                    self.rope[knot + 1] = move_tail(self.rope[knot], self.rope[knot + 1])
                    visited.append(self.rope[-1].copy())

        visited_once = [list(x) for x in set(tuple(x) for x in visited)]

        return len(visited_once)


def day9():
    input = get_input(2022, 9)
    ropes = RopeBridge(input)

    return ropes.part1(), ropes.part2()


if __name__ == "__main__":
    ans1, ans2 = day9()

    print(
        f"{'# of positions visited at least once (Part 1):':<40} {ans1:>10}",
        f"\n{'# of positions visited at least once (Part 2):':<40} {ans2:>10}"
    )
