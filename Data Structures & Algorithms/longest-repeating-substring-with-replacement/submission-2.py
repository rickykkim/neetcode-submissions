class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        count = {s[0]: 1}
        res = 0
        l = 0
        r = l + 1
        
        while l < len(s) - 1:
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1

            curr = (r - l + 1) - max(count.values())

            if curr <= k:
                if r < len(s) - 1:
                    r += 1
                else:
                    res = max(res, r - l + 1)
                    l += 1
                    r = l + 1
                    count = {s[l]: 1}
            else:
                r -= 1
                res = max(res, r - l + 1)
                l += 1
                r = l + 1
                count = {s[l]: 1}
        
        return res
