#  Copyright (c) 2024.
#  @Author Subhrajeet Ghosh

def customSortString(self, order: str, s: str) -> str:
    result = []
    s_array = [0] * 26
    order_array = [0] * 26
    for st in s:
        s_array[ord(st) - ord('a')] += 1
    for st in order:
        while s_array[ord(st) - ord('a')] > 0:
            s_array[ord(st) - ord('a')] -= 1
            order_array[ord(st) - ord('a')] += 1
            result.append(st)
    for st in s:
        if order_array[ord(st) - ord('a')] > 0:
            continue
        result.append(st)
    return ''.join(result)
