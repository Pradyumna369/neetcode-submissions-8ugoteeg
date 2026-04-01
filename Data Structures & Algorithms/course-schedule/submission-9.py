class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)
        can = set() # All the courses which can be taken.
        seen = set()    # List of all prerequesites seen for the course, including it. 
        def canBeTaken(course):
            if course in can:   # If it has not prereqs or it is already checked to be taken, it can be taken.
                return True
            if course in seen:  # If there is a loop in courses, then that course cannot be taken.
                return False
            seen.add(course)
            for each in prereq[course]:
                if not canBeTaken(each):    # If a single prereq cant be taken, course cant be taken.
                    return False
            can.add(course) # If all the prereqs can be take, this course can be taken.
            return True
        for course in range(numCourses):
            if course not in seen:
                if not canBeTaken(course):
                    return False
            seen.clear()
        return True

            

        