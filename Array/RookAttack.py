class Solution:
   # Time:
   # Space:
   def rookAttack(self, board):
      firstRow, firstCol = False, False
      rows, cols = len(board), len(board[0])
      for i in range(cols):
         if board[0][i] == 0:
            firstRow = True
            break
      for i in range(rows):
         if board[i][0] == 0:
            firstCol = True
            break
      for i in range(1, rows):
         for j in range(1, cols):
            if board[i][j] == 0:
               board[i][0], board[0][j] = 0, 0
      for i in range(1, rows):
         for j in range(1, cols):
            if board[0][j] == 0 or board[i][0] == 0:
               board[i][j] = 0
      if firstRow:
         for i in range(cols): board[0][i] = 0
      if firstCol:
         for i in range(rows): board[i][0] = 0

if __name__ == "__main__":
   board = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1]]
   t = Solution()
   t.rookAttack(board)
   print board
