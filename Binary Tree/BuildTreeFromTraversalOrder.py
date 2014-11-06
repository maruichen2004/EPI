from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def buildTreeFromInorderAndPreorder(self, inorder, preorder):
      if len(inorder) == 0: return None
      root = TreeNode(preorder[0])
      idx = inorder.index(preorder[0])
      root.left = self.buildTreeFromInorderAndPreorder(inorder[:idx], preorder[1:idx+1])
      root.right = self.buildTreeFromInorderAndPreorder(inorder[idx+1:], preorder[idx+1:])
      return root

   def buildTreeFromInorderAndPostorder(self, inorder, postorder):
      if len(inorder) == 0: return None
      root = TreeNode(postorder[-1])
      idx = inorder.index(postorder[-1])
      root.left = self.buildTreeFromInorderAndPostorder(inorder[:idx], postorder[:idx])
      root.right = self.buildTreeFromInorderAndPostorder(inorder[idx+1:], postorder[idx:-1])
      return root

def display(root):
   if root:
      display(root.left)
      print root.val,
      display(root.right)

if __name__ == "__main__":
   preorder = [6, 4, 2, 1, 3, 5, 8, 7, 10, 9]
   inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   postorder = [1, 3, 2, 5, 4, 7, 9, 10, 8, 6]
   t = Solution()
   root = t.buildTreeFromInorderAndPostorder(inorder, postorder)
   display(root)
