class Solution:
   # Time: O(kn)
   # Space: O(k)
   def numberSteps(self, n, k):
      if n <= 1: return 1
      dp = [0 for i in range(k+1)]
      dp[0], dp[1] = 1, 1
      for i in range(2, n+1):
         dp[i % (k + 1)] = 0
         for j in range(1, k+1):
            if i >= j: dp[i % (k+1)] += dp[(i - j) % (k + 1)]
      return dp[n % (k + 1)]

if __name__ == "__main__":
   t = Solution()
   print t.numberSteps(4, 2)
