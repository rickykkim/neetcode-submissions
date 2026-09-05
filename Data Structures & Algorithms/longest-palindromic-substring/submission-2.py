class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        max_len = 0
        max_word = s[0]

        for i in range(len(s)):
            # Odd
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    max_word = s[l:r+1]
                l -= 1
                r += 1
            # Even
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    max_word = s[l:r+1]
                l -= 1
                r += 1

        return max_word