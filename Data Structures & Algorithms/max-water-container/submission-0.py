class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVolume = 0
        while left < right:
            leftH = heights[left]
            rightH = heights[right]
            volume = (right - left) * min(leftH, rightH)
            maxVolume = max(volume, maxVolume)
            if leftH <= rightH:
                left += 1
            else:
                right -= 1
        return maxVolume