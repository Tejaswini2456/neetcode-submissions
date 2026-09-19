# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:

            # Find the kth node
            kth = groupPrev

            for i in range(k):
                if not kth:
                    break
                kth = kth.next

            # Not enough nodes
            if not kth:
                break

            # Save the node after the group
            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part to reversed group
            temp = groupPrev.next
            groupPrev.next = prev

            # Move groupPrev to the end of reversed group
            groupPrev = temp

        return dummy.next