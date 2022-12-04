from day1.day1 import day1
from day2.day2 import day2
from day3.day3 import day3
from day4.day4 import day4

elf_id, most_cals, top_three_cals = day1()
print(
    "DAY 1:"
    f"\n{'Elf carrying the most Calories:':<40} {elf_id:>10}",
    f"\n{'Total Calories carried:':<40} {most_cals:>10}",
    f"\n{'Sum of Calories of the top three elves:':<40} {top_three_cals:>10}"
)

score_p1, score_p2 = day2()
print(
    "\nDAY 2:"
    f"\n{'Score for part 1:':<40} {score_p1:>10}",
    f"\n{'Score for part 2:':<40} {score_p2:>10}"
)

sum_p1, sum_p2 = day3()
print(
    "\nDAY 3:",
    f"\n{f'{chr(931)} priorities of the item types (Part 1):':<40} {sum_p1:>10}",
    f"\n{f'{chr(931)} priorities of the item types (Part 2):':<40} {sum_p2:>10}"
)

ans_p1, ans_p2 = day4()
print(
    "\nDAY 4:",
    f"\n{'Pairs in which one range fully contains':<40}",
    f"\n{'another:':<40} {ans_p1:>10}",
    f"\n{'Number of overlapping ranges:':<40} {ans_p2:>10}"
)
