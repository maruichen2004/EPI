from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(|dr - dt|)
   # Space: O(|dr - dt|)
   def testBSTTotallyOrdered(self, r, s, m):
      cur_r, cur_s = r, s
      while cur_r and cur_r != s and cur_r != m and cur_s and cur_s != r and cur_s != m:
         cur_r = cur_r.left if cur_r.val > m.val else cur_r.right
         cur_s = cur_s.left if cur_s.val > m.val else cur_s.right
      if cur_r == s or cur_s == r or (cur_r != m and cur_s != m): return False
      return self.searchTarget(cur_r, s, m) or self.searchTarget(cur_s, r, m)


   def searchTarget(self, p, t, m):
      while p and p != t and p != m:
         p = p.left if p.val > t.val else p.right
      return p == m

if __name__ == "__main__":
   tree = BinaryTree()
   r = tree.getRoot()
   s = tree.getRoot().right.right
   m = tree.getRoot().right.left
   t = Solution()
   print t.testBSTTotallyOrdered(r, s, m)
