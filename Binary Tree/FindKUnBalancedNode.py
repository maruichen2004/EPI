from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def findKUnBalancedNode(self, root, k):
      return self.findKUnBalancedNodeHelper(root, k)[0]

   def findKUnBalancedNodeHelper(self, root, k):
      if root is None: return (None, 0)
      left = self.findKUnBalancedNodeHelper(root.left, k)
      if left[0] is not None: return left
      right = self.findKUnBalancedNodeHelper(root.right, k)
      if right[0] is not None: return right
      sum = left[1] + right[1] + 1
      if abs(left[1] - right[1]) == k: return (root, sum)
      return (None, sum)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.findKUnBalancedNode(tree.getRoot(), 1).val
