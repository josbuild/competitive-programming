class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dict_temp = {}
        curr_idx = 0
        curr_min = temp[0]
        for i in range(len(temp)):
            curr = temp[i]
            if curr != curr_min:
                curr_idx = i
                curr_min = curr
            dict_temp[curr] = curr_idx
        ans = []
        for num in nums:
            ans.append(dict_temp[num])
        return ans
        