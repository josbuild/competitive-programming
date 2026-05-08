# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        should_move = count - n
        dummy = ListNode()
        slow = dummy
        fast = head
        while should_move > 0:
            slow.next = fast
            slow = slow.next
            fast = fast.next
            should_move -= 1
        slow.next = fast.next     
        return dummy.next

        