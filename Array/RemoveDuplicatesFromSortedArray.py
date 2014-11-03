class Solution:
   # Time: O(n)
   # Space: O(1)
   def removeDuplicatesFromSortedArray(self, A):
      i = 0
      for j in range(1, len(A)):
         if A[i] != A[j]:
            i += 1
            A[i] = A[j]
      return A[:i+1]

if __name__ == "__main__":
   A = [1, 1, 2, 3, 3, 4, 4, 5]
   t = Solution()
   print t.removeDuplicatesFromSortedArray(A)
