class Solution:
   # Time: O(nW)
   # Space: O(W)
   def knapsack(self, W, items):
      V = [0] * (W + 1)
      for i in range(len(items)):
         for j in reversed(range(items[i][0], W + 1)):
            V[j] = max(V[j], V[j - items[i][0]] + items[i][1])
      return V[W]

if __name__ == "__main__":
   items = [[2, 3], [3, 4], [4, 5], [5, 6]]
   W = 5
   t = Solution()
   print t.knapsack(W, items)
