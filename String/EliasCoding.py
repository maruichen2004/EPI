from random import randint

class Solution:
   # Time: O(n)
   # Space: O(n)
   def encode(self, A):
      res = ""
      for a in A:
         binary = self.intToBinary(a)
         for i in range(len(binary)):
            res += "0"
         res += binary
      return res

   def intToBinary(self, decimal):
      res = ""
      while decimal != 0:
         res += str(decimal & 1)
         decimal >>= 1
      res = res[::-1]
      return res

   # Time: O(len(s))
   # Space: O(n)
   def decode(self, s):
      res = []
      idx = 0
      while idx < len(s):
         zeroIdx = idx
         while zeroIdx < len(s) and s[zeroIdx] == "0":
            zeroIdx += 1
         length = zeroIdx - idx
         res.append(self.binaryToInt(s[zeroIdx:zeroIdx+length]))
         idx = zeroIdx + length
      return res

   def binaryToInt(self, binary):
      res = 0
      for ch in binary:
         res = res * 2 + (ord(ch) - ord("0"))
      return res

if __name__ == "__main__":
   A = [randint(0, 99) for i in range(10)]
   t = Solution()
   x = t.encode(A)
   print A
   print x
   print t.decode(x)
