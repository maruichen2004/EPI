from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def isSymmetricTree(self, root):
      if root is None: return True
      return self.isMirror(root.left, root.right)

   def isMirror(self, p, q):
      if p is None and q is None:
         return True
      if p is None or q is None:
         return False
      if p.val != q.val:
         return False
      return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.isSymmetricTree(tree.getRoot())
