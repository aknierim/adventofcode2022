from aoctools.input import get_input
from aoctools.timelogger import timelogger
from collections import defaultdict
from pathlib import Path


@timelogger(2022, 7)
def dir_parser(input):
    current_path = None
    dirs = defaultdict(int)
    for line in input:
        match line.split():
            # ignore ls command
            case ["$" "ls"]:
                pass
            # case for cd command and directory
            case ["$", "cd", dir]:
                match dir:
                    # find root directory
                    case "/":
                        current_path = Path("/")
                    # find execution of 'cd ..' to save current dirs
                    # parent dir as new curren dir
                    case "..":
                        current_path = current_path.parents[0]
                    # find any other directory name
                    case _:
                        current_path = current_path / dir
            # Find files and add their sizes to the dirs defaultdict.
            # This results in the sizes being added for each directory
            # and subdirectory
            case [file_size, file_name] if file_size.isdigit():
                file_size = int(file_size)
                for path in [current_path, *current_path.parents]:
                      dirs[path] += file_size
    
    return dirs


@timelogger(2022, 7, part=1)
def part1(dirs: defaultdict) -> int:
    total_size = 0
    for item in dirs.values():
        if item <= 100_000:
            total_size += item

    return total_size


@timelogger(2022, 7, part=2)
def part2(dirs: defaultdict) -> int:
    DISK_TOTAL = 70_000_000
    NEEDED = 30_000_000

    curr_du = list(dirs.values())[0]

    total_avail = DISK_TOTAL - curr_du
    to_free = NEEDED - total_avail

    chonk_dirs = []
    for val in list(dirs.values())[1:]:
        if val >= to_free:
            chonk_dirs.append(val)

    return min(chonk_dirs)


def day7() -> tuple[int, int]:
    input = get_input(2022, 7)

    dirs = dir_parser(input)

    return part1(dirs), part2(dirs)


if __name__ == "__main__":
    size_pt1, size_pt2 = day7()

    print(
        f"{'Sum of total sizes of all directories':40}",
        f"\n{'with a total of at most 100000:':<40} {size_pt1:>10}",
        f"\n{'Total size of smallest directory to':<40}",
        f"\n{'delete:':<40} {size_pt2:>10}"
    )
