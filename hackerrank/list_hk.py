#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

if __name__ == '__main__':
    N = int(input())
    list_test = []
    for _ in range(N):
        command, *data = input().split()
        data = list(map(int, data))
        if command == "insert":
            list_test.insert(data[0], data[1])
        elif command == "remove":
            list_test.remove(data[0])
        elif command == "append":
            list_test.append(data[0])
        elif command == "pop":
            list_test.pop()
        elif command == "sort":
            list_test.sort()
        elif command == "reverse":
            list_test.reverse()
        else:
            print(list_test)
