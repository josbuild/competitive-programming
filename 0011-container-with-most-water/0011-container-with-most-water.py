class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = -float(inf)
        while left < right:
            curr_width = right - left
            curr_height = min(height[left], height[right])
            curr_area = curr_width * curr_height
            max_area = max(max_area, curr_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area