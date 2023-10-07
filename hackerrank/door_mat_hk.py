#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
main, side = map(int, input().split())
for i in range(main // 2):
    print((".|." * (i * 2 + 1)).center(side, "-"))
print("WELCOME".center(side, "-"))
for i in reversed(range(main // 2)):
    print((".|." * (i * 2 + 1)).center(side, "-"))
