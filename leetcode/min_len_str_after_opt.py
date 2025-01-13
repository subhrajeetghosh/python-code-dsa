class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for i in range(26):
            if arr[i] > 2:
                result += 2 if arr[i] % 2 == 0 else 1
            else: 
                result += arr[i]
        return result