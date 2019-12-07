# Advent of Code 2016, Day 6
# (c) blu3r4y

from operator import itemgetter

import numpy as np
from toolz.itertoolz import frequencies


def part1(data):
    return solve(data, selector=max)


def part2(data):
    return solve(data, selector=min)


def solve(data, selector=max):
    phrase = ""
    for i in range(data.shape[1]):  # iterate column-wise
        freq = frequencies(data[:, i])  # letter frequencies
        top = selector(freq.items(), key=itemgetter(1))[0]  # key with highest/lowest value
        phrase += top

    return phrase


def load(path):
    return np.array([list(e.strip()) for e in open(path).readlines()])


if __name__ == "__main__":
    print(part1(load(r"../assets/day6_demo.txt")))
    print(part1(load(r"../assets/day6.txt")))

    print(part2(load(r"../assets/day6_demo.txt")))
    print(part2(load(r"../assets/day6.txt")))
