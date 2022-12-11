from day1.day1 import day1
from day10.day10 import day10
from day11.day11 import day11
from day2.day2 import day2
from day3.day3 import day3
from day4.day4 import day4
from day5.day5 import day5
from day6.day6 import day6
from day7.day7 import day7
from day8.day8 import day8
from day9.day9 import day9


if __name__ == "__main__":

    ans1, ans2, ans3 = day1()
    print(
        "DAY 1:"
        f"\n{'Elf carrying the most Calories: ':.<50}{ans1:.>20}",
        f"\n{'Total Calories carried: ':.<50}{ans2:.>20}",
        f"\n{'Sum of Calories of the top three elves: ':.<50}{ans3:.>20}"
    )

    ans1, ans2 = day2()
    print(
        "DAY 2:"
        f"\n{'Score for part 1: ':.<50}{ans1:.>20}",
        f"\n{'Score for part 2: ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day3()
    print(
        "DAY 3:",
        f"\n{f'{chr(931)} priorities of the item types (Part 1): ':.<50}{ans1:.>20}",
        f"\n{f'{chr(931)} priorities of the item types (Part 2): ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day4()
    print(
        "DAY 4:",
        f"\n{'Pairs in which one range fully contains':<50}",
        f"\n{'another: ':.<50}{ans1:.>20}",
        f"\n{'Number of overlapping ranges: ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day5()
    print(
        "DAY 5:",
        f"\n{'Crates on top of each stack (Part 1): ':.<50}{ans1:.>20}",
        f"\n{'Crates on top of each stack (Part 2): ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day6()
    print(
        "DAY 6:"
        f"\n{'Characters needed to be processed':<50}",
        f"\n{'before start-of-message (Part 1): ':.<50}{ans1:.>20}",
        f"\n{'Characters needed to be processed':<50}",
        f"\n{'before start-of-message (Part 2): ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day7()
    print(
        "DAY 7:"
        f"\n{'Sum of total sizes of all directories':40}",
        f"\n{'with a total of at most 100000: ':.<50}{ans1:.>20}",
        f"\n{'Total size of smallest directory to':<50}",
        f"\n{'delete: ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day8()
    print(
        "DAY 8",
        f"\n{'Trees visible from outside the grid: ':.<50}{ans1:.>20}",
        f"\n{'Highest scenic score possible: ':.<50}{ans2:.>20}"
    )

    ans1, ans2 = day9()
    print(
        "DAY 9:"
        f"\n{'# of positions visited at least once (Part 1): ':.<50}{ans1:.>20}",
        f"\n{'# of positions visited at least once (Part 2): ':.<50}{ans2:.>20}"
    )

    ans1 = day10()
    print(
        "DAY 10:"
        f"\n{'Sum of the signal strengths: ':.<50}{ans1:.>20}"
    )

    ans1, ans2 = day11()
    print(
        "DAY 11:"
        f"\n{'Monkey business level after 20 rounds: ':.<50}{ans1:.>20}",
        f"\n{'Monkey business level after 10,000 rounds: ':.<50}{ans2:.>20}"
    )
