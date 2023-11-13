#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique_char = ""
        current_str = string[i:i + k]
        for char in current_str:
            if char not in unique_char:
                unique_char += char
        print(unique_char)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
