class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if len(q) > 0 and q[0][1] == time:
                cpu, t = q.popleft()
                heapq.heappush(maxHeap, cpu)
            if len(maxHeap) == 0:
                continue
            cpu = 1 + heapq.heappop(maxHeap)
            if cpu < 0:
                q.append((cpu, time + n + 1))
        
        return time