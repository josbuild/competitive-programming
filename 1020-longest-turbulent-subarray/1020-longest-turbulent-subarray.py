class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        slow = 0
        mid = 1
        ans = 1

        if arr[0] < arr[1]:
            status = 'INC'
            ans = 2
        elif arr[0] > arr[1]:
            status = 'DEC'
            ans = 2
        else:
            status = 'SKIP'

        for fast in range(2, len(arr)):
            temp = status

            if arr[mid] < arr[fast]:
                status = 'INC'
            elif arr[mid] > arr[fast]:
                status = 'DEC'
            else:
                status = 'SKIP'

            if status == 'SKIP':
                slow = fast
            elif temp == 'SKIP':
                slow = mid
            elif status == temp:
                slow = mid

            ans = max(ans, fast - slow + 1)
            mid += 1

        return ans