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
                if count > 1:   # If all nodes are not part of same tree, it is not a valid tree.
                    return False
                visited.add(each)
                dfs(each)


        if len(edgeSet) == n - 1:   # if no.of edges == no.of nodes - 1 in undirected graph, it is a tree
            return True
        else:   # Else it is not a tree
            return False
        