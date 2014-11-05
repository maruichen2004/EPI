from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time:
   # Space:
   def sumRootToLeafNumber(self, root):
      return self.sumRootToLeafNumberHelper(root, 0)

   def sumRootToLeafNumberHelper(self, root, sum):
      if root is None: return 0
      res = (sum * 10) + root.val
      if root.left is None and root.right is None:
         return res
      return self.sumRootToLeafNumberHelper(root.left, res) + self.sumRootToLeafNumberHelper(root.right, res)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.sumRootToLeafNumber(tree.getRoot())
