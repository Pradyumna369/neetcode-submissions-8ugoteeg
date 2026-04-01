class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        l = len(tasks)
        highest = max(list(c.values()))
        count = 0
        for val in list(c.values()):
            if highest == val:
                count += 1
        # Minimum no. of cycles needed for tasks with same highest frequency
        minimum = (highest - 1) * (n + 1) + count
        # If the no. of tasks is more than minimum, then the highest would be no.of tasks
        return max(minimum, l)
        