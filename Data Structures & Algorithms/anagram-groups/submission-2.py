class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        elif len(strs) == 1:
            return [[strs[0]]]
        
        keys = dict()
        for word in strs:
            sort_word = str(sorted(word))
            if sort_word not in keys:
                keys[sort_word] = []
            keys[sort_word].append(word)
        
        return list(keys.values())
            