class Solution:
   # Time: O(n)
   # Space: O(n)
   def snakeString(self, s, nRows):
      if nRows == 1: return s
      cache = [[] for i in range(nRows)]
      pos, dir = 0, 1
      for i in s:
         cache[pos].append(i)
         if pos == 0: dir = 1
         if pos == nRows - 1: dir = -1
         pos += dir
      return "".join(["".join(i) for i in cache])

if __name__ == "__main__":
   s = "PAYPALISHIRING"
   nRows = 3
   t = Solution()
   print t.snakeString(s, nRows)
