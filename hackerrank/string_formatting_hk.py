#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def print_formatted(number):
    space = len(bin(number)[2:]) + 1
    for i in range(1, number + 1):
        print(str(i).rjust(space - 1) + oct(i)[2:].rjust(space) + hex(i)[2:].upper().rjust(space) + bin(i)[2:].rjust(
            space))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
