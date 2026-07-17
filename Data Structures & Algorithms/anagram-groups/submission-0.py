class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        anagram_result = []

        for item in strs:
            item_counter = {}
            for letter in item:
                if letter not in item_counter:
                    item_counter[letter] = 0
                item_counter[letter] += 1
            
            if item_counter not in anagram:
                anagram.append(item_counter)
                anagram_result.append([item])
            else:
                idx = anagram.index(item_counter)
                anagram_result[idx].append(item)
        
        return anagram_result