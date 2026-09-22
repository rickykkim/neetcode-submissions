class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        cache = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in cache:
                cache[temp] = []
            cache[temp].append(word)
        
        return list(cache.values())