# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

"""
Inorder gives 2 gives 1, 2, 3 on traversal, so lets use that
            /  \
            1   3
"""
#Recursive DFS

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # #Do we need a helper function? 
        result = []
        cur = root
        while cur or result:
            while cur:
                result.append(cur)
                cur = cur.left 
            #Once this above loop ends, we will reach the smallest elem in the tree, pop it
            cur = result.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

#Iterative BFS :  BFS approach more optimized where k is relatively small
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k-=1
            if k==0:
                return cur.val
            cur = cur.right
            