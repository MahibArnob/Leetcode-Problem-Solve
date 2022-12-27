# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(next=head)
        hare = tortoise = temp

        while hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next

        tortoise.next = tortoise.next.next
        return temp.next
