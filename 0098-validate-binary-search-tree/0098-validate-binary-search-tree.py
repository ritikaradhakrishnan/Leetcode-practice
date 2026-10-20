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
            '''example [2,1,3]:
             -inf < 2 < inf -> 
             now on left when 1 in middle (root.left)
             -inf < 1 < 2
             meaning: 1 can be as small as possible as long as its less than 2
            '''
            rightcase = dfs(root.val,root.right, right)
            '''example [2,1,3]:
             -inf < 2 < inf -> 
             now on right when 3 in middle (root.right)
             2 < 3 < inf
             meaning: 3 can be as big as possible as long as its more than 2
            '''

            return leftcase and rightcase

        return dfs(float("-infinity"), root, float("infinity"))
        