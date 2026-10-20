# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Notes #TC - 0(n) SC - 0(n)
        '''At any point, for a given node, we need to know the maximum Value above it and the number of good nodes it has seen till now
Good number of nodes we can increment by checking condition
Maximum value we need to pass as parameter in the function and update every time for the next child nodes'''
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

#You are correct; the given code is using recursion, not Depth-First Search (DFS) explicitly. However, it is essential to understand that recursion is often a fundamental technique used in various DFS implementations.

# DFS is a way to traverse a tree or graph data structure, where we explore as far as possible along each branch before backtracking. Recursion is a natural fit for DFS because it allows us to traverse a tree or graph by calling the same function repeatedly for its child nodes, exploring deeper and deeper until we reach the base case.

# In the code provided, `dfs` is indeed a recursive function that traverses the binary tree, and each recursive call explores deeper into the tree while updating the `maxVal` and `good` variables. It's a form of DFS, and you can consider this implementation as a type of DFS.

# So, although the code explicitly mentions a function named `dfs`, it is using recursion to traverse the binary tree in a depth-first manner, making it a DFS implementation.


#I TRIED THE BFS SOLUTION
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
        # q = collections.deque()
        # count = 0
        # q.append(root)
        # rootval = root.val

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.val >= rootval:
        #             count += 1
        #             rootval = node.val
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return count

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
