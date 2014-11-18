from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(h)
   def searchBSTForFirstOccurrence(self, root, k):
      if root is None: return None
      elif root.val == k:
         node = self.searchBSTForFirstOccurrence(root.left, k)
         return node if node is not None else root
      elif root.val < k:
         return self.searchBSTForFirstOccurrence(root.right, k)
      else:
         return self.searchBSTForFirstOccurrence(root.left, k)

   # Time: O(h)
   # Space: O(1)
   def searchBSTForFirstOccurrenceIterative(self, root, k):
      cur, res = root, None
      while cur:
         if cur.val == k:
            res = cur
            cur = cur.left
         elif cur.val < k:
            cur = cur.right
         else:
            cur = cur.left
      return res

if __name__ == "__main__":
   tree = BinaryTree()
   k = 2
   t = Solution()
   print t.searchBSTForFirstOccurrence(tree.getRoot(), k).val
