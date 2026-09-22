class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cache_s, cache_t = {}, {}
        for idx in range(len(s)):
            if s[idx] not in cache_s:
                cache_s[s[idx]] = 0
            if t[idx] not in cache_t:
                cache_t[t[idx]] = 0
            cache_s[s[idx]] += 1
            cache_t[t[idx]] += 1
        
        return cache_s == cache_t