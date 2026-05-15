class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        temp = defaultdict()
        for i in range(len(s)):
            temp[s[i]] = i
        ans = []
        max_index = temp[s[0]]
        slow = 0
        for fast in range(len(s)):
            max_index = max(max_index, temp[s[fast]])
            if max_index == fast:
                ans.append(fast - slow + 1)
                slow = fast + 1
        return ans

        