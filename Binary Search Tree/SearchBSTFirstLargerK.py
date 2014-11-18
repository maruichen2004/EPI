from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(1)
   def searchBSTFirstLargerK(self, root, k):
      cur, res, found = root, None, False
      while cur:
         if cur.val == k:
            found = True
            cur = cur.right
         elif cur.val < k:
            cur = cur.right
         else:
            res = cur
            cur = cur.left
      return res if found else None

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   k = 2
   print t.searchBSTFirstLargerK(tree.getRoot(), k).val
