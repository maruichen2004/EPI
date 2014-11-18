from Util.BinaryTree import TreeNode

class ListNode:
   def __init__ (self, val):
      self.val = val
      self.next = None

class Solution:
   # Time: O(n)
   # Space: O(logn)
   def sortedListToBST(self, head):
      cur, length = head, 0
      while cur:
         cur = cur.next
         length += 1
      self.head = head
      return self.sortedListToBSTHelper(0, length - 1)

   def sortedListToBSTHelper(self, l, r):
      if l > r: return None
      mid = l + ((r - l) >> 1)
      left = self.sortedListToBSTHelper(l, mid - 1)
      root = TreeNode(self.head.val)
      root.left = left
      self.head = self.head.next
      root.right = self.sortedListToBSTHelper(mid + 1, r)
      return root

def inorder(root):
   if root:
      inorder(root.left)
      print root.val,
      inorder(root.right)

def preorder(root):
   if root:
      print root.val,
      preorder(root.left)
      preorder(root.right)

if __name__ == "__main__":
   nodes = [ListNode(2*i + 1) for i in range(7)]
   for i in range(6): nodes[i].next = nodes[i+1]
   t = Solution()
   root = t.sortedListToBST(nodes[0])
   preorder(root)
   inorder(root)
