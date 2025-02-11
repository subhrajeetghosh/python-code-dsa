class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index] + s[index + len(part):]
        return s
    
    def removeOccurrences_2nd_method(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s