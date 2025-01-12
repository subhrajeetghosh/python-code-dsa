class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        locked_stack = []
        unlocked_stack = []
        for i in range(len(s)):
            if s[i] == ')' and locked[i] == '1':
                if locked_stack:
                    locked_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
                else:
                    return False
            else:
                if locked[i] == '1':
                    locked_stack.append(i)
                else:
                    unlocked_stack.append(i)
        if len(locked_stack) > len(unlocked_stack):
            return False
        while locked_stack:
            if locked_stack[-1] > unlocked_stack[-1]:
                return False
            else:
                locked_stack.pop()
                unlocked_stack.pop()
        return len(unlocked_stack) % 2 == 0
