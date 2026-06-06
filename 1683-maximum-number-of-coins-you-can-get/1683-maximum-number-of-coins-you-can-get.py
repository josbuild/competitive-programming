class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 1
        mid = right - 1
        ans = 0
        while left < mid:
            ans += piles[mid]
            right -= 2
            mid -= 2
            left += 1
        return ans

        