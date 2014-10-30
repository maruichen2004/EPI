class TreeNode:
   def __init__(self, value):
      self.val = value
      self.left = None
      self.right = None

class BST:
   def __init__(self):
      node = [TreeNode(i) for i in range(1, 11)]
      node[5].left = node[3]
      node[5].right = node[7]
      node[3].left = node[1]
      node[3].right = node[4]
      node[1].left = node[0]
      node[1].right = node[2]
      node[7].left = node[6]
      node[7].right = node[9]
      node[9].left = node[8]
      self.root = node[5]

   def getRoot(self):
      return self.root
