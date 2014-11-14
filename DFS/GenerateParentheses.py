class Solution:
   # Time:
   # Space:
   def generateParentheses(self, n):
      res = []
      self.generateParenthesesHelper(res, "", n, n)
      return res

   def generateParenthesesHelper(self, res, cur, left, right):
      if left == 0 and right == 0:
         res.append(cur)
      if left > 0:
         self.generateParenthesesHelper(res, cur + "(", left - 1, right)
      if left < right:
         self.generateParenthesesHelper(res, cur + ")", left, right - 1)

if __name__ == "__main__":
   n = 4
   t = Solution()
   print t.generateParentheses(n)
