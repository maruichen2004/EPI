from random import randint
class Solution:
   # Time: O(n)
   # Space: O(1)
   def randomPermutation(self, A):
      for i in reversed(range(len(A))):
         r = randint(0, i)
         A[r], A[i] = A[i], A[r]

if __name__ == "__main__":
   A = [1, 2, 3, 4]
   t = Solution()
   t.randomPermutation(A)
   print A
