class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = {}
        for edge in edges:
            if edge[0] not in mapping:
                mapping[edge[0]] = []
            if edge[1] not in mapping:
                mapping[edge[1]] = []
            
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])
        
        curr = set()
        visited = set()
        count = 0
        
        def dfs(i, prev):
            if i in curr:
                return

            curr.add(i)

            for j in mapping[i]:
                if j != prev:
                    dfs(j, i)
            
        
        for i in mapping.keys():
            if i not in visited:
                dfs(i, -1)
                original = len(visited)
                for node in curr:
                    visited.add(node)
                if len(visited) > original:
                    count += 1
        
        return count + (n - len(visited))