class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        # every time, get the highest frequency letter
        # len(so far) - max <= k, keep going
        # > k then move left + 1

        l, r = 0, 0
        cache = {}
        max_len = 0

        while r < len(s):
            if s[r] not in cache:
                cache[s[r]] = 0
            cache[s[r]] += 1
            # (length) - max
            diff = (r - l + 1) - max(cache.values())
            if diff <= k:
                max_len = max(r - l + 1, max_len)
                r += 1
            else:
                cache[s[r]] -= 1
                cache[s[l]] -= 1
                l += 1
        return max_len