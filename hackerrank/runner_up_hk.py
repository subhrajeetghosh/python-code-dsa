#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(map(int, input().split())), reverse=True)
    print(arr[1])
