from Util.BST import TreeNode
from Util.BST import BST

class Solution:
   # Time: O(n)
   # Space: O(h)
   def bstSortedOrder(self, node):
      stack, cur, res = [], node, []
      if node is None: return []
      while cur or stack:
         if cur:
            stack.append(cur)
            cur = cur.left
         else:
            parent = stack.pop()
            res.append(parent.val)
            cur = parent.right
      return res

if __name__ == "__main__":
   bst = BST()
   t = Solution()
   print t.bstSortedOrder(bst.getRoot())
