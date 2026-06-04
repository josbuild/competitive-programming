class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = {}
        for num in arr1:
            temp[num] = temp.get(num, 0) + 1
        ans = []
        for num in arr2:
            ans.extend([num] * temp[num])
            del temp[num]
        for num in sorted(temp.keys()):
            ans.extend([num] * temp[num])
        return ans
        