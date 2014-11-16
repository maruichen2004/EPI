from Util.BinaryTree import TreeNode

class Solution:
   # Time: C(n) = sum(C(n-i) * C(i-1))
   # Space: O(n)
   def uniqueBinaryTrees(self, n):
      return self.uniqueBinaryTreesHelper(1, n)

   def uniqueBinaryTreesHelper(self, low, high):
      res = []
      if low > high: res.append(None)
      else:
         for i in range(low, high+1):
            left = self.uniqueBinaryTreesHelper(low, i-1)
            right = self.uniqueBinaryTreesHelper(i+1, high)
            for j in left:
               for k in right:
                  root = TreeNode(i)
                  root.left = j
                  root.right = k
                  res.append(root)
      return res

if __name__ == "__main__":
   n = 3
   t = Solution()
   res = t.uniqueBinaryTrees(n)
   print len(res)
