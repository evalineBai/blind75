class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeRecursively(self, root: TreeNode) -> TreeNode:
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            
            self.invertTreeRecursively(root.left)
            self.invertTreeRecursively(root.right)
        return root
    
    def invertTreeIteratively(self, root: TreeNode) -> TreeNode:
        if root:
            queue = []
            queue.append(root)
            while queue != []:
                current = queue.pop(-1)
                temp = current.left
                current.left = current.right
                current.right = temp

                if current.left not None:
                   queue.append(current.left)
                if current.right not None:
                    queue.append(current.right)
        return root