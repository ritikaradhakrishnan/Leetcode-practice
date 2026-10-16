# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal diameter
            left = dfs(root.left)
            right = dfs(root.right)
            #1. one thing to maintain -> largest diameter at any point(starting from root will not be necessarily the largest diameter)
            diameter = max(diameter, left+right)
            #2. second -> max height of left or right to pass on to parent to peform step 1.
            return 1 + max(left, right)
        dfs(root)
        return diameter

        