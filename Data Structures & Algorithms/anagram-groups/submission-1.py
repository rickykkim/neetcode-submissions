class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for item in strs:
            item_sorted = sorted(item)
            item_modified = ''.join(item_sorted)

            if item_modified not in anagram:
                anagram[item_modified] = []
            anagram[item_modified].append(item)
            
        return list(anagram.values())