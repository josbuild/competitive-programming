class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = {}
        for i in range(len(heights)):
            temp[heights[i]] = i
        sorted_heights = sorted(temp.keys(), reverse = True)
        ans = []
        for height in sorted_heights:
            ans.append(names[temp[height]])
        return ans


        