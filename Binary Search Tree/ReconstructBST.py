from Util.BinaryTree import TreeNode
from Util.BinaryTree import BinaryTree

class Solution:
   # Time: O(n)
   # Space: O(h)
   def reconstructBST(self, root):
      nodes = [None, None, None]
      self.reconstructBSTHelper(root, nodes)
      nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val

   def reconstructBSTHelper(self, root, nodes):
      if root is None: return
      self.reconstructBSTHelper(root.left, nodes)
      if nodes[2] and nodes[2].val > root.val:
         nodes[1] = root
         if nodes[0] is None: nodes[0] = nodes[2]
      nodes[2] = root
      self.reconstructBSTHelper(root.right, nodes)

def inorder(root):
   if root:
      inorder(root.left)
      print root.val,
      inorder(root.right)

if __name__ == "__main__":
   tree = BinaryTree()
   t = Solution()
   tree.getRoot().left.right.val, tree.getRoot().right.left.val = tree.getRoot().right.left.val, tree.getRoot().left.right.val
   inorder(tree.getRoot())
   t.reconstructBST(tree.getRoot())
   inorder(tree.getRoot())
