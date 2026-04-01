class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        l = len(tasks)
        highest = max(list(c.values()))
        count = 0
        for val in list(c.values()):
            if highest == val:
                count += 1
        minimum = (highest - 1) * (n + 1) + count
        return max(minimum, l)
        