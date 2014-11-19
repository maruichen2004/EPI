from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h + m)
   # Space: O(h + m)
   def rangeQueryOnBST(self, root, L, U):
      res = []
      p = self.findFirstLargerEqualK(root, L)
      while p and p.val <= U:
         res.append(p.val)
         p = self.findSuccessorBST(p)
      return res

   def findFirstLargerEqualK(self, root, k):
      if root is None: return None
      elif root.val >= k:
         node = self.findFirstLargerEqualK(root.left, k)
         return node if node else root
      else:
         return self.findFirstLargerEqualK(root.right, k)

   def findSuccessorBST(self, root):
      if root.right:
         p = root.right
         while p.left: p = p.left
         return p
      while root.parent and root.parent.right == root:
         root = root.parent
      return root.parent

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   L, U = 4, 9
   print t.rangeQueryOnBST(tree.getRoot(), L, U)
