class Solution:
   # Time: O(mn)
   # Space: O(mn)
   def maxPathSum(self, grid):
      rows, cols = len(grid), len(grid[0])
      dp = [[0 for i in range(cols)] for j in range(rows)]
      dp[0][0] = grid[0][0]
      for i in range(1, rows):
         dp[i][0] = dp[i - 1][0] + grid[i][0]
      for j in range(1, cols):
         dp[0][j] = dp[0][j - 1] + grid[0][j]
      for i in range(1, rows):
         for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
      return dp[rows - 1][cols - 1]

if __name__ == "__main__":
   grid = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
   t = Solution()
   print t.maxPathSum(grid)
