class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pt = 0
        right_pt = len(numbers) - 1
        while left_pt <= right_pt:
            curr_sum = numbers[left_pt] + numbers[right_pt]
            if curr_sum == target:
                return [left_pt + 1,right_pt + 1]
            elif curr_sum > target:
                right_pt -= 1
            else:
                left_pt += 1
        