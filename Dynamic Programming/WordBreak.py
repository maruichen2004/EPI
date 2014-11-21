class Solution:
   # Time:
   # Space:
   def wordBreak(self, dict, s):
      res = []
      self.wordBreakHelper(res, "", dict, s)
      return res

   def wordBreakHelper(self, res, cur, dict, s):
      if self.canBreak(dict, s):
         if len(s) == 0: res.append(cur[1:])
         for i in range(1, len(s) + 1):
            if s[:i] in dict:
               self.wordBreakHelper(res, cur + " " + s[:i], dict, s[i:])

   def canBreak(self, dict, s):
      dp = [False for i in range(len(s) + 1)]
      dp[0] = True
      for i in range(1, len(s) + 1):
         for k in range(i):
            if dp[k] and s[k:i] in dict:
               dp[i] = True
      return dp[len(s)]

if __name__ == "__main__":
   dict = ["cat", "cats", "and", "sand", "dog"]
   s = "catsanddog"
   t = Solution()
   print t.wordBreak(dict, s)
