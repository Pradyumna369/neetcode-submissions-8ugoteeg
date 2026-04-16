class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        0 <= m <= 1000
        0 <= n <= 1000
        -10^6 <= nums1[i], nums2[i] <= 10^6
        nums1  = [1, 3, 5]
                  ^        
        nums2 = [2, 4, 5, 6]
                          ^
        len(nums) = m + n
        if m + n % 2 == 0:
            nums[(m + n) // 2 - 1] + nums[(m + n) // 2] / 2
        else:
            return nums[(m + n) // 2]
                 
        nums = [1, 3, 5, 2, 4, 5, 6]
                     4  |         
                        ^ x ^
                ^ y  ^
        x + y = nums[(m + n) // 2]
        x = m + 
        O(log(m + n))
        '''
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        # apprx index of the median in the merged arrays
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            # last element of A in left half
            Aleft = A[i] if i >= 0 else float("-inf")
            # first element of A in right half
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            # last element of B in left half
            Bleft = B[j] if j >= 0 else float("-inf")
            # first element of B in right half
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Aright >= Bleft:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # more numbers in left
            elif Aleft > Bright:
                r = i - 1
            # less numbers in left
            else:
                l = i + 1






