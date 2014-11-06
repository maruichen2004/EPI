from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def buildTreeFromMarkedPreorder(self, preorder):
      stack = []
      for num in reversed(preorder):
         if num is None: stack.append(None)
         else:
            left = stack.pop()
            right = stack.pop()
            root = TreeNode(num)
            root.left = left
            root.right = right
            stack.append(root)
      return stack[-1]

def display(root):
   if root:
      display(root.left)
      print root.val,
      display(root.right)

if __name__ == "__main__":
   preorder = [6, 4, 2, 1, None, None, 3, None, None, 5, None, None, 8, 7, None, None, 10, 9, None, None, None]
   t = Solution()
   root = t.buildTreeFromMarkedPreorder(preorder)
   display(root)
