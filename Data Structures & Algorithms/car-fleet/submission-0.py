class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x:x[0])
        zipped.reverse()
        stack = []
        stack.append(0)
        for car in zipped:
            distance = target - car[0]
            time = distance / car[1]
            if time > stack[-1]:
                stack.append(time)
        return len(stack) - 1