"""Advent of Code 2022 Day 9 solution
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger
import pandas as pd

class RopeBridge():

    __slots__ = (
        "input",
        "rope",
        "visited"
    )

    def __init__(self, input):
        self.input = input
        self.rope = [[0, 0] for _ in range(10)]
        self.visited = [[] for _ in range(10)]

    @timelogger(2022, 9)
    def pos_tracker(self):
        for instruction in self.input:
            dir, steps = instruction.split()

            for _ in range(int(steps)):
                self.rope[0] = self.move_head(dir, self.rope[0])
                self.visited[0].append(self.rope[0].copy())

                for knot, _ in enumerate(self.rope[1:]):
                    self.rope[knot + 1] = self.move_tail(self.rope[knot], self.rope[knot + 1])
                    self.visited[knot + 1].append(self.rope[knot + 1].copy())

        return self.visited

    def move_head(self, direction, position):
        match direction:
            case "U":
                position[1] += 1
            case "D":
                position[1] -= 1
            case "L":
                position[0] -= 1
            case "R":
                position[0] += 1

        return position

    def move_tail(self, head_pos, tail_pos):
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


def visited_once(visited_list, idx):
    return len([list(x) for x in set(tuple(x) for x in visited_list[idx])])


def day9():
    input = get_input(2022, 9)
    
    ropes = RopeBridge(input)
    visited = ropes.pos_tracker()

    return visited_once(visited, 1), visited_once(visited, -1)


if __name__ == "__main__":
    ans1, ans2 = day9()

    print(
        f"{'# of positions visited at least once (Part 1):':<40} {ans1:>10}",
        f"\n{'# of positions visited at least once (Part 2):':<40} {ans2:>10}"
    )
