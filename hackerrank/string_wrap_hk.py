#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
import textwrap


def wrap(string, max_width):
    list_data = textwrap.wrap(string, max_width)
    string_data = ""
    for i in range(len(list_data)):
        if i == len(list_data)-1:
            string_data += list_data[i]
        else:
            string_data += list_data[i] + "\n"
    return string_data


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
