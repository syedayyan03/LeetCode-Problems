# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:

            first = curr
            second = curr.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            curr = first.next

        return dummy.next
        