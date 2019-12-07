# Advent of Code 2016, Day 5
# (c) blu3r4y

import hashlib

import numpy as np


def part1(door_id):
    password, i = "", 0
    for _ in range(8):
        digest = ""
        while not digest.startswith("00000"):
            digest = hashlib.md5((door_id + str(i)).encode()).hexdigest()
            i += 1

        password += digest[5]  # chose 6th character

        print("cracking ...", digest, password)  # status output

    return password


def part2(door_id):
    password, i = ["_"] * 8, 0
    while "_" in password:
        digest = ""
        while not (digest.startswith("00000") and int(digest[5], base=16) < 8):
            digest = hashlib.md5((door_id + str(i)).encode()).hexdigest()
            i += 1

        pos, val = int(digest[5]), digest[6]
        if password[pos] == "_":  # avoid overwrites
            password[pos] = val

        print("cracking ...", digest, "".join(password))  # status output

    return "".join(password)


def load(path):
    return np.loadtxt(path, dtype=int)


if __name__ == "__main__":
    print(part1("abc"))
    print(part1("ugkcyxxp"))

    print(part2("abc"))
    print(part2("ugkcyxxp"))
