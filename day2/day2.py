"""Advent of Code 2022 Day 2 solution.
"""
from aoctools.input import get_input


def day2():
    lines = get_input(2022, 2)

    # Part 1
    score_p1 = 0
    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)
        player = "XYZ".index(player)

        if (opp - player == -1) or (opp - player == 2):
            score_p1 += player + 7
        elif opp - player == 0:
            score_p1 += player + 4
        else:
            score_p1 += player + 1

    # Part 2
    score_p2 = 0
    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)

        match player:
            case "X":
                # score_p2 for chosen shape + 0 (for losing)
                score_p2 += (opp - 1) % 3 + 1
            case "Y":
                # score_p2 equals opponents score_p2 + 3 (for draw)
                score_p2 += opp + 4
            case "Z":
                # score_p2 for chosen shape + 6 (for winning)
                score_p2 += (opp + 1) % 3 + 7

    return score_p1, score_p2


if __name__ == "__main__":
    score_p1, score_p2 = day2()

    print(
        f"{'Score for part 1:':<18} {score_p1:>10}",
        f"\n{'Score for part 2:':<18} {score_p2:>10}"
    )
