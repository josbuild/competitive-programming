class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        temp = dict()
        slow = 0
        ans = 0
        for fast in range(len(fruits)):
            curr_fruit = fruits[fast]
            temp[curr_fruit] = temp.get(curr_fruit, 0) + 1

            while len(temp) > 2:
                slow_fruit = fruits[slow]
                temp[slow_fruit] -= 1
                if temp[slow_fruit] == 0:
                    del temp[slow_fruit]
                slow += 1

            ans = max(ans, fast - slow + 1)
        return ans



        