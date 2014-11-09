class Solution:
   # Time: O(n)
   # Space: O(1)
   def singleNumber(self, A):
      bits, res = [0] * 32, 0
      for x in A:
         for i in range(32):
            if x & (1 << i) == 1 << i:
               bits[i] += 1 << i
      if bits[31] % 3 == 0:
         for i in range(31):
            if bits[i] % 3 == 1:
               res += 1 << i
      elif bits[31] % 3 == 1:
         for i in range(31):
            if bits[i] % 3 == 0:
               res += 1 << i
         res = -(1 + res)
      return res

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9, 1, 3, 7, 9, 9, 7, 3, 1]
   t = Solution()
   print t.singleNumber(A)
