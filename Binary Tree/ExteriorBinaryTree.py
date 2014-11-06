from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def exteriorBinaryTree(self, root):
      if root:
         res = [root.val]
         self.traversalLeftBoundary(root.left, res, True)
         self.traversalRightBoundary(root.right, res, True)
         return res

   def traversalLeftBoundary(self, root, res, isBoundary):
      if root:
         if isBoundary or (root.left is None and root.right is None):
            res.append(root.val)
         self.traversalLeftBoundary(root.left, res, isBoundary)
         self.traversalLeftBoundary(root.right, res, isBoundary and root.left is None)

   def traversalRightBoundary(self, root, res, isBoundary):
      if root:
         self.traversalRightBoundary(root.left, res, isBoundary and root.right is None)
         self.traversalRightBoundary(root.right, res, isBoundary)
         if isBoundary or (root.left is None and root.right is None):
            res.append(root.val)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.exteriorBinaryTree(tree.getRoot())
