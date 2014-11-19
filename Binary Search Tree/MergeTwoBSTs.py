from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def mergeTwoBSTs(self, a, b):
      l1 = self.BSTToSortedList(a)
      l2 = self.BSTToSortedList(b)
      head = self.mergeTwoSortedLists(l1, l2)
      return self.SortedListToBST(head)

   def BSTToSortedList(self, root):
      head = self.BSTToSortedListHelper(root)
      head.left.right = None
      head.left = None
      return head

   def BSTToSortedListHelper(self, root):
      if root is None: return None
      l_head = self.BSTToSortedListHelper(root.left)
      r_head = self.BSTToSortedListHelper(root.right)
      l_tail, r_tail = None, None
      if l_head:
         l_tail = l_head.left
         l_tail.right = root
         root.left = l_tail
         l_tail = root
      else:
         l_head = root
         l_tail = root
      if r_head:
         r_tail = r_head.left
         r_head.left = l_tail
         l_tail.right = r_head
      else:
         r_tail = l_tail
      r_tail.right = l_head
      l_head.left = r_tail
      return l_head

   def mergeTwoSortedLists(self, l1, l2):
      dummy = TreeNode(0)
      cur = dummy
      while l1 and l2:
         if l1.val < l2.val:
            cur.right = l1
            l1.left = cur
            l1, cur = l1.right, cur.right
         else:
            cur.right = l2
            l2.left = cur
            l2, cur = l2.right, cur.right
      if l1 is not None:
         cur.right = l1
         l1.left = cur
      if l2 is not None:
         cur.right = l2
         l2.left = cur
      return dummy.right

   def SortedListToBST(self, head):
      cur, length = head, 0
      while cur:
         cur = cur.right
         length += 1
      self.head = head
      return self.SortedListToBSTHelper(0, length - 1)

   def SortedListToBSTHelper(self, l, r):
      if l > r: return None
      mid = l + ((r - l) >> 1)
      left = self.SortedListToBSTHelper(l, mid - 1)
      root = self.head
      root.left = left
      self.head = self.head.right
      root.right = self.SortedListToBSTHelper(mid + 1, r)
      return root

def inorder(root):
   if root:
      inorder(root.left)
      print root.val,
      inorder(root.right)

if __name__ == "__main__":
   t1 = BinaryTree()
   t2 = BinaryTree(10)
   t = Solution()
   root = t.mergeTwoBSTs(t1.getRoot(), t2.getRoot())
   inorder(root)
