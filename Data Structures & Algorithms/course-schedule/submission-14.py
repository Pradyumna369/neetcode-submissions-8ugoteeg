class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)
        can = set() # All the courses which can be taken.
        cycle = set()    # List of all prerequesites cycle for the course, including it. 
        def canBecycle(course):
            if course in can:   # If it has not prereqs or it is already checked to be cycle, it can be cycle.
                return True
            if course in cycle:  # If there is a loop in courses, then that course cannot be cycle.
                return False
            cycle.add(course)
            for each in prereq[course]:
                if not canBecycle(each):    # If a single prereq cant be cycle, course cant be cycle.
                    return False
            can.add(course) # If all the prereqs can be taken, this course can be taken.
            cycle.remove(course)
            return True
        for course in range(numCourses):
            if not canBecycle(course):
                return False
        return True

            

        