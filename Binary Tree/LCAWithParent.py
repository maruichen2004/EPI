from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(h)
   # Space: O(1)
   def LCAWithParent(self, a, b):
      p, lena, q, lenb = a, 1, b, 1
      while p.parent != None:
         p = p.parent
         lena += 1
      while q.parent != None:
         q = q.parent
         lenb += 1
      p, q = a, b
      if lena < lenb:
         for i in range(lenb - lena): q = q.parent
      else:
         for i in range(lena - lenb): p = p.parent
      while p != q:
         p, q = p.parent, q.parent
      return p

if __name__ == "__main__":
   tree = BinaryTree()
   a = tree.getRoot().left.left.left
   b = tree.getRoot().left.left
   t = Solution()
   print t.LCAWithParent(a, b).val
