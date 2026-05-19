class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = dict()
        slow, fast = 0, 0
        ans = 0
        while fast < len(s):
            if s[fast] in temp and temp[s[fast]] >= slow:
                slow = temp[s[fast]] + 1
            temp[s[fast]] = fast
            ans = max(ans, fast - slow + 1)
            fast += 1
        return ans



        