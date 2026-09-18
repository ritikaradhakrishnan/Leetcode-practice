# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #hashset would have O(n) TC, flyod's cycle detetction/ turtle hare algorithm brings it to O(1)
        # If there is no loop, the hare will reach the end (null) of the list. If a cycle exists, the faster hare will loop around and meet the slower tortoise at some node inside the loop.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        