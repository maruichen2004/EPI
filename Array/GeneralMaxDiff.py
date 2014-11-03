import sys
class Solution:
   # Time: O(kn)
   # Space: O(k)
   def maxDiffKPair(self, A, k):
      k_sum = [-sys.maxint - 1] * k * 2
      for i in range(len(A)):
         pre_k_sum, sign = [j for j in k_sum], -1
         for j in range(k*2):
            if j <= i:
               diff = sign * A[i] + (0 if j == 0 else pre_k_sum[j-1])
               k_sum[j] = max(diff, pre_k_sum[j])
            sign *= -1
      return k_sum[-1]

   # Time: O(n)
   # Space: O(1)
   def maxDiffUnlimitedPair(self, A):
      maxDiff = 0
      for i in range(len(A) - 1):
         maxDiff += max(0, A[i+1] - A[i])
      return maxDiff

if __name__ == "__main__":
   A = [1, 2, 3, 4, 5, 6, 7]
   k = 2
   t = Solution()
   print t.maxDiffKPair(A, k)
   print t.maxDiffUnlimitedPair(A)
