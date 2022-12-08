from aoctools.input import get_input
from aoctools.timelogger import timelogger 


class TreeVisibility:

    __slots__ = (
        'input',
        'tree_x',
        'tree_y',
        'height',
    )

    def __init__(
        self,
        input,
        tree_x,
        tree_y,
        height
    ):

        self.input = input
        self.tree_x = tree_x
        self.tree_y = tree_y
        self.height = height

    def horizontal(self):
        visible = []
        for idx in range(0, self.tree_x):
            if self.input[self.tree_y][idx] < self.height:
                visible.append(True)
            else:
                visible.append(False)

        return all(visible)

    def horizontal_reversed(self, row):
        visible = []
        for idx in range(self.tree_x + 1, len(row)):
            if self.input[self.tree_y][idx] < self.height:
                visible.append(True)
            else:
                visible.append(False)

        return all(visible)

    def vertical(self):
        visible = []
        for idx in range(0, self.tree_y):
            if self.input[idx][self.tree_x] < self.height:
                visible.append(True)
            else:
                visible.append(False)

        return all(visible)

    def vertical_reversed(self):
        visible = []
        for idx in range(self.tree_y + 1, len(self.input)):
            if self.input[idx][self.tree_x] < self.height:
                visible.append(True)
            else:
                visible.append(False)

        return all(visible)


class ScenicScore(TreeVisibility):

    __slots__ = (
        'input',
        'tree_x',
        'tree_y',
        'height',
        'row'
    )

    def __init__(
        self,
        input,
        tree_x,
        tree_y,
        height,
        row
    ):

        super().__init__(input, tree_x, tree_y, height)
        self.row = row

    def score_right(self):
        right = 0
        for idx in range(self.tree_x + 1, len(self.row)):
            right += 1
            if self.input[self.tree_y][idx] >= self.height:
                break

        return right

    def score_left(self):
        left = 0
        for idx in reversed(range(0, self.tree_x)):
            left += 1
            if self.input[self.tree_y][idx] >= self.height:
                break

        return left

    def score_up(self):
        up = 0
        for idx in reversed(range(0, self.tree_y)):
            up += 1
            if self.input[idx][self.tree_x] >= self.height:
                break

        return up

    def score_down(self):
        down = 0
        for idx in range(self.tree_y + 1, len(self.input)):
            down += 1
            if self.input[idx][self.tree_x] >= self.height:
                break

        return down


@timelogger(2022, 8)
def day8():
    input = get_input(2022, 8)

    scenic_score = []
    ans = 0
    for tree_y, row in enumerate(input):
        for tree_x, height in enumerate(row):
            vis = TreeVisibility(input, tree_x, tree_y, height)
            scen = ScenicScore(input, tree_x, tree_y, height, row)

            ans += (
                vis.horizontal()
                or vis.horizontal_reversed(row)
                or vis.vertical()
                or vis.vertical_reversed()
            )

            score = (
                scen.score_left()
                * scen.score_right()
                * scen.score_up()
                * scen.score_down()
            )
            scenic_score.append(score)

    return ans, max(scenic_score)


if __name__ == "__main__":
    ans1, ans2 = day8()

    print(
        f"{'Trees visible from outside the grid:':<40} {ans1:>10}",
        f"\n{'Highest scenic score possible:':<40} {ans2:>10}"
    )
