""" You are given the root of a binary tree. 
Return the deepest node (the furthest node from the root).

Example:
    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Fill this in.
    pass


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
