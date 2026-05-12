class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 3,2,2,1 => 2
        people.sort(reverse=True)
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
        return left


            


                



        