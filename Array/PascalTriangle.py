class Solution:
   # Time: O(n^2)
   # Space: O(n^2)
   def generatePascalTriangle(self, n):
      if n == 0: return []
      res, cur = [], [1]
      res.append(cur)
      for i in range(1, n):
         next = [1]
         for j in range(i - 1):
            next.append(cur[j] + cur[j+1])
         next.append(1)
         res.append(next)
         cur = next
      return res

   # Time: O(n^2)
   # Space: O(n)
   def kthPascalTriangle(self, k):
      res = [1]
      for i in range(1, k + 1):
         next = [1]
         for j in range(i - 1):
            next.append(res[j] + res[j+1])
         next.append(1)
         res = next
      return res

if __name__ == "__main__":
   n = 4
   t = Solution()
   print t.generatePascalTriangle(n)
   k = 4
   print t.kthPascalTriangle(k)
