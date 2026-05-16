class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = dict()
        for i in range(len(nums)):
            curr_ch = nums[i]
            if curr_ch not in temp:
                temp[curr_ch] = i
            else:
                if temp[curr_ch] != i and abs(temp[curr_ch] - i) <= k:
                    return True
                else:
                    temp[curr_ch] = i
        return False

        