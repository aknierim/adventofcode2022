from day1.day1 import day1
from day2.day2 import day2

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