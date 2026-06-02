class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0]*n
        if k == 0:
            return ans
        if k > 0:
            curr_sum = sum(code[1: 1 + k])
            ans[0] = curr_sum
            for i in range(1, n):
                curr_sum += code[(i + k) % n] - code[i]
                ans[i] = curr_sum
        if k < 0:
            curr_sum = sum(code[k:])
            ans[0] = curr_sum
            for i in range(1, n):
                curr_sum += code[i - 1] - code[i - 1 - abs(k)]
                ans[i] = curr_sum
        return ans
                

        