class Solution:
   # Time: O(n)
   # Space: O(1)
   def nextPermutation(self, A):
      k, l = -1, 0
      for i in range(len(A) - 1):
         if A[i] < A[i+1]: k = i
      if k == -1: return A[::-1]
      for i in range(len(A)):
         if A[i] > A[k]: l = i
      A[l], A[k] = A[k], A[l]
      return A[:k+1] + A[:k:-1]

   def previousPermutation(self, A):
      k, l = len(A), 0
      for i in range(len(A) - 1):
         if A[i] < A[i+1]: k = i
      if k == len(A): return A[::-1]
      for i in range(len(A)):
         if A[i] < A[k]: l = i
      A[l], A[k] = A[k], A[l]
      return A[:k+1] + A[:k:-1]

if __name__ == "__main__":
   A = [1, 2, 4, 3]
   t = Solution()
   print t.nextPermutation(A)
   print t.previousPermutation(A)
