# Advent of Code 2016, Day 7
# (c) blu3r4y

import re

from more_itertools import flatten, windowed


def part1(ips):
    count = 0
    for sup, hyp in ips:
        if any(map(has_abba, sup)) and not any(map(has_abba, hyp)):
            count += 1
    return count


def part2(ips):
    count = 0
    for sup, hyp in ips:
        for a, b, _ in flatten(map(has_aba, sup)):
            bab = b + a + b
            if any([bab in e for e in hyp]):
                count += 1
                break
    return count


def has_abba(text):
    # rolling window with size = 4 and check
    for a, b, c, d in windowed(text, 4):
        if a == d and b == c and a != b:
            return True


def has_aba(text):
    matches = []
    # rolling window with size = 3 and check
    for a, b, c in windowed(text, 3):
        if a == c and a != b:
            matches.append(a + b + c)

    return matches


def load(path):
    data = []

    lines = open(path).read().splitlines()
    for line in lines:
        sup = re.split(r"\[|\]", line)  # main sequences
        hyp = re.findall(r"\[(\w+)\]", line)  # hypernet sequences
        for h in hyp:
            sup.remove(h)
        data.append((sup, hyp))

    return data


if __name__ == "__main__":
    print(part1(load(r"../assets/day7_demo1.txt")))
    print(part1(load(r"../assets/day7.txt")))

    print(part2(load(r"../assets/day7_demo2.txt")))
    print(part2(load(r"../assets/day7.txt")))
