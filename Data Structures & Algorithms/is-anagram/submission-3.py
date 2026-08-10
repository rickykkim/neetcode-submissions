class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        
        s_key = dict()
        t_key = dict()
        for i in range(len(s)):
            if s[i] not in s_key:
                s_key[s[i]] = 0
            if t[i] not in t_key:
                t_key[t[i]] = 0
            
            s_key[s[i]] += 1
            t_key[t[i]] += 1
        
        return s_key == t_key