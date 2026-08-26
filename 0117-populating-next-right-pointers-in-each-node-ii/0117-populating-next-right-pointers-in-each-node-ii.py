"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes = []

        def level(node, height):
            if not node:
                return
            
            if height == len(nodes):
                nodes.append([node])
            else:
                nodes[height][-1].next = node
                nodes[height].append(node)
            
            level(node.left, height + 1)
            level(node.right, height + 1)

        level(root, 0)
        return root