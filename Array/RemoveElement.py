class Solution:
   # Time: O(n)
   # Space: O(1)
   def removeElement(self, A, elem):
      i, last = 0, len(A)
      while i < last:
         if A[i] == elem:
            last -= 1
            A[i], A[last] = A[last], A[i]
         else:
            i += 1
      return A[:last]

if __name__ == "__main__":
   A = [1, 3, 5, 7, 1, 2, 3, 4]
   elem = 3
   t = Solution()
   print t.removeElement(A, elem)
