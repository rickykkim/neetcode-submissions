class Solution:
    def compress(self, chars: List[str]) -> int:
        # i = edit index / k = traverse index
        # i = 0 / k = 1 initialize
        # if [i] == [k]: count += 1
        # else: 
        # 1) if count == 1: update index i with [k-1] value
        # 2) else: update index i with [k-1] value + i+1... with count
        # repeat this until k == len(chars)

        i, k = 0, 1
        prev, count = chars[0], 1
        while k < len(chars):
            if prev == chars[k]:
                count += 1
            else:
                if count == 1:
                    chars[i] = chars[k-1]
                    i += 1
                else:
                    temp = chars[k-1] + str(count)
                    for idx in range(len(temp)):
                        chars[i] = temp[idx]
                        i += 1
                prev = chars[k]
                count = 1
            k += 1
        
        # address what happens at the last index
        if count == 1:
            chars[i] = chars[k-1]
            i += 1
        else:
            temp = chars[k-1] + str(count)
            for idx in range(len(temp)):
                chars[i] = temp[idx]
                i += 1
        
        return i