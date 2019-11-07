# Advent of Code 2016, Day 4
# (c) blu3r4y

from functools import partial

import numpy as np
from parse import parse, with_pattern
from toolz.itertoolz import frequencies


def part1(rooms):
    result = 0

    for r in rooms:
        freq = frequencies(r["name"].replace("-", ""))  # letter frequencies
        freq = sorted(freq.items(), key=lambda e: (-e[1], e[0]))  # sort by counts first, and then by letter
        hash_ = ''.join(map(lambda e: e[0], freq[:5]))  # calculate expected hash

        if hash_ == r["hash"]:
            result += r["id"]

    return result


def part2(rooms):
    for r in rooms:
        # decrypt individual words and find northpole object storage
        names = tuple(map(partial(_rotate_str, offset=r["id"]), r["name"].split("-")))
        if names == ("northpole", "object", "storage"):
            return r["id"]


def _rotate_str(text, offset):
    arr = (np.array(list(map(ord, text))) - ord('a') + offset) % 26 + ord('a')  # a-z shift cipher
    new = ''.join(map(chr, arr))  # convert chr list to str
    return new


def load(path):
    @with_pattern(r"[a-z-]+")  # match letters and dashes
    def _name_pattern(text):
        return text[:-1]  # remove trailing dash

    return [parse("{name:name}{id:d}[{hash:l}]", line, dict(name=_name_pattern)) for line in open(path).readlines()]


if __name__ == "__main__":
    print(part1(load(r"../assets/day4_demo.txt")))
    print(part1(load(r"../assets/day4.txt")))

    print(part2(load(r"../assets/day4.txt")))
