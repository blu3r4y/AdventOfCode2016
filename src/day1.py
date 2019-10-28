# Advent of Code 2016, Day 1
# (c) blu3r4y

from parse import *


def part1(directions):
    pos, orient = 0, 1j  # start at (0, 0) facing north

    for way, step in directions:
        # rotate and move
        orient *= 1j if way == "L" else -1j
        pos += orient * step

    # manhattan distance
    return int(abs(pos.real) + abs(pos.imag))


def part2(directions):
    pos, orient = 0, 1j 
    path = set([pos])

    for way, step in directions:
        orient *= 1j if way == "L" else -1j

        for _ in range(step):
            pos += orient

            # trace visited coordinates and stop on duplicates
            if pos in path:
                return int(abs(pos.real) + abs(pos.imag))
            path.add(pos)


def load(data):
    # parse "R2" -> (R, 2)
    return [parse("{:l}{:d}", e) for e in data.split(", ")]


if __name__ == "__main__":
    print(part1(load("R2, L3")))
    print(part1(load("R2, R2, R2")))
    print(part1(load("R5, L5, R5, R3")))
    print(part1(load(open(r"../assets/day1.txt").readlines()[0])))

    print(part2(load("R8, R4, R4, R8")))
    print(part2(load(open(r"../assets/day1.txt").readlines()[0])))
