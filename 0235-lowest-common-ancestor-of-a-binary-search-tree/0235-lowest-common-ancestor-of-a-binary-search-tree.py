# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # #Notes #SC: O(log n), TC: O(1)
#         # curr = root
#         # while curr: #we are guaranteed to find p and q
#         #     if curr.val<p.val and curr.val<q.val:
#         #         curr = curr.right
#         #     elif curr.val>p.val and curr.val>q.val:
#         #         curr = curr.left
#         #     else: #p<curr<q or q<curr<p 
#         #         return curr

#         # #No need to return false as p and q are guaranteed to be present
#         curr = root
#         if curr.val>p.val and curr.val>q.val:
#             curr = curr.left
#         if curr.val<p.val and curr.val<q.val:
#             curr = curr.right
#         else:
#             return curr
        

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr.val<p.val and curr.val<q.val:
                curr = curr.right
            elif curr.val>p.val and curr.val>q.val:
                curr = curr.left
            else:
                return curr

