class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum(gas) < sum(cost):    # Excluding impossible cases
        #     return -1
        # total = 0
        # res = 0
        # for i in range(len(gas)):
        #     total += gas[i] - cost[i]
        #     if total < 0:           # Not starting from case where cost more than gas
        #         total = 0
        #         res = i + 1
        # return res

        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:       # Dropping bad prefixes. resetting if total is zero
                res = i + 1
                total = 0
        return res
            

        