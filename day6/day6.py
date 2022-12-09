"""Advent of Code 2022 Day 6 solution
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger


@timelogger(2022, 6, part=1)
def part1(signal: str):
    for idx, _ in enumerate(signal):
        if len(set(signal[idx - 4:idx])) == 4:
            return idx


@timelogger(2022, 6, part=2)
def part2(signal: str):
    for idx, _ in enumerate(signal):
        if len(set(signal[idx - 14:idx])) == 14:
            return idx


def day6():
    signal = get_input(2022, 6)[0]

    return part1(signal), part2(signal)


if __name__ == "__main__":
    idx_part1, idx_part2 = day6()

    print(
        f"{'Characters needed to be processed':<40}",
        f"\n{'before start-of-message (Part 1):':<40} {idx_part1:>10}",
        f"\n{'Characters needed to be processed':<40}",
        f"\n{'before start-of-message (Part 2):':<40} {idx_part2:>10}"
    )
