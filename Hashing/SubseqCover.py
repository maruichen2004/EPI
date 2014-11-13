import sys

class Solution:
   # Time: O(len(A))
   # Space: O(len(Q))
   def subseqCover(self, A, Q):
      K, L, D, start, end = {}, [-1] * len(Q), [sys.maxint] * len(Q), -1, len(A)
      for i in range(len(Q)):
         K[Q[i]] = i
      for i in range(len(A)):
         if A[i] in K:
            idx = K[A[i]]
            if idx == 0: D[0] = 1
            elif D[idx - 1] != sys.maxint: D[idx] = i - L[idx - 1] + D[idx - 1]
            L[idx] = i
            if idx == len(Q) - 1 and D[len(D) - 1] < end - start + 1:
               start, end = i - D[len(D) - 1] + 1, i
      return A[start:end+1]

if __name__ == "__main__":
   A, Q = [1, 2, 3, 4, 4, 2, 5, 6], [3, 4, 5]
   t = Solution()
   print t.subseqCover(A, Q)
