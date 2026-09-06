class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites[i] = [a, b] = must take b to take a

        # Create adjacency list {a: [b, b, b]}
        cache = {}
        for prereq in prerequisites:
            if prereq[0] not in cache:
                cache[prereq[0]] = []
            cache[prereq[0]].append(prereq[1])
        
        visited = set()

        def dfs(next_course):
            if next_course in visited:
                return False
            if next_course not in cache:
                return True
            visited.add(next_course)
            for course in cache[next_course]:
                if not dfs(course):
                    return False
            visited.remove(next_course)
            cache[next_course] = []
            return True

        for course in cache:
            if not dfs(course):
                return False
        return True