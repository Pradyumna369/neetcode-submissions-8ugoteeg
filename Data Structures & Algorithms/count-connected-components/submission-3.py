class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeNodes = defaultdict(list)
        visited = set()
        count = 0
        for n1, n2 in edges:
            edgeNodes[n1].append(n2)
            edgeNodes[n2].append(n1)
        def dfs(node):
            for each in edgeNodes[node]:
                if each not in visited:
                    visited.add(each)
                    dfs(each)
        for node in edgeNodes:
            if node not in visited:
                count += 1
                visited.add(node)
                dfs(node)
        return count + n - len(visited) # Adding nodes which are not part of any edges.
        