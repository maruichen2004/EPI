class Solution:
   # Time: O(n^2)
   # Space: O(n)
   def longestNondecreasingSubsequence(self, A):
      if len(A) == 0: return A
      length = [1] * len(A)
      prevIdx = [-1] * len(A)
      maxIdx = 0
      for i in range(1, len(A)):
         for j in range(i):
            if A[i] >= A[j] and length[j] + 1 > length[i]:
               length[i] = length[j] + 1
               prevIdx[i] = j
      if length[i] > length[maxIdx]: maxIdx = i
      maxLength = length[maxIdx]
      res = [0] * maxLength
      while maxLength > 0:
         res[maxLength] = A[maxIdx]
         maxIdx = prevIdx[maxIdx]
         maxLength -= 1
      return res
