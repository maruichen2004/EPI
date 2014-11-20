class Solution:
   # Time: O(mn)
   # Space: O(mn)
   def uniquePath(self, m, n):
      dp = [[1 for i in range(n)] for j in range(m)]
      for i in range(1, m):
         for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
      return dp[m - 1][n - 1]

   def uniquePath2(self, board):
      rows, cols = len(board), len(board[0])
      dp = [[0] * cols] * rows
      for i in range(rows):
         dp[i][0] = 1 if board[i][0] else 0
      for j in range(cols):
         dp[0][j] = 1 if board[0][j] else 0
      for i in range(1, rows):
         for j in range(1, cols):
            dp[i][j] = 0 if board[i][j] == False else dp[i - 1][j] + dp[i][j - 1]
      return dp[rows - 1][cols - 1]

if __name__ == "__main__":
   m, n = 3, 7
   t = Solution()
   print t.uniquePath(m, n)
   board = [[True, True, True], [True, False, True], [True, True, True]]
   print t.uniquePath2(board)
