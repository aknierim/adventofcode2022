from day1.day1 import day1
from day2.day2 import day2
from day3.day3 import day3
from day4.day4 import day4
from day5.day5 import day5
from day6.day6 import day6
from day7.day7 import day7


if __name__ == "__main__":

    elf_id, most_cals, top_three_cals = day1()
    print(
        "DAY 1:"
        f"\n{'Elf carrying the most Calories:':<40} {elf_id:>10}",
        f"\n{'Total Calories carried:':<40} {most_cals:>10}",
        f"\n{'Sum of Calories of the top three elves:':<40} {top_three_cals:>10}"
    )

    score_p1, score_p2 = day2()
    print(
        "DAY 2:"
        f"\n{'Score for part 1:':<40} {score_p1:>10}",
        f"\n{'Score for part 2:':<40} {score_p2:>10}"
    )

    sum_p1, sum_p2 = day3()
    print(
        "DAY 3:",
        f"\n{f'{chr(931)} priorities of the item types (Part 1):':<40} {sum_p1:>10}",
        f"\n{f'{chr(931)} priorities of the item types (Part 2):':<40} {sum_p2:>10}"
    )

    ans_p1, ans_p2 = day4()
    print(
        "DAY 4:",
        f"\n{'Pairs in which one range fully contains':<40}",
        f"\n{'another:':<40} {ans_p1:>10}",
        f"\n{'Number of overlapping ranges:':<40} {ans_p2:>10}"
    )

    crates_pt1, crates_pt2 = day5()
    print(
        "DAY 5:",
        f"\n{'Crates on top of each stack (Part 1):':<40} {crates_pt1:>10}",
        f"\n{'Crates on top of each stack (Part 2):':<40} {crates_pt2:>10}"
    )

    ans1, ans2 = day6()
    print(
        "DAY 6:"
        f"\n{'Characters needed to be processed':<40}",
        f"\n{'before start-of-message (Part 1):':<40} {ans1:>10}",
        f"\n{'Characters needed to be processed':<40}",
        f"\n{'before start-of-message (Part 2):':<40} {ans2:>10}"
    )

    ans1, ans2 = day7()
    print(
        "DAY 7:"
        f"\n{'Sum of total sizes of all directories':40}",
        f"\n{'with a total of at most 100000:':<40} {ans1:>10}",
        f"\n{'Total size of smallest directory to':<40}",
        f"\n{'delete:':<40} {ans2:>10}"
    )
