class Solution:
   # Time: O(nlogn)
   # Space: O(1)
   def nonConstructibleChange(self, A):
      A.sort()
      sum = 0
      for i in range(len(A)):
         if A[i] > sum + 1: break
         else: sum  += A[i]
      return sum + 1

if __name__ == "__main__":
   A = [1, 1, 4, 5]
   t = Solution()
   print t.nonConstructibleChange(A)
