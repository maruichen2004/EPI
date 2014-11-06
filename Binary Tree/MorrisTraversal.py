from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(1)
   def preorder(self, root):
      cur, res = root, []
      while cur:
         if cur.left is None:
            res.append(cur.val)
            cur = cur.right
         else:
            prev = cur.left
            while prev.right is not None and prev.right is not cur:
               prev = prev.right
            if prev.right is None:
               res.append(cur.val)
               prev.right = cur
               cur = cur.left
            else:
               prev.right = None
               cur = cur.right
      return res

   def inorder(self, root):
      cur, res = root, []
      while cur:
         if cur.left is None:
            res.append(cur.val)
            cur = cur.right
         else:
            prev = cur.left
            while prev.right is not None and prev.right is not cur:
               prev = prev.right
            if prev.right is None:
               prev.right = cur
               cur = cur.left
            else:
               prev.right = None
               res.append(cur.val)
               cur = cur.right
      return res

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.preorder(tree.getRoot())
   print t.inorder(tree.getRoot())
