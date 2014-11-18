from Util.BinaryTree import TreeNode

class Solution:
   # Time: O(n)
   # Space: O(logn)
   def sortedArrayToBST(self, A):
      return self.sortedArrayToBSTHelper(A, 0, len(A))

   def sortedArrayToBSTHelper(self, A, s, e):
      if s < e:
         mid = s + ((e - s) >> 1)
         root = TreeNode(A[mid])
         root.left = self.sortedArrayToBSTHelper(A, s, mid)
         root.right = self.sortedArrayToBSTHelper(A, mid+1, e)
         return root
      return None

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
   A = [1, 3, 5, 7, 9, 11, 13]
   t = Solution()
   root = t.sortedArrayToBST(A)
   preorder(root)
   inorder(root)   
