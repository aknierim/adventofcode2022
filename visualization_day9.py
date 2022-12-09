import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
import numpy as np
from aoctools.input import get_input
from day9.day9 import RopeBridge


def visualization(visited_x, visited_y):
    colors = cm.gist_rainbow(np.linspace(0, 1, len(visited_x.columns)))
    my_cmap = ListedColormap(colors[:,:-1])

    fig, ax = plt.subplots(1, 1, figsize=(16,10), layout="constrained", dpi=400)
    sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=plt.Normalize(vmin=0, vmax=10))
    
    ax.axis("off")
    fig.patch.set_facecolor('#3a3d41')

    for idx, _ in enumerate(visited_x.columns):
        ax.plot(
            visited_x[idx], 
            visited_y[idx], 
            marker="o",
            linestyle="-",
            ms=0.3, 
            linewidth=0.5, 
            color=colors[idx], 
            label='Head' if idx == 0 else idx, 
            alpha=0.7
    )
    
    l = ax.legend(title="Knots", frameon=False, labelcolor='white')
    plt.setp(l.get_title(), color='white')
    
    ax.set_title(
        "Advent of Code Day 9 | Rope Bridge", 
        fontsize=16, 
        color='white'
    )

    plt.savefig("day9/day9_visualisation.png")


def main():
    input = get_input(2022, 9)
    ropes = RopeBridge(input)
    visited = ropes.pos_tracker()

    x = []
    y = []
    for item in visited:
        xval = []
        yval = []
        
        for idx in range(len(item)):
            xval.append(item[idx][0])
            yval.append(item[idx][1])
        x.append(xval)
        y.append(yval)

    visited_x = pd.DataFrame(x).T
    visited_y = pd.DataFrame(y).T

    visualization(visited_x, visited_y)


if __name__ == "__main__":
    main()

