"""Adevnt of Code 2022 Day 4 solution
"""
from aoctools.input import get_input


def day4():
    pair_list = get_input(2022, 4)

    counter_p1 = 0
    counter_p2 = 0

    for item in pair_list:
        elf1, elf2 = item.replace('\n', '').split(',')

        elf1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)
        elf2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)

        if set(elf1).issubset(elf2) or set(elf2).issubset(elf1):
            counter_p1 += 1

        if set(elf1).intersection(elf2):
            counter_p2 += 1

    return counter_p1, counter_p2


if __name__ == "__main__":
    ans_p1, ans_p2 = day4()

    print(
        f"\n{'Pairs in which one range fully contains':<40}"
        f"\n{'another:':<40} {ans_p1:>10}",
        f"\n{'Number of overlapping ranges:':<40} {ans_p2:>10}"
    )
