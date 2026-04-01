class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeSet = set()
        edgeNodes = defaultdict(list)
        visited = set()
        count = 0
        for n1, n2 in edges:
            edgeSet.add((n1, n2))
            edgeNodes[n1].append(n2)
            edgeNodes[n2].append(n1)
        def dfs(node):
            for each in edgeNodes[node]:
                if each not in visited:
                    visited.add(each)
                    dfs(each)
                

        for each in edgeNodes:
            if each not in visited:
                count += 1
                if count > 1:
                    return False
                visited.add(each)
                dfs(each)


        if len(edgeSet) == n - 1:
            return True
        else:
            return False
        