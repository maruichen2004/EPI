class Solution:
   # Time: O(n(V+1))
   # Space:  O(n(V+1))
   def tieElection(self, V):
      total = sum(V)
      if total & 1 == 1: return 0
      dp = [[0 for i in range(total + 1)] for j in range(len(V) + 1)]
      dp[0][0] = 1
      for i in range(len(V)):
         for j in range(total + 1):
            dp[i+1][j] = dp[i][j]
            if j >= V[i]: dp[i+1][j] += dp[i][j-V[i]]
      return dp[len(V)][total/2]

if __name__ == "__main__":
   V = [4, 5, 2, 7]
   t = Solution()
   print t.tieElection(V)
