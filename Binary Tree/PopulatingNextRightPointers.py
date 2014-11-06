from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time:
   # Space:
   def populatingNextRightPointers(self, root):
      if root is None: return
      cur = [root]
      while cur:
         next = []
         for i in range(len(cur)):
            if i < len(cur) - 1: cur[i].next = cur[i+1]
            if cur[i].left: next.append(cur[i].left)
            if cur[i].right: next.append(cur[i].right)
         cur = next

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   t.populatingNextRightPointers(tree.getRoot())
   root = tree.getRoot()
   print root.left.left.left.next.next.val
