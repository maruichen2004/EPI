class Solution:
   # Time: O(2^n)
   # Space: O(1)
   def grayCode(self, n):
      res = [0]
      for i in range(n):
         highbit = 1 << i
         for j in reversed(range(len(res))):
            res.append(highbit + res[j])
      return res

if __name__ == "__main__":
   n = 3
   t = Solution()
   print t.grayCode(n)
