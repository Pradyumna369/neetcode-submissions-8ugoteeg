class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)
        can = set()
        seen = set()
        def canBeTaken(course):
            if len(prereq[course]) == 0 or course in can:
                return True
            if course in seen:
                return False
            seen.add(course)
            for each in prereq[course]:
                if not canBeTaken(each):
                    return False
            can.add(course)
            return True
        for course in range(numCourses):
            if not canBeTaken(course):
                return False
            seen.clear()
        return True

            

        