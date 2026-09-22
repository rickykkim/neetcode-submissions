class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += chr(len(word)) + word
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        res = []
        while s:
            length = ord(s[0])
            res.append(s[1:length+1])
            s = s[length+1:]
        
        return res