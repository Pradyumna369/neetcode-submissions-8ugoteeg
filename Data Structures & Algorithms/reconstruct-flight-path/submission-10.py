class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse = True):
            graph[src].append(dest)
        route = []  # Exploring in a postorder traversal. Hierholzer's algorithm as every edge is used only once.
        def dfs(airport):   # Appending the dead end to the stack.
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)
        
        dfs("JFK")
        return route[::-1]