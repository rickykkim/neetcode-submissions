class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            #   2  5
            # 1 2  2 5  5 7
            pivot = output[-1]
            curr = intervals[i]
            if curr[0] <= pivot[1]:
                l = min(pivot[0], curr[0])
                r = max(pivot[1], curr[1])
                output[-1] = [l, r]
            else:
                output.append(curr)
        return output