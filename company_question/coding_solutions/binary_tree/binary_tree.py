
from typing import Optional


# Binary Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional["TreeNode"] = left
        self.right: Optional["TreeNode"] = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Base condition: empty node has depth 0
        if root is None:
            return 0

        # Calculate left subtree depth
        left_depth = self.maxDepth(root.left)

        # Calculate right subtree depth
        right_depth = self.maxDepth(root.right)

        # Return maximum depth + 1 for current node
        return 1 + max(left_depth, right_depth)


# Create binary tree
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Create Solution object
solution = Solution()

# Find maximum depth
result = solution.maxDepth(root)

# Print result
print("Maximum Depth:", result)