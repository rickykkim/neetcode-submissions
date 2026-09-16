class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[len(s)].append("")

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    for addWord in dp[i + len(word)]:
                        if addWord == "":
                            dp[i].append(word)
                        else:
                            dp[i].append(word + " " + addWord)
        
        return dp[0]