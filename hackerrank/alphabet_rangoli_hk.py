#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def print_rangoli(size):
    space = (((size * 2) - 1) * 2) - 1
    for i in range(1, space + 1):
        print_alphabet(2, 3)


def print_alphabet(start, end):
    while ord(start) < ord(end):
        print(start + "-")
        start = chr(ord(start) + 1)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
