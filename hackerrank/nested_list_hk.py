#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
if __name__ == '__main__':
    list_dict = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_dict[name] = score

    sorted_value = dict(sorted(list_dict.items(), key=lambda item: item[1]))
    second_lowest = list(set(sorted_value.values()))[1]
    final_list = []
    for i in sorted_value.keys():
        if sorted_value.get(i) == second_lowest:
            final_list.append(i)
    for i in sorted(final_list):
        print(i)


# nested list implementation here
def another_method():
    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]
    new_list = []
    for i in score_list:
        new_list.append([i, score_list[i]])
    new_list.sort()
    result = new_list[1][1]
    result.sort()
    print(*result, sep="\n")
