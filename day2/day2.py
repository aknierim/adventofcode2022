"""Advent of Code 2022 Day 2 solution.
"""
from aoctools.input import get_input

def main():
    lines = get_input(2022, 2)

    # Part 1
    score = 0
    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)
        player = "XYZ".index(player)

        if (opp - player == -1) or (opp - player == 2):
            score += player + 7
        elif opp - player == 0:
            score += player + 4
        else:
            score += player + 1

    score_p1 = score

    # Part 2
    score = 0
    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)

        match player:
            case "X":
                # score for chosen shape + 0 (for losing)
                score += (opp - 1) % 3 + 1
            case "Y":
                # score equals opponents score + 3 (for draw)
                score += opp + 4
            case "Z":
                # score for chosen shape + 6 (for winning)
                score += (opp + 1) % 3 + 7

    score_p2 = score

    return score_p1, score_p2

if __name__ == "__main__":
    score_p1, score_p2 = main()

    print(
        f"{'Score for part 1:':<18} {score_p1:>10}",
        f"\n{'Score for part 2:':<18} {score_p2:>10}"
    )
