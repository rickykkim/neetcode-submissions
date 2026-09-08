class Solution:
    from collections import defaultdict

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = defaultdict(int)
        have = defaultdict(int)
        for c in s1:
            need[c] += 1
        for c in s2[:k]:
            have[c] += 1

        alpha = "abcdefghijklmnopqrstuvwxyz"
        match = sum(1 for c in alpha if need[c] == have[c])
        if match == 26:
            return True

        for i in range(k, len(s2)):
            for c, delta in ((s2[i - k], -1), (s2[i], +1)):   # leaving letter, then entering letter
                if need[c] == have[c]:
                    match -= 1                # it was counted as matching, remove that
                have[c] += delta
                if need[c] == have[c]:
                    match += 1                # it matches now, count it
            if match == 26:
                return True
        return False