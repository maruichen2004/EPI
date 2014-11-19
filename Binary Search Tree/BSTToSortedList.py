from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def BSTToSortedList(self, root):
      head = self.BSTToSortedListHelper(root)
      head.left.right = None
      head.left = None
      return head

   def BSTToSortedListHelper(self, root):
      if root is None: return None
      l_head = self.BSTToSortedListHelper(root.left)
      r_head = self.BSTToSortedListHelper(root.right)
      l_tail = None
      if l_head:
         l_tail = l_head.left
         l_tail.right = root
         root.left = l_tail
         l_tail = root
      else:
         l_head = root
         l_tail = root
      r_tail = None
      if r_head:
         r_tail = r_head.left
         l_tail.right = r_head
         r_head.left = l_tail
      else:
         r_tail = l_tail
      r_tail.right = l_head
      l_head.left = r_tail
      return l_head

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   head = t.BSTToSortedList(tree.getRoot())
   cur = head
   while cur:
      print cur.val,
      cur = cur.right
