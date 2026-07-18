class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        l = 0
        r = len(s) - 1

        while l < r:
            move_l = l
            for move_r in range(r, len(s)):
                curr_l = move_l
                curr_r = move_r
                while curr_l < curr_r:
                    if s[curr_l] != s[curr_r]:
                        break
                    
                    if curr_l + 1 == curr_r or curr_l + 2 == curr_r:
                        return s[move_l:move_r+1]

                    curr_l += 1
                    curr_r -= 1

                move_l += 1
            
            r -= 1
        
        return s[0]