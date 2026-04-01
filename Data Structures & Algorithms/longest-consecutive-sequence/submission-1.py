class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numbers = set()
        # for num in nums:
        #     numbers.add(num)
        numbers = set(nums)
        longest = 0
        for number in numbers:
            length = 1
            while number + 1 in numbers:
                length += 1
                number += 1
            longest = max(longest, length)
        return longest