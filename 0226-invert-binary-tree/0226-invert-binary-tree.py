# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return 
        tmp = root.left
        root.left = root.right
        root.right = tmp
        #root.left, root.right = root.right, root.left (python)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        




# #Python evaluates the entire right-hand side first before assigning anything to the left-hand side:
# Read phase: Python looks up the current objects pointed to by root.right and root.left and holds both references in memory.
# Write phase: Python unpacks those saved references and assigns them from left to right into root.left and root.right.


#The time complexity of the invertTree function is O(n), where n is the number of nodes in the binary tree. This is because the function visits each node once, and for each node, it performs a constant amount of work (swapping the left and right children). Therefore, the time complexity is linear with respect to the number of nodes.

# The space complexity of the invertTree function is O(h), where h is the height of the binary tree. This is because the function makes recursive calls to invert the left and right subtrees. The maximum depth of the recursive call stack corresponds to the height of the tree. In the worst case, where the tree is completely unbalanced and resembles a linked list, the height of the tree is n, resulting in O(n) space complexity. However, in a balanced binary tree, the height is logarithmic with respect to the number of nodes, resulting in O(log n) space complexity.

# It's worth noting that the space complexity also includes the space used by the implicit stack during the recursive calls. In the worst case, where the tree is completely unbalanced, the stack space usage is O(n). However, in a balanced binary tree, the stack space usage is O(log n).

#In the case of the invertTree function, the recursive calls to invert the left and right subtrees will result in multiple frames being added to the call stack. The depth of the call stack corresponds to the height of the binary tree. This is called the "implicit stack" because it is managed automatically by the programming language's runtime system.