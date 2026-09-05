class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        count = len(s)

        for i in range(len(s)):
            # Odd
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # Even
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count