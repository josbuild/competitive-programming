class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = isqrt(c)
        while left <= right:
            curr = left**2 + right**2
            if curr == c:
                return True
            elif curr < c:
                left += 1
            else:
                right -= 1
        return False
        