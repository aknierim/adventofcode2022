"""Advent of Code 2022 Day 3 solution.
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger


def id_sum(duplicates):
    summed_ids = 0
    for dup in duplicates:
        if ord(dup) >= 97:
            summed_ids += ord(dup) - 96
        else:
            summed_ids += ord(dup) - 64 + 26

    return summed_ids


@timelogger(2022, 3)
def day3():
    ruck_list = get_input(2022, 3)

    # Part 1
    duplicates = []
    for item in ruck_list:
        # get same elements in both strings
        dup = set(item[len(item)//2:]).intersection(item[:len(item)//2])
        duplicates.append(''.join(dup))

    id_sum_p1 = id_sum(duplicates)

    # Part 2
    # Create a list of sublists with 3 strings each
    grouped_list = [ruck_list[n:n + 3] for n in range(0, len(ruck_list), 3)]

    duplicates_p2 = []
    for group in grouped_list:
        dup = set(group[0].strip()).intersection(group[1].strip())
        dup_all_three = set(''.join(dup)).intersection(group[2].strip())

        duplicates_p2.append(''.join(dup_all_three))

    id_sum_p2 = id_sum(duplicates_p2)

    return id_sum_p1, id_sum_p2


if __name__ == "__main__":
    sum_p1, sum_p2 = day3()

    print(
        f"{'Sum of priorities of the item types (Part 1):':<40} {sum_p1:>10}",
        f"\n{'Sum of priorities of the item types (Part 2):':<40} {sum_p2:>10}"
    )
