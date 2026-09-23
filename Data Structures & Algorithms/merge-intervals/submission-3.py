class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # 1 3: 1 5, 2 3, 3 5
            if intervals[i][0] <= res[-1][1]:
                left = min(res[-1][0], intervals[i][0])
                right = max(res[-1][1], intervals[i][1])
                res[-1] = [left, right]
            else:
                res.append(intervals[i])
        return res