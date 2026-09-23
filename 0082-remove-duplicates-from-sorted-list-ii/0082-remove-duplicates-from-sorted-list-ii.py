# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp and temp.next:

            if temp.val == temp.next.val:

                value = temp.val

                while temp and temp.val == value:
                    temp = temp.next

                prev.next = temp

            else:
                prev = temp
                temp = temp.next

        return dummy.next