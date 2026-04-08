class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        c = Counter(hand)
        for num in c:
            if c[num] > 0:
                count = c[num]
                c[num] -= count
                cur = num
                for _ in range(groupSize - 1):
                    if cur + 1 in c:
                        c[cur + 1] -= count
                    else:
                        return False
                    cur += 1
        values = c.values()
        for val in values:
            if val != 0:
                return False
        return True       