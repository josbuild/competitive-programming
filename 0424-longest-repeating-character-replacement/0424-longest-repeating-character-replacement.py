class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = dict()
        slow = 0
        ans = 0
        for fast in range(len(s)):
            temp[s[fast]] = temp.get(s[fast], 0) + 1
            max_freq = max(temp.values())
            curr_len = fast - slow + 1
            if curr_len - max_freq > k:
                temp[s[slow]] -= 1
                slow += 1
            ans = max(ans, fast - slow + 1)
        return ans
        