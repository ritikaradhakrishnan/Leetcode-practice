# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(left, root, right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            leftcase = dfs(left, root.left, root.val)
            rightcase = dfs(root.val,root.right, right)

            return leftcase and rightcase

        return dfs(float("-infinity"), root, float("infinity"))
        