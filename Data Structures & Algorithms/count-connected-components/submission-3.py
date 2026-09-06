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
        
        count = 0
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return 0
            visit.add(node)
            for nei in mapping[node]:
                if node == nei:
                    continue
                dfs(nei, node)
            return 1
        
        for i in mapping:
            count += dfs(i, -1)
        
        return count + len(set(range(n)) - visit)