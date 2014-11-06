from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(1)
   def inorderSuccessor(self, node):
      res = node
      if node.right is not None:
         res = res.right
         while res.left is not None:
            res = res.left
         return res
      while res.parent is not None and res.parent.right == res:
         res = res.parent
      return res.parent

if __name__ == "__main__":
   tree = BinaryTree()
   node = tree.getRoot().left.right
   t = Solution()
   print t.inorderSuccessor(node).val
