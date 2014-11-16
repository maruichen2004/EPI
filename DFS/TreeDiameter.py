import sys

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.edges = []

class Solution:
   # Time: O(n)
   # Space: O(n)
   def computeDiameter(self, root):
      return self.computeDiameterHelper(root)[1] if root is not None else 0.0

   def computeDiameterHelper(self, root):
      diameter = sys.float_info.min
      height = [0.0, 0.0]
      for node, h in root.edges:
         heightDiameter = self.computeDiameterHelper(node)
         if heightDiameter[0] + h > height[0]:
            height[1] = height[0]
            height[0] = heightDiameter[0] + h
         elif heightDiameter[0] + h > height[1]:
            height[1] = heightDiameter[0] + h
         diameter = max(diameter, heightDiameter[1])
      return (height[0], max(diameter, height[0] + height[1]))

if __name__ == "__main__":
   nodes = [TreeNode(i+1) for i in range(16)]
   nodes[0].edges = [(nodes[1], 7), (nodes[2], 14), (nodes[3], 3)]
   nodes[1].edges = [(nodes[4], 4), (nodes[5], 3)]
   nodes[4].edges = [(nodes[8], 6)]
   nodes[3].edges = [(nodes[6], 2), (nodes[7], 1)]
   nodes[7].edges = [(nodes[9], 6), (nodes[10], 4)]
   nodes[10].edges = [(nodes[11], 4), (nodes[12], 2)]
   nodes[12].edges = [(nodes[13], 1), (nodes[14], 2), (nodes[15], 3)]
   t = Solution()
   print t.computeDiameter(nodes[0])
