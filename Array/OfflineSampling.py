from random import randint
class Solution:
   # Time: O(n)
   # Space: O(1)
   def offlineSampling(self, A, k):
      for i in reversed(range(len(A) - 1 - k, len(A))):
         r = randint(0, i)
         A[r], A[i] = A[i], A[r]
      return A[:k:-1]

if __name__ == "__main__":
   A = [1, 2, 3, 4, 5]
   k = 2
   t = Solution()
   print t.offlineSampling(A, k)
