class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        hashMap = {}
        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word not in hashMap:
                hashMap[new_word] = []
            hashMap[new_word].append(word)
        
        return list(hashMap.values())