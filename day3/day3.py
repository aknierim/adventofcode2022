"""Advent of Code 2022 Day 3 solution.
"""

from aoctools.input import get_input


def id_sum(id_mapping, duplicates):
    summed_ids = 0
    for dup in duplicates:
        summed_ids += id_mapping[dup]

    return summed_ids


def day3():
    ruck_list = get_input(2022, 3)

    lower_alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper_alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    alphabet = lower_alpha + upper_alpha

    # Part 1
    duplicates = []
    for item in ruck_list:
        comp1 = item[len(item)//2:]
        comp2 = item[:len(item)//2]

        dup = set(comp1).intersection(comp2)
        duplicates.append(''.join(dup))

    id_mapping = {}
    for idx, alpha in enumerate(alphabet):
        id_mapping[alpha] = idx + 1

    id_sum_p1 = id_sum(id_mapping, duplicates)

    # Part 2
    grouped_list = [ruck_list[n:n + 3] for n in range(0, len(ruck_list), 3)]

    duplicates_p2 = []
    for group in grouped_list:
        dup = set(group[0].strip()).intersection(group[1].strip())
        dup_all_three = set(''.join(dup)).intersection(group[2].strip())

        duplicates_p2.append(''.join(dup_all_three))

    id_sum_p2 = id_sum(id_mapping, duplicates_p2)

    return id_sum_p1, id_sum_p2


if __name__ == "__main__":
    sum_p1, sum_p2 = day3()

    print(
        f"{'Sum of priorities of the item types (Part 1):':<40} {sum_p1:>10}",
        f"\n{'Sum of priorities of the item types (Part 2):':<40} {sum_p2:>10}"
    )
