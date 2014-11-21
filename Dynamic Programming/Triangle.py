class Solution:
   # Time: O(n^2)
   # Space: O(n)
   def minTotal(self, triangle):
      if len(triangle) == 0: return 0
      prev = triangle[0]
      for i in range(1, len(triangle)):
         cur = [prev[0] + triangle[i][0]]
         for j in range(1, len(prev)):
            cur.append(min(prev[j], prev[j-1]) + triangle[i][j])
         cur.append(cur[-1] + triangle[i][-1])
         prev = cur
      return min(prev)

if __name__ == "__main__":
   triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
   t = Solution()
   print t.minTotal(triangle)
