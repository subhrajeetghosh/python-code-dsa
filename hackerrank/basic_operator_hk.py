#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
"""
if __name__ == '__main__':
    main_list = []
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    main_list.append([i, j, k])

    print(main_list)

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
