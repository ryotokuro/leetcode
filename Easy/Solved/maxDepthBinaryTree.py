# link

# PROBLEM
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.

# EXAMPLE
# Given binary tree [3,9,20,null,null,15,7],
# The tree is as follows:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# So the solution is return depth = 3


# Definition of a binary tree node
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            lheight = Solution.maxDepth(self, root.left)
            rheight = Solution.maxDepth(self, root.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1


# Create Tree
tree = TreeNode()

# Testing Solution
s = Solution()
s.maxDepth()
