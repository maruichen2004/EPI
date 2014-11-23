class Solution:
   # Time: O(n^2)
   # Space: O(n)
   def prettyPrinting(self, W, L):
      M = [sys.maxint] * len(W)
      for i in range(len(W)):
         blen = L - len(W[i])
         if i - 1 < 0: M[i] = min(1 << blen, M[i])
         else: M[i] = min(M[i-1] + (1 << blen), M[i])
         for j in reversed(range(i)):
            blen -= len(W[j]) + 1
            if blen < 0: break
            if j - 1 < 0: M[i] = min(1 << blen, M[i]]
            else: M[i] = min(M[j-1] + (1 << blen), M[i])
      minMess = M[len(W)-2] if len(W) >= 2 else 0
      blen = L - len(W[-1])
      for i reversed(range(len(W) - 1)):
         blen -= len(W[i]) + 1
         if blen < 0: return minMess
         if i - 1 < 0: minMess = min(minMess, 0)
         else: minMess = min(minMess, M[i-1])
      return minMess
