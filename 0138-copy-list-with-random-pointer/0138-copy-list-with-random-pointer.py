"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict = {None:None}
        cur = head      
        while cur:
            dict[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new = dict[cur]
            new.next = dict[cur.next]
            new.random = dict[cur.random]
            cur = cur.next
        return dict[head]


        