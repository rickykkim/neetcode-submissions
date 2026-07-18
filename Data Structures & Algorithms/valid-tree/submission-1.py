class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        mapping = {}
        for edge in edges:
            if edge[0] not in mapping:
                mapping[edge[0]] = []
            if edge[1] not in mapping:
                mapping[edge[1]] = []
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in mapping[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n