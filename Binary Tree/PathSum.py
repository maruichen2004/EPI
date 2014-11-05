from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(1)
   def hasPathSum(self, root, sum):
      if root is None: return False
      if root.left is None and root.right is None:
         return sum == root.val
      return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

   # Time: O(n)
   # Space: O(h)
   def getPathSum(self, root, sum):
      res = []
      self.getPathSumHelper(root, sum, res, [])
      return res

   def getPathSumHelper(self, root, sum, res, cur):
      if root is None: return
      if root.left is None and root.right is None:
         if sum == root.val:
            res.append(cur + [root.val])
      self.getPathSumHelper(root.left, sum - root.val, res, cur + [root.val])
      self.getPathSumHelper(root.right, sum - root.val, res, cur + [root.val])

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   sum = 15
   print t.hasPathSum(tree.getRoot(), sum)
   print t.getPathSum(tree.getRoot(), sum)
