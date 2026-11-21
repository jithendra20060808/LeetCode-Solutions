# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        stack = []
        while temp:
            stack.append(temp)
            temp = temp.next
        n = len(stack)
        curr = head
        for i in range(n//2):
            last = stack.pop()
            nxt = curr.next

            curr.next = last
            last.next = nxt
            curr = nxt
        curr.next = None