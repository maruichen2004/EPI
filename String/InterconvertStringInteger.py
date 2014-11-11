class Solution:
   # Time: O(len(x))
   # Space: O(1)
   def intToStr(self, x):
      if x == 0: return "0"
      sign = -1 if x < 0 else 1
      x = abs(x)
      res = ""
      while x > 0:
         res += str(x%10)
         x /= 10
      res = res[::-1]
      return "-" + res if sign == -1 else res

   # Time: O(len(s))
   # Space: O(1)
   def strToInt(self, s):
      if len(s) == 0 or s == "-": return 0
      neg = 1 if s[0] == "-" else 0
      res = 0
      for i in range(neg, len(s)):
         res = res * 10 + ord(s[i]) - ord("0")
      return -1 * res if neg == 1 else res

if __name__ == "__main__":
   x = -123
   t = Solution()
   s = t.intToStr(x)
   print s
   print t.strToInt(s)
