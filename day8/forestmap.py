import matplotlib as mpl
import matplotlib.pyplot as plt
from aoctools.input import get_input

def main():
    input = get_input(2022, 8)
    input = [list(map(int, item)) for item in input]

    # ht_min = min([min(item) for item in input])
    ht_max = max([max(item) for item in input])


    fig, ax = plt.subplots(1, 1, figsize=(8,6), layout='constrained')
    
    cmap = plt.get_cmap('YlGn').copy()
    cmap.set_under('xkcd:light brown')

    c = ax.pcolormesh(input, cmap=cmap, vmin=1, vmax=ht_max)
    fig.colorbar(c, ax=ax, norm=mpl.colors.Normalize(vmin=-1, vmax=ht_max))

    plt.savefig("day8/forestmap.pdf")


if __name__ == "__main__":
    main()

