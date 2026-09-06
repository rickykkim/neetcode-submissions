class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        rem = []

        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            adj[a].append(b)
            adj[b].append(a)

            for node in adj:
                if node in visit:
                    continue
                if not dfs(node, -1):
                    rem.append(i)
                    adj[a] = adj[a][:-1]
                    adj[b] = adj[b][:-1]
                    break
            
            visit = set()
        
        return edges[rem[-1]]