class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        level = 0
        queue = []
        queue.append(root)
        while len(queue) != 0:
            levels.append([])
            for i in range(len(queue)):
                current = queue.pop(0)
                levels[level].append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level += 1
        return levels