class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        1 <= triplets.length <= 1000
        1 <= ai, bi, ci, x, y, z <= 100
        triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]], target = [5, 4, 6]
        i, j -> max(i[0]) <= target[0]
                max(i[1]) <= target[1]
                max(i[2]) <= target[2]
        possible = []
        '''
        x, y, z = 1, 1, 1
        tx, ty, tz = target
        for index, triplet in enumerate(triplets):
            if triplet[0] <= tx and triplet[1] <= ty and triplet[2] <= tz:
                x, y, z = max(x, triplet[0]), max(y, triplet[1]), max(z, triplet[2])
        if x == tx and y == ty and z == tz:
            return True
        else: 
            return False


