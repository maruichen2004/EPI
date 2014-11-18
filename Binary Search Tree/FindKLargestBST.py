from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def findKLargestBST(self, root, k):
      res = []
      self.findKLargestBSTHelper(root, k, res)
      return res

   def findKLargestBSTHelper(self, root, k, res):
      if root and len(res) < k:
         self.findKLargestBSTHelper(root.right, k, res)
         if len(res) < k:
            res.append(root.val)
            self.findKLargestBSTHelper(root.left, k, res)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   k = 5
   print t.findKLargestBST(tree.getRoot(), k)
