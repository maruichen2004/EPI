class Solution:
   # Time: O(1)
   # Space: O(1)
   def validIPAddress(self, s):
      res = []
      for i in range(1, 4):
         if i < len(s):
            first = s[:i]
            if self.isValid(first):
               for j in range(1, 4):
                  if i + j < len(s):
                     second = s[i:i+j]
                     if self.isValid(second):
                        for k in range(1, 4):
                           if i + j + k < len(s):
                              third, forth = s[i+j:i+j+k], s[i+j+k:]
                              if self.isValid(third) and self.isValid(forth):
                                 res.append(first + "." + second + "." + third + "." + forth)
      return res

   def isValid(self, s):
      if len(s) == 0 or (s[0] == "0" and s != "0") or len(s) > 3:
         return False
      return int(s) < 256

if __name__ == "__main__":
   s = "19216811"
   t = Solution()
   print t.validIPAddress(s)
