class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)  # reverse edges: pre → course

        visiting = set()  # for cycle detection
        visited = set()   # courses fully processed
        order = []        # topological order

        def dfs(course):
            if course in visiting:   # cycle detected
                return False
            if course in visited:    # already processed
                return True

            visiting.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []

        return order[::-1]  # reverse for correct order
