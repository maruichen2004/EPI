from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def LCANoParent(self, root, a, b):
      if root is None: return None
      if root == a or root == b: return root
      left = self.LCANoParent(root.left, a, b)
      right = self.LCANoParent(root.right, a, b)
      if left is not None and right is not None: return root
      return left if left is not None else right

if __name__ == "__main__":
   tree = BinaryTree()
   a = tree.getRoot().right.right
   b = tree.getRoot().right
   t = Solution()
   print t.LCANoParent(tree.getRoot(), a, b).val
