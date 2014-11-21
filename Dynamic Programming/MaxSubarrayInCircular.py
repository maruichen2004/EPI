class Solution:
   # Time: O(n)
   # Space: O(1)
   def maxSubarrayInCircular(self, A):
      return max(self.maxSubarray(A), sum(A) - self.minSubarray(A))

   def maxSubarray(self, A):
      tmp, res = 0, 0
      for a in A:
         tmp = max(a, tmp + a)
         res = max(tmp, res)
      return res

   def minSubarray(self, A):
      tmp, res = 0, 0
      for a in A:
         tmp = min(a, tmp + a)
         res = min(tmp, res)
      return res

if __name__ == "__main__":
   A = [3, 2, 1, -1, 4, -3, -1]
   t = Solution()
   print t.maxSubarrayInCircular(A)
