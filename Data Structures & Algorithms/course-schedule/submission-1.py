class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {}
        for course in prerequisites:
            if course[0] not in mapping:
                mapping[course[0]] = []
            mapping[course[0]].append(course[1])
        

        visited = set()

        def dfs(i):
            if i in visited:
                return False
            
            if i not in mapping:
                return True

            visited.add(i)
            for j in mapping[i]:
                if not dfs(j):
                    return False
            
            visited.remove(i)
            return True
        
        for i in mapping.keys():
            if not dfs(i):
                return False
        return True