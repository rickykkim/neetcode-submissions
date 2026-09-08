class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cache = {}
        for letter in s1:
            if letter not in cache:
                cache[letter] = 0
            cache[letter] += 1

        for i in range(len(s2) - len(s1) + 1):
            temp = s2[i:i+len(s1)]
            temp_cache = {}
            for letter in temp:
                if letter not in temp_cache:
                    temp_cache[letter] = 0
                temp_cache[letter] += 1
            
            if cache == temp_cache:
                return True
        
        return False
        