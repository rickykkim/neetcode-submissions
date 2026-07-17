class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        reverse = ""

        for i in range(len(s)):
            rev_idx = -i - 1
            fwd = s[i]
            rev = s[rev_idx]

            if ord(fwd) >= ord("0") and ord(fwd) <= ord("9"):
                forward += fwd
            elif (ord(fwd) >= ord("A") and ord(fwd) <= ord("Z")) or (ord(fwd) >= ord("a") and ord(fwd) <= ord("z")):
                forward += fwd.lower()
            
            if ord(rev) >= ord("0") and ord(rev) <= ord("9"):
                reverse += rev
            elif (ord(rev) >= ord("A") and ord(rev) <= ord("Z")) or (ord(rev) >= ord("a") and ord(rev) <= ord("z")):
                reverse += rev.lower()
        
        return forward == reverse