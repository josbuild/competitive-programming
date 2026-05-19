class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        curr_sum = 0
        ans = []
        for fast in range(len(nums)):
            curr_sum += nums[fast]
            while curr_sum >= target:
                ans.append(fast - slow + 1)
                curr_sum -= nums[slow]
                slow += 1
        return min(ans) if ans else 0
        