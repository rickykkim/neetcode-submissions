class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += chr(len(word)) + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        decoded = []

        while s:
            size = ord(s[0])
            word = s[1:size+1]
            decoded.append(word)
            s = s[size+1:]
        
        return decoded