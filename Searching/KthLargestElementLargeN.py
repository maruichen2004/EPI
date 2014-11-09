from random import randint

class Solution:
   # Time: O(n)
   # Space: O(1)
   def kthLargestElementLargeN(self, A, k):
      M = []
      for x in A:
         M.append(x)
         if len(M) == (k << 1) - 1:
            self.findKthLargest(M, k)
            M = M[:k]
      self.findKthLargest(M, k)
      print M
      return M[k - 1]

   def findKthLargest(self, A, k):
      l, r = 0, len(A) - 1
      while l <= r:
         pivot = randint(l, r)
         p = self.partition(l, r, k, A)
         if p == k - 1: return A[p]
         elif p > k - 1: r = p - 1
         else: l = p + 1
      return -1

   def partition(self, l, r, pivot, A):
      p = A[pivot]
      largestIndex = l
      A[pivot], A[r] = A[r], A[pivot]
      for i in range(l, r):
         if A[i] > p:
            A[i], A[largestIndex] = A[largestIndex], A[i]
            largestIndex += 1
      A[r], A[largestIndex] = A[largestIndex], A[r]
      return largestIndex

if __name__ == "__main__":
   A = [i for i in range(1000)]
   k = 5
   t = Solution()
   print t.kthLargestElementLargeN(A, k)
