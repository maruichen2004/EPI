from Util.BST import TreeNode
from Util.BST import BST
from collections import deque

class Solution:
   # Time: O(n)
   # Space: O(m) m is the max number of nodes in a depth
   def binaryTreeLevelOrder(self, root):
      if root is None: return []
      res, queue = [], deque([root])
      while queue:
         cur = queue.popleft()
         res.append(cur.val)
         if cur.left: queue.append(cur.left)
         if cur.right: queue.append(cur.right)
      return res

if __name__ == "__main__":
   bst = BST()
   t = Solution()
   print t.binaryTreeLevelOrder(bst.getRoot())
