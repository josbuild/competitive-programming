class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        mid = len(piles) - 2
        ans = 0
        while left < mid:
            ans += piles[mid]
            mid -= 2
            left += 1
        return ans

        