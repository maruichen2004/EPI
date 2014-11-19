from Util.BinaryTree import TreeNode

class Solution:
   # Time: O(h)
   # Space: O(1)
   def insertNode(self, root, k):
      if root is None: return TreeNode(k)
      else:
         cur = root
         par = cur
         while cur:
            par = cur
            if cur.val == k: return root
            elif cur.val < k: cur = cur.right
            else: cur = cur.left
         if par.val < k: par.right = TreeNode(k)
         else: par.left = TreeNode(k)
      return root

   # Time: O(h)
   # Space: O(1)
   def deleteNode(self, root, k):
      if root is None: return root
      prev, cur = None, root
      while cur:
         if cur.val < k: prev, cur = cur, cur.right
         elif cur.val > k: prev, cur = cur, cur.left
         else:
            if cur.left is None and cur.right is None:
               if cur == prev.left: prev.left = None
               else: prev.right = None
            elif cur.left is None:
               if cur == prev.left: prev.left = cur.right
               else: prev.right = cur.right
            elif cur.right is None:
               if cur == prev.left: prev.left = cur.left
               else: prev.right = cur.left
            else:
               p, q = cur.left, cur
               while p.right:
                  q = p
                  p = p.right
               cur.val = p.val
               if p.left is None: p = None
               else: q.right = p.left
            return root
      return root

def inorder(root):
   if root:
      inorder(root.left)
      print root.val,
      inorder(root.right)

if __name__ == "__main__":
   A = [4, 3, 2, 1, 5, 6, 7]
   root = None
   t = Solution()
   for i in A:
      root = t.insertNode(root, i)
   #inorder(root)
   B = [3, 2, 5, 7]
   for i in B:
      root = t.deleteNode(root, i)
   inorder(root)
