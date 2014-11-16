class TreeNode:
   def __init__(self, value):
      self.val = value
      self.left = None
      self.right = None
      self.parent = None
      self.next = None
      self.size = 0

class BinaryTree:
   def __init__(self):
      node = [TreeNode(i) for i in range(1, 11)]
      node[5].left = node[3]
      node[5].right = node[7]
      node[3].left = node[1]
      node[3].right = node[4]
      node[3].parent = node[5]
      node[1].left = node[0]
      node[1].right = node[2]
      node[1].parent = node[3]
      node[4].parent = node[3]
      node[7].left = node[6]
      node[7].right = node[9]
      node[7].parent = node[5]
      node[9].left = node[8]
      node[9].parent = node[7]
      node[6].parent = node[7]
      node[0].parent = node[1]
      node[2].parent = node[1]
      node[8].parent = node[9]
      node[0].size = 1
      node[1].size = 3
      node[2].size = 1
      node[3].size = 5
      node[4].size = 1
      node[5].size = 10
      node[6].size = 1
      node[7].size = 4
      node[8].size = 1
      node[9].size = 2
      self.root = node[5]

   def getRoot(self):
      return self.root
