from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree
import sys

class Solution:
   # Time: O(n)
   # Space: O(h)
   def isBST(self, root):
      inf = sys.maxint
      return self.isBSTHelper(-inf, root, inf)

   def isBSTHelper(self, MIN, root, MAX):
      if root is None: return True
      if MIN > root.val or root.val > MAX: return False
      return self.isBSTHelper(MIN, root.left, root.val) and self.isBSTHelper(root.val, root.right, MAX)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.isBST(tree.getRoot())
