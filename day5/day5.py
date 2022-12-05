from aoctools.input import get_input
from aoctools.timelogger import timelogger
from copy import deepcopy



def join_str(stack_list: list) -> str:
    return "".join([item[-1] for item in stack_list])

@timelogger(2022, 5)
def day5():
    input_list = get_input(2022, 5)
    crates = input_list[:input_list.index('')]
    procedure = input_list[input_list.index('') + 1:]

    num_stacks = [int(stack_num) for stack_num in crates[-1].split()][-1]

    stacks = [[] for _ in range(num_stacks)]

    for line in crates[::-1]:
        for idx, cont in enumerate(line[1::4]):
            if cont not in " ":
                stacks[idx].append(cont)

    stacks_pt2 = deepcopy(stacks)

    def move_crates(amount: int, origin: int, target: int):
        crates_moved = []
        for _ in range(amount):
            # Part 1
            crate = stacks[origin - 1].pop()
            stacks[target - 1].append(crate)

            # Part 2
            crates_moved.append(stacks_pt2[origin - 1].pop())

        stacks_pt2[target - 1].extend(crates_moved[::-1])

    for item in procedure:
        item = item.split()
        move_crates(int(item[1]), int(item[3]), int(item[5]))

    return [*map(join_str, [stacks, stacks_pt2])]


if __name__ == "__main__":
    pt1, pt2 = day5()

    print(
        f"\n{'Crates on top of each stack (Part 1):':<40} {pt1:>10}",
        f"\n{'Crates on top of each stack (Part 2):':<40} {pt2:>10}"
    )
