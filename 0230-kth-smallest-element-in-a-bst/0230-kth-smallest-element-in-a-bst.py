# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#inorder traversal of a BST always sort the array
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        #inorder for bst gives the correct ascending order
        curr = root
        n = 0
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
            



        
        