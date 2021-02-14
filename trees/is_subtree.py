class Solution:
    # confusingly, s = tree and t = subtree
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return True
        if s is None:
            return False
        if (self.areSame(s, t)):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def areSame(self, sroot: TreeNode, troot: TreeNode) -> bool:
        if not sroot and not troot:
            return True
        if not sroot or not troot:
            return False
        return (sroot.val == troot.val and 
            self.areSame(sroot.left , troot.left) and
            self.areSame(sroot.right, troot.right))