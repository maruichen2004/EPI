class Solution:
   # Time: O(sn)
   # Space: O(s)
   def scorePermutation(self, scores, k):
      dp = [0] * (k + 1)
      dp[0] = 1
      for i in range(k + 1):
         for score in scores:
            if i >= score: dp[i] += dp[i - score]
      return dp[k]

if __name__ == "__main__":
   scores = [2, 3, 7]
   k = 12
   t = Solution()
   print t.scorePermutation(scores, k)
