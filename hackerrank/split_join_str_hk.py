#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh


def split_and_join(line):
    line_list = line.split(" ")
    return "-".join(line_list)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
