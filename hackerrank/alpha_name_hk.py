#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
import os


def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))


if __name__ == '__main__':
    print(solve(input()))
