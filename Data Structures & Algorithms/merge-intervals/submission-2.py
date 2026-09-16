class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        # 2 5
        # 2 4   2 5     4  6    5 8
        for i in range(1, len(intervals)):
            incoming = intervals[i]
            pivot = res[-1]
            if incoming[0] <= pivot[1]:
                l = min(pivot[0], incoming[0])
                r = max(pivot[1], incoming[1])
                res[-1] = [l, r]
            else:
                res.append(incoming)
        
        return res