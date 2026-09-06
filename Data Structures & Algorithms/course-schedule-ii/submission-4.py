class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cache = {}
        for p in prerequisites:
            if p[0] not in cache:
                cache[p[0]] = []
            cache[p[0]].append(p[1])
        
        visited = set()
        path = []

        def dfs(i):
            if i in visited:
                return False
            if i not in cache:
                if i not in path:
                    path.append(i)
                return True
            
            visited.add(i)
            for j in cache[i]:
                # How to align courses
                if not dfs(j):
                    return False        
            
            visited.remove(i)
            cache[i] = []
            if i not in path:
                path.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
        