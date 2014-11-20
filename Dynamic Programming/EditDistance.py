class Solution:
   # Time: O(mn)
   # Space: O(mn)
   def editDistance(self, s1, s2):
      dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
      for i in range(1, len(s1) + 1):
         dp[0][i] = dp[0][i - 1] + 1
      for i in range(1, len(s2) + 1):
         dp[i][0] = dp[i - 1][0] + 1
      for i in range(1, len(s2) + 1):
         for j in range(1, len(s1) + 1):
            addition = dp[i][j - 1] + 1
            deletion = dp[i - 1][j] + 1
            replace = dp[i - 1][j - 1]
            if s2[i - 1] != s1[j - 1]: replace += 1
            dp[i][j] = min(addition, deletion, replace)
      return dp[len(s2)][len(s1)]

if __name__ == "__main__":
   s1, s2 = "saturday", "sunday"
   t = Solution()
   print t.editDistance(s1, s2)
