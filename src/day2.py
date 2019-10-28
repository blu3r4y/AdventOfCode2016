# Advent of Code 2016, Day 2
# (c) blu3r4y

import math


def part1(instructions):
    # start at (0, 0) and stay within abs(...) <= sqrt(2)
    return solve(instructions, 0, math.sqrt(2), num_to_pin)


def part2(instructions):
    # start at (-2, 0j) and stay within abs(...) <= 2
    return solve(instructions, -2, 2, num_to_designer_pin)


def solve(instructions, pos, radius, mapper):
    pin = ""
    for moves in instructions:
        for move in moves:
            if abs(pos + move) <= radius:  # only move inside the pad
                pos += move
        pin += str(mapper(pos))

    return pin


def num_to_pin(num):
    num += (1 - 1j)  # reset origin to upper left
    idx = int(num.real + 3 * abs(num.imag))  # flatten index
    return idx + 1  # regular 1-9 pad


def num_to_designer_pin(num):
    num += (2 - 2j)  # reset origin to upper left
    idx = int(num.real + 5 * abs(num.imag))  # flatten index

    pad = \
        "  1  " \
        " 234 " \
        "56789" \
        " ABC " \
        "  D  "
    return pad[idx]


def load(data):
    mapping = {"U": 1j, "R": 1, "D": -1j, "L": -1}
    return [[mapping[f] for f in e.strip()] for e in data]


if __name__ == "__main__":
    print(part1(load(open(r"../assets/day2_demo.txt").readlines())))
    print(part1(load(open(r"../assets/day2.txt").readlines())))

    print(part2(load(open(r"../assets/day2_demo.txt").readlines())))
    print(part2(load(open(r"../assets/day2.txt").readlines())))
