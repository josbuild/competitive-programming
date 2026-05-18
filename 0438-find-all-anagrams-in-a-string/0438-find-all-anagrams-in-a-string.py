class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_counter = Counter(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i: i + len(p)]) == freq_counter:
                ans.append(i)
        return ans
        