class Solution:
   # Time:
   # Space:
   def nQueens(self, n):
      res = []
      self.nQueensHelper(res, [], n, 0)
      return res

   def nQueensHelper(self, res, cur, n, i):
      if i == n: res.append(map((lambda x: "." * x + "Q" + "." * (n-1-x)),cur))
      for j in range(n):
         if j not in cur and self.check(cur, i, j):
            self.nQueensHelper(res, cur + [j], n, i + 1)

   def check(self, cur, row, col):
      for i in range(len(cur)):
         if abs(row - i) == abs(col - cur[i]):
            return False
      return True

if __name__ == "__main__":
   n = 8
   t = Solution()
   print t.nQueens(n)
