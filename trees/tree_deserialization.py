class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserial(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserial(root.left, string)
                string = rserial(root.right, string)
            return string
        return rserial(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserial(node_list):
            if node_list[0] == 'None':
                node_list.pop(0)
                return None
            root = TreeNode(node_list[0])
            node_list.pop(0)
            root.left = rdeserial(node_list)
            root.right = rdeserial(node_list)
            return root
        data_list = data.split(',')
        root = rdeserial(data_list)
        return root