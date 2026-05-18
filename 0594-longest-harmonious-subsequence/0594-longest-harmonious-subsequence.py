class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
        ans = 0
        for item in freq_counter:
            if item - 1 in freq_counter:
                ans = max(ans, freq_counter[item] + freq_counter[item - 1])
            elif item + 1 in freq_counter:
                ans = max(ans, freq_counter[item] + freq_counter[item + 1])
            else:
                pass
        return ans
        