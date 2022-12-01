"""Advent of Code 2022 Day 1 solution.
"""
# initialize lists
elves = []
total_calories = []

with open("day1/day1.txt") as f:
    lines = f.readlines()

    # prerequisites
    calories = 0
    elf_count = 1

    for line in lines:
        # check that the current line is not a new line,
        # else save sum over Calories to total_calories
        # and save elf id
        if line != "\n":
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

print(
    f"{'Elf carrying the most Calories:':<40} {elf_id:>10}",
    f"\n{'Total Calories carried:':<40} {most_calories:>10}"
)

# Part 2
sorted_calories = sorted(total_calories)
sum_top_three = sum(sorted_calories[-3:])

print(f"{'Sum of Calories of the top three elves:':<40} {sum_top_three:>10}")
