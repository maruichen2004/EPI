class Solution:
   # Time: O((c+1)(d+1))
   # Space: O((c+1)(d+1))
   def heightDetermination(self, c, d):
      F = [[-1 for i in range(d + 1)] for j in range(c + 1)]
      return self.heightDeterminationHelper(F, c, d)

   def heightDeterminationHelper(self, F, c, d):
      if c == 0 or d == 0: return 0
      elif c == 1: return d
      else:
         if F[c][d] == -1:
            F[c][d] = self.heightDeterminationHelper(F, c, d-1) + 1 + self.heightDeterminationHelper(F, c-1, d-1)
         return F[c][d]

if __name__ == "__main__":
   t = Solution()
   print t.heightDetermination(1, 10)
   print t.heightDetermination(2, 1)
   print t.heightDetermination(2, 2)
   print t.heightDetermination(2, 3)
   print t.heightDetermination(2, 4)
   print t.heightDetermination(2, 5)
   print t.heightDetermination(3, 2)
   print t.heightDetermination(100, 2)
   print t.heightDetermination(3, 5)
   print t.heightDetermination(8, 11)
   print t.heightDetermination(3, 0)
   print t.heightDetermination(3, 1)
   print t.heightDetermination(3, 3)
   print t.heightDetermination(0, 10)
   print t.heightDetermination(0, 0)
