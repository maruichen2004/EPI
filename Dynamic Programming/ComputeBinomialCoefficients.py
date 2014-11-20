class Solution:
   # Time: O(nk)
   # Sapce: O(k)
   def computeBinomialCoefficients(self, n, k):
      dp = [[0] * (k + 1), [0] * (k + 1)]
      dp[0][0] = 1
      for i in range(1, n + 1):
         dp[i & 1][0] = 1
         for j in range(1, k + 1):
            if j <= i:
               dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[(i - 1) & 1][j - 1]
      return dp[n & 1][k]

if __name__ == "__main__":
   t = Solution()
   n = 5
   for i in range(n+1):
      print t.computeBinomialCoefficients(n, i)
