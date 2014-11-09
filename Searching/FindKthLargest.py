from random import randint

class Solution:
   # Time: O(n)
   # Space: O(1)
   def findKthLargest(self, A, k):
      l, r = 0, len(A) - 1
      while l <= r:
         pivot = randint(l, r)
         p = self.partition(l, r, pivot, A)
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
   A = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
   k = 4
   t = Solution()
   print t.findKthLargest(A, k)
