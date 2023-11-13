#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
def minion_game(s):
    stuart = 0
    kevin = 0
    vowels = "AEIOU"

    for i in range(len(s)):
        c = s[i]
        if c in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

