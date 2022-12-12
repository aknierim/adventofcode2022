"""Advent of Code 2022 Day 10 solution.
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger


@timelogger(2022, 10)
def day10():
    global signal, cycle, pixels
    pixels = ""
    signal = 0
    cycle = 0
    x = 1

    input = get_input(2022, 10)

    def cycle_check():
        global signal, cycle, pixels

        if cycle % 40 in [x - 1, x, x + 1]:
            pixels += f'{chr(127873)}'
        else:
            pixels += f'{chr(127876)}'

        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += x * cycle
        
        if cycle % 40 == 0:
            print(pixels)
            pixels = ""

    for line in input:
        match line.split():
            case ["noop"]:
                cycle_check()
            case ["addx", val]:
                cycle_check()
                cycle_check()
                x += int(val)

    return signal


if __name__ == "__main__":
    ans1 = day10()

    print(
        f"{'Sum of the signal strengths:':<40} {ans1:>10}"
    )
