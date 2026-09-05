class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        hashMap = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)
        
        return list(hashMap.values())