class Solution:
   # Time:
   # Space:
   def regularExpressionMatching(self, s, p):
      if s is None or p is None: return False
      if len(p) == 0: return len(s) == 0
      if len(p) == 1 or p[1] != "*":
         if len(s) > 0 and (s[0] == p[0] or p[0] == "."):
            return self.regularExpressionMatching(s[1:], p[1:])
         else:
            return False
      else:
         i = -1
         length = len(s)
         while i < length and (i < 0 or s[i] == p[0] or p[0] == "."):
            if self.regularExpressionMatching(s[i+1:], p[2:]):
               return True
            i += 1
         return False

if __name__ == "__main__":
   s = "abbbc"
   p = "ab*c"
   t = Solution()
   print t.regularExpressionMatching(s, p)
