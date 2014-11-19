class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

class Solution:
   # Time: O(h)
   # Space: O(h)
   def searchMinFirstBST(self, root, k):
      if root is None or root.val > k: return False
      elif root.val == k: return True
      elif root.right and root.right.val <= k:
         return self.searchMinFirstBST(root.right, k)
      else:
         return self.searchMinFirstBST(root.left, k)

if __name__ == "__main__":
   nodes = [TreeNode(i+2) for i in range(7)]
   nodes[0].left = nodes[1]
   nodes[0].right = nodes[3]
   nodes[1].right = nodes[2]
   nodes[3].right = nodes[4]
   nodes[4].left = nodes[5]
   nodes[4].right = nodes[6]
   t = Solution()
   k = 6
   print t.searchMinFirstBST(nodes[0], k)
