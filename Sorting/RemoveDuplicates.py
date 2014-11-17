class Solution:
   # Time: O(nlogn)
   # Space: O(1)
   def removeDuplicates(self, A):
      i = 0
      for j in range(1, len(A)):
         if A[j] != A[i]:
            i += 1
            A[i] = A[j]
      return A[:i+1]

if __name__ == "__main__":
   A = [1, 1, 2, 3, 3, 4, 5, 5, 5]
   t = Solution()
   print t.removeDuplicates(A)
