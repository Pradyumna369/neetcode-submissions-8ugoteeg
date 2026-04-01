class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if not nums:
        #     return False
        # count = Counter(nums)
        # return True if max(count.values()) > 1 else False

        return len(set(nums)) < len(nums)