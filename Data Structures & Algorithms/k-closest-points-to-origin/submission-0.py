class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2)**(0.5)
            dist.append([distance, point[0], point[1]])

        heapq.heapify(dist)
        res = []
        while k > 0:
            result = heapq.heappop(dist)
            res.append([result[1], result[2]])
            k -= 1
        
        return res