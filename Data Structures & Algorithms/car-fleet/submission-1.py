class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x:x[0])     
        zipped.reverse()    # Sorting based on distance from target, as the cars cant 
                            # pass the cars before them. So calculating from cars which are 
                            # nearest to the target
        stack = []
        stack.append(0)
        for car in zipped:
            distance = target - car[0]
            time = distance / car[1]
            if time > stack[-1]:    # If the next car can reach in less time than target, 
                                    # it should merge with the previous fleet. If the time is more
                                    # then it comes as next fleet
                stack.append(time)
        return len(stack) - 1