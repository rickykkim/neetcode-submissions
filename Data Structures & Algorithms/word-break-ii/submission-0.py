class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[len(s)].append("")
        output = []

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    for add_word in dp[i + len(word)]:
                        if add_word == "":
                            dp[i].append(word)
                        else:
                            dp[i].append(word + " " + add_word)
        
        return dp[0]
        
        # idx=0 must be true
        # racecar   is  car
        # 2    1      1   1