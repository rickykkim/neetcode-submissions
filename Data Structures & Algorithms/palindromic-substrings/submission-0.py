class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        if count < 2:
            return count
        
        for i in range(len(s)):
            status = True
            odd_status = True
            odd_l = i - 1
            odd_r = i + 1
            even_status = True
            even_l = i
            even_r = i + 1

            while status:
                # Odd
                if not odd_status or odd_l < 0 or odd_r >= len(s):
                    odd_status = False
                else:
                    if s[odd_l] == s[odd_r]:
                        count += 1
                        odd_l -= 1
                        odd_r += 1
                        odd_status = True
                    else:
                        odd_status = False
                
                # Even
                if not even_status or even_l < 0 or even_r >= len(s):
                    even_status = False
                else:
                    if s[even_l:even_r] == s[even_r:even_l:-1]:
                        count += 1
                        even_l -= 1
                        even_r += 1
                        even_status = True
                    else:
                        even_status = False
            
                status = odd_status or even_status
        
        return count