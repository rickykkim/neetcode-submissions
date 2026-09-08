class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        list is already sorted
        non overlapping = complete no overlap
        it can be inserted at the beginning, middle, end
        BUT regardless the incoming can span more than one existing list

        [1 3]   [4 6]
        incoming [1 5]
        if possible
            merge it, replace i
            count += 1
            break

        if count == 0: add it at the end and return 

        [1 5]   [4 6]   [7 8]
        while i < len()-1
            i, i+1
            if both are mergeable, merge
                insert at i 
                drop i+1 and i+2
            else:
                i += 1
        '''
        # first insert the newInterval anywhere
        count = 0
        for i in range(len(intervals)):
            # merge
            left = newInterval[1] >= intervals[i][0]
            right = newInterval[0] <= intervals[i][1]

            if left and right:
                min_val = min(newInterval[0], intervals[i][0])
                max_val = max(newInterval[1], intervals[i][1])
                intervals[i] = [min_val, max_val]
                count += 1
                break
            
            elif newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                count += 1
                break

        if count == 0:
            intervals.append(newInterval)
            return intervals
        
        # take care of remaining merge opportunities
        while i < len(intervals) - 1:
            l, r = intervals[i], intervals[i+1]
            left = l[1] >= r[0]
            right = l[0] <= r[1]

            if left and right:
                min_val = min(l[0], r[0])
                max_val = max(l[1], r[1])
                intervals[i] = [min_val, max_val]
                del intervals[i+1]
            else:
                i += 1
        
        return intervals
