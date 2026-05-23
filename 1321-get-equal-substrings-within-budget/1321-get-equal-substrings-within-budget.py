class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        slow = 0
        ans = 0
        curr_cost = 0
        for fast in range(len(s)):
            curr_cost += abs(ord(s[fast]) - ord(t[fast]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[slow]) - ord(t[slow]))
                slow += 1
            ans = max(ans, fast - slow + 1)
        return ans
        