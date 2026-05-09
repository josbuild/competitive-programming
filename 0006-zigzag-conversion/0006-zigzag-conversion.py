class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        row_index, dirc = 0, 1
        for ch in s:
            rows[row_index].append(ch)
            if row_index == 0:
                d = 1
            elif row_index == numRows - 1:
                d = -1
            row_index += d
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)

        