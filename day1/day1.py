"""Advent of Code 2022 Day 1 solution.
"""
from aoctools.input import get_input
from aoctools.timelogger import timelogger

@timelogger(2022, 1)
def day1():
    # Part 1
    # initialize lists
    elves = []
    total_calories = []

    lines = get_input(2022, 1)

    # prerequisites
    calories = 0
    elf_count = 1

    for line in lines:
        # check that the current line is not a new line,
        # else save sum over Calories to total_calories
        # and save elf id
        if line != "":
            calories += int(line)
        else:
            total_calories.append(calories)
            elves.append(elf_count)

            # reset calories, increase elf id counter
            calories = 0
            elf_count += 1

    # last elf in list
    total_calories.append(calories)
    elves.append(elf_count)

    most_calories = max(total_calories)
    elf_id = elves[total_calories.index(most_calories)]

    # Part 2
    total_calories.sort()

    return elf_id, most_calories, sum(total_calories[-3:])


if __name__ == "__main__":
    elf_id, most_cals, top_three_cals = day1()

    print(
        f"{'Elf carrying the most Calories:':<40} {elf_id:>10}",
        f"\n{'Total Calories carried:':<40} {most_cals:>10}",
        f"\n{'Sum of Calories of the top three elves:':<40} {top_three_cals:>10}"
    )

