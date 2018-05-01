"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def pre_order(root):
    # Write your code here
    node = root
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data, end=" ")
        else:
            print(node.data, end=" ")
            pre_order(node.left)
            pre_order(node.right)
