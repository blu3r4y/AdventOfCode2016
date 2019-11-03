# Advent of Code 2016, Day 3
# (c) blu3r4y

import numpy as np


def part1(t):
    # triangular inequalities
    c1 = t[:, 0] + t[:, 1] > t[:, 2]
    c2 = t[:, 1] + t[:, 2] > t[:, 0]
    c3 = t[:, 0] + t[:, 2] > t[:, 1]

    return np.sum(c1 & c2 & c3)


def part2(t):
    # transpose and wrap every 3rd column
    return part1(t.T.reshape(len(t), 3))


def load(path):
    return np.loadtxt(path, dtype=int)


if __name__ == "__main__":
    print(part1(load(r"../assets/day3.txt")))
    print(part2(load(r"../assets/day3.txt")))
