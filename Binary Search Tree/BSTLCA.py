from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(1)
   def BSTLCA(self, root, a, b):
      cur = root
      while cur.val < a.val or cur.val > b.val:
         while cur.val < a.val: cur = cur.right
         while cur.val > b.val: cur = cur.left
      return cur

if __name__ == "__main__":
   tree = BinaryTree()
   a = tree.getRoot().left.right
   b = tree.getRoot().left.left.right
   t = Solution()
   print a.val, b.val
   print t.BSTLCA(tree.getRoot(), b, a).val
