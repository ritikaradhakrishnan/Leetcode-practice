# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''At any point, for a given node, we need to know the maximum Value above it and the number of good nodes it has seen till now
-Good number of nodes we can increment by checking condition
-Maximum value we need to pass as parameter in the function and update every time for the next child nodes'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(root, maxVal):
            nonlocal good

            if not root:
                return
            
            if root.val >= maxVal:
                good += 1
            
            maxVal = max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)
        return good
            


        

        