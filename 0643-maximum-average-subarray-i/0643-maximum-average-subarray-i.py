class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -float(inf)
        curr_sum = sum(nums[:k])
        ans = max(ans, curr_sum/k)
        for i in range(1, len(nums) - k + 1):
            curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
            ans = max(ans, curr_sum/k)
        return ans
        

        