### First way of implementation iteratively ###
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

### First way of implementation recursively ###

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev
            return tail
        
        return rec(None, head)