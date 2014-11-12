from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(max(da, db) - dl)
   # Space: O(max(da, db) - dl)
   def LCAHash(self, a, b):
      i, j, map = a, b, []
      while i or j:
         if i:
            if i in map: return i
            map.append(i)
            i = i.parent
         if j:
            if j in map: return j
            map.append(j)
            j = j.parent
      return None

if __name__ == "__main__":
   tree = BinaryTree()
   n1, n2 = tree.getRoot().left.left.left, tree.getRoot().left.right
   t = Solution()
   print t.LCAHash(n1, n2).val
