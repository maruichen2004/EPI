class Solution:
   # Time: O(n^2)
   # Space: O(n^2)
   def houseMajority(self, probs, n):
      dp = [[-1.0 for i in range(n+1)] for j in range(n+1)]
      sum = 0.0
      for r in range(n/2, n+1):
         sum += self.houseMajorityHelper(probs, r, n, dp)
      return sum

   def houseMajorityHelper(self, probs, r, n, dp):
      if r > n: return 0.0
      if r == 0 and n == 0: return 1.0
      if r < 0: return 0.0
      if dp[r][n] == -1.0:
         dp[r][n] = self.houseMajority(probs, r-1, n-1, dp) * probs[n-1] + self.houseMajority(probs, r, n-1, dp) * (1 - probs[n-1])
      return dp[r][n] 
