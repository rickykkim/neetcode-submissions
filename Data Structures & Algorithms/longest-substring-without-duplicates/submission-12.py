class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1
        stringHash = {s[l]: l}
        length, max_len = 1, 0

        while r < len(s):
            if s[r] in stringHash:
                l = max(l, stringHash[s[r]] + 1)
                stringHash[s[r]] = r
                r += 1
                max_len = max(length, max_len)
                length = r - l 
            else:
                stringHash[s[r]] = r
                r += 1
                length += 1
        
        return max(max_len, length)