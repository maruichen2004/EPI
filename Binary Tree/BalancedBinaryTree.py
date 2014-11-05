from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def isBalanced(self, root):
      return self.getHeight(root) != -1

   def getHeight(self, root):
      if root is None: return 0
      left = self.getHeight(root.left)
      right = self.getHeight(root.right)
      if left == -1 or right == -1 or abs(left - right) > 1:
         return -1
      return max(left, right) + 1

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.isBalanced(tree.getRoot())
