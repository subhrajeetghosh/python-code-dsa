from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def get_frequency(word: str) -> List[int]:
            result = [0] * 26
            for i in range(len(word)):
                result[ord(word[i]) - ord('a')] += 1
            return result
        
        def get_max_frequency(words: List[str]) -> List[int]:
            result = [0] * 26
            for word in words:
                current_freq = get_frequency(word)
                for i in range(len(result)):
                    result[i] = max(result[i], current_freq[i])
            return result
        
        def check_validate(current_word: List[int], max_freq: List[int]) -> bool:
            for i in range(len(current_freq)):
                if current_freq[i] < max_freq[i]:
                    return False
            return True
        
        max_freq = get_max_frequency(words2)
        result = []
        for word in words1:
            current_freq = get_frequency(word)
            if(check_validate(current_freq, max_freq)):
                result.append(word)

        return result