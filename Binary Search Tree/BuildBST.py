from Util.BinaryTree import TreeNode

class Solution:
   # Time: O(h)
   # Space: O(h)
   def buildBSTPreorder(self, preorder):
      return self.buildBSTPreorderHelper(preorder, 0, len(preorder))

   def buildBSTPreorderHelper(self, preorder, s, e):
      if s < e:
         x = s + 1
         while x < e and preorder[x] < preorder[s]: x += 1
         root = TreeNode(preorder[s])
         root.left = self.buildBSTPreorderHelper(preorder, s+1, x)
         root.right = self.buildBSTPreorderHelper(preorder, x, e)
         return root
      return None

def inorder(root):
   if root:
      inorder(root.left)
      print root.val,
      inorder(root.right)

if __name__ == "__main__":
   preorder = [6, 4, 2, 1, 3, 5, 8, 7, 10, 9]
   t = Solution()
   root = t.buildBSTPreorder(preorder)
   inorder(root)
