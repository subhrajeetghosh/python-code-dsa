#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

def count_substring(string, sub_string):
    count_sb_string = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            current_ind = i
            is_found = True
            for j in sub_string:
                if current_ind < len(string) and string[current_ind] == j:
                    current_ind += 1
                else:
                    is_found = False
                    break
            if is_found:
                count_sb_string += 1
    return count_sb_string


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)