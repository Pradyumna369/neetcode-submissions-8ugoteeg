class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        exitTime = []
        preReq = defaultdict(list)
        can = set()
        seen = set()
        for course, pre in prerequisites:
            preReq[course].append(pre)
        def canBeTaken(course):
            if len(preReq[course]) == 0 or course in can:
                can.add(course)
                if course not in exitTime:
                    exitTime.append(course)
                return True
            if course in seen:
                return False
            seen.add(course)
            for each in preReq[course]:
                if not canBeTaken(each):
                    return False
            can.add(course)
            exitTime.append(course)
            return True
        
        for course in range(numCourses):
            if course not in seen:
                if not canBeTaken(course):
                    return []
        return exitTime