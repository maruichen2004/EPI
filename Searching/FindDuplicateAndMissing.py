class Solution:
   # Time: O(n)
   # Space: O(1)
   def findDuplicateAndMissing(self, A):
      sum, square = 0, 0
      for i in range(len(A)):
         sum += i - A[i]
         square += i * i - A[i] * A[i]
      return (square/sum - sum) >> 1, (square/sum + sum) >> 1

if __name__ == "__main__":
   A = [0, 1, 2, 2, 4, 5]
   t = Solution()
   print t.findDuplicateAndMissing(A)
