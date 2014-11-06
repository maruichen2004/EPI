from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(m) m is the number of leaves
   # Space: O(h)
   def connectLeaves(self, root):
      res = []
      self.connectLeavesHelper(root, res)
      return res

   def connectLeavesHelper(self, root, res):
      if root is None: return
      if root.left is None and root.right is None:
         res.append(root.val)
      self.connectLeavesHelper(root.left, res)
      self.connectLeavesHelper(root.right, res)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.connectLeaves(tree.getRoot())
