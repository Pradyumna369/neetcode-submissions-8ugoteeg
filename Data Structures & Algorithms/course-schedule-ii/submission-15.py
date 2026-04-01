class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        exitTime = []
        preReq = defaultdict(list)
        can = set()
        cycle = set()
        for course, pre in prerequisites:
            preReq[course].append(pre)
        def canBeTaken(course):
            if course in can:
                return True
            if course in cycle:  # Loop detected
                return False
            cycle.add(course)    
            for each in preReq[course]:
                if not canBeTaken(each):
                    return False
            cycle.remove(course)
            can.add(course)
            exitTime.append(course)
            return True
        
        for course in range(numCourses):
            if not canBeTaken(course):
                return []
        return exitTime