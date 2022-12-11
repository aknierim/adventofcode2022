"""Advent of Code Day 11 solution
"""
# from aoctools.input import get_input
from aoctools.timelogger import timelogger


def multiply_list(inputlist):
    result = 1
    for num in inputlist:
        result = result * num
    return result


class MonkeyTrouble():

    __slots__ = (
        "input",
        "monkeys",
        "monkeys_2",
        "business_dict",
        "business_dict_2",
        "new_divisor"
    )

    def __init__(
        self,
        input
    ):
        self.monkeys = []
        self.monkeys_2 = []
        for lines in input:
            lines = lines.splitlines()
            self.monkeys.append(self.monkey_stats(lines))
            self.monkeys_2.append(self.monkey_stats(lines))

        # part 1
        self.business_dict = {i: 0 for i, _ in enumerate(input)}

        # part 2
        self.business_dict_2 = {i: 0 for i, _ in enumerate(input)}
        self.new_divisor = multiply_list([monkey["divisor"] for monkey in self.monkeys])

    def monkey_stats(self, lines):
        """Creates a dict with all monkey stats from the input.

        Very helpful here: https://stackoverflow.com/a/9686074,
        also learned some more about the usage of lambda functions
        """

        monkey_dict = {
            "items": [int(x) for x in lines[1].replace(":", " ").replace(",", " ").split()[2:]],
            "operation": lambda old: eval(lines[2].split("new = ")[1]),
            "test": lambda x: x % int(lines[3].split("by ")[1]) == 0,
            "divisor": int(lines[3].split("by ")[1]),
            "cond": {
                True: int(lines[4].split("monkey ")[1]),
                False: int(lines[5].split("monkey ")[1]),
            }
        }
        return monkey_dict

    @timelogger(2022, 11, part=1)
    def part1(self, rounds):
        for _ in range(rounds):
            for idx, monkey in enumerate(self.monkeys_2):
                for item in monkey["items"]:
                    self.business_dict[idx] += 1

                    new = monkey["operation"](item) // 3
                    test = monkey["test"](new)
                    throw_to = monkey["cond"][test]

                    self.monkeys_2[throw_to]["items"].append(new)
                monkey["items"] = []

        most_active_two = [*self.business_dict.values()]
        most_active_two.sort()

        return most_active_two[-2] * most_active_two[-1]

    @timelogger(2022, 11, part=2)
    def part2(self, rounds):
        for _ in range(rounds):
            for idx, monkey in enumerate(self.monkeys):
                for item in monkey["items"]:
                    self.business_dict_2[idx] += 1

                    new = monkey["operation"](item) % self.new_divisor
                    test = monkey["test"](new)
                    throw_to = monkey["cond"][test]

                    self.monkeys[throw_to]["items"].append(new)
                monkey["items"] = []

        most_active_two = [*self.business_dict_2.values()]
        most_active_two.sort()

        return most_active_two[-2] * most_active_two[-1]


def day11():
    # will use get_input() later, but I'm hungry rn :D
    with open("day11/day11.txt") as f:
        input = f.read().split("\n\n")

    trouble = MonkeyTrouble(input)

    return trouble.part1(20), trouble.part2(10_000)


if __name__ == "__main__":
    ans1, ans2 = day11()

    print(ans1, ans2)
