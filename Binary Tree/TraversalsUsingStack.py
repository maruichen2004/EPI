from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def preorder(self, root):
      if root is None: return []
      stack, res = [root], []
      while stack:
         cur = stack.pop()
         res.append(cur.val)
         if cur.right is not None:
            stack.append(cur.right)
         if cur.left is not None:
            stack.append(cur.left)
      return res

   def inorder(self, root):
      if root is None: return []
      stack, res, cur = [], [], root
      while stack or cur:
         if cur is not None:
            stack.append(cur)
            cur = cur.left
         else:
            parent = stack.pop()
            res.append(parent.val)
            cur = parent.right
      return res

   def postorder(self, root):
      if root is None: return []
      stackRdy, stackPre, res = [], [root], []
      while stackPre:
         cur = stackPre.pop()
         stackRdy.append(cur.val)
         if cur.left is not None:
            stackPre.append(cur.left)
         if cur.right is not None:
            stackPre.append(cur.right)
      while stackRdy:
         res.append(stackRdy.pop())
      return res

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   print t.preorder(tree.getRoot())
   print t.inorder(tree.getRoot())
   print t.postorder(tree.getRoot())
