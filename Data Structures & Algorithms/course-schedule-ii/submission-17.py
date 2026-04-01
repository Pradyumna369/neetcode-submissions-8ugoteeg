class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        exitTime = []
        preReq = defaultdict(list)
        taken = set()
        cycle = set()   # List of all prerequesites cycle for the course, including it.
        for course, pre in prerequisites:
            preReq[course].append(pre)
        def canBeTaken(course):
            if course in taken:
                return True
            if course in cycle:  # Loop detected
                return False
            cycle.add(course)    
            for each in preReq[course]:
                if not canBeTaken(each):    # If a single prerequisite cant be taken, course cant be taken.
                    return False
            cycle.remove(course)
            taken.add(course)
            exitTime.append(course) # Exiting after all the prerequisites are taken.
            return True
        
        for course in range(numCourses):
            if not canBeTaken(course):
                return []
        return exitTime