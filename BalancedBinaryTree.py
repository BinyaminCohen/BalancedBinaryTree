# Given a binary tree, determine if it is height-balanced

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isBalanced(root):
    """
    Check if a binary tree is height-balanced.

    :param root: TreeNode, the root of the binary tree
    :return: True if the tree is height-balanced, False otherwise
    """

    def checkHeight(node):
        """
        Recursively check the height of the tree and if it is balanced.

        :param node: TreeNode, the current node
        :return: The height of the current subtree, or -1 if it is unbalanced
        """
        if not node:
            return 0  # Base case: An empty tree is height-balanced

        left_height = checkHeight(node.left)
        if left_height == -1:
            return -1  # Left subtree is not balanced

        right_height = checkHeight(node.right)
        if right_height == -1:
            return -1  # Right subtree is not balanced

        # Check if the current node is balanced
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced

        # Return the height of the subtree rooted at the current node
        return max(left_height, right_height) + 1

    return checkHeight(root) != -1


# Constructing the tree from the example
#       3
#      / \
#     9  20
#       /  \
#      15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Check if the tree is height-balanced
print(isBalanced(root))  # Output: True

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(3)), TreeNode(3, TreeNode(4), TreeNode(4)))
root.right = TreeNode(2)

print(isBalanced(root))  # Output: False

root = None  # Input: root = []
print(isBalanced(root))  # Output: True
