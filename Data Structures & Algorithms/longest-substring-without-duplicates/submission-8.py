class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 1
        hash_map = {s[l]: 0}
        longest = 0

        while r < len(s):
            if s[r] not in s[l:r]:
                hash_map[s[r]] = r
                if r == len(s) - 1:
                    longest = max(longest, r - l + 1)
                r += 1
            else:
                longest = max(longest, r - l)
                l = hash_map[s[r]] + 1
                hash_map[s[r]] = r
                r += 1

        return longest