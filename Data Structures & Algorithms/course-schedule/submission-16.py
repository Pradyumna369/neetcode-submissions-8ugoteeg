class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)
        cycle = set() # All the courses which can be taken.
        def canBecycle(course):
            if prereq[course] == []:   # If it has not prereqs or it is already checked to be cycle, it can be cycle.
                return True
            if course in cycle:  # If there is a loop in courses, then that course cannot be cycle.
                return False
            cycle.add(course)
            for each in prereq[course]:
                if not canBecycle(each):    # If a single prereq cant be cycle, course cant be cycle.
                    return False
            prereq[course] = []
            cycle.remove(course)
            return True
        for course in range(numCourses):
            if not canBecycle(course):
                return False
        return True

            

        