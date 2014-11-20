class Solution:
   # Time: O(mnl)
   # Space: O(mnl)
   def wordSearch(self, board, word):
      visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
      for i in range(len(board)):
         for j in range(len(board[0])):
            if self.wordSearchHelper(board, word, visited, i, j):
               return True
      return False

   def wordSearchHelper(self, board, word, visited, i, j):
      if len(word) == 0: return True
      if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or visited[i][j] == 1 or board[i][j] != word[0]:
         return False
      visited[i][j] = 1
      found = self.wordSearchHelper(board, word[1:], visited, i + 1, j) or \
              self.wordSearchHelper(board, word[1:], visited, i - 1, j) or \
              self.wordSearchHelper(board, word[1:], visited, i, j + 1) or \
              self.wordSearchHelper(board, word[1:], visited, i, j - 1)
      visited[i][j] = 0
      return found

if __name__ == "__main__":
   board = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
   word = "abcced"
   t = Solution()
   print t.wordSearch(board, word)
