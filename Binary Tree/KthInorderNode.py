from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(h)
   def kthInorderNode(self, root, k):
      cur = root
      while cur:
         l = cur.left.size if cur.left is not None else 0
         if l < k - 1:
            return self.kthInorderNode(root.right, k - l - 1)
         elif l == k - 1:
            return root
         else:
            return self.kthInorderNode(root.left, k)
      return None

if __name__ == "__main__":
   tree = BinaryTree()
   k = 7
   t = Solution()
   print t.kthInorderNode(tree.getRoot(), k).val
