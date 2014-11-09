class Solution:
   # Time: O(logn)
   # Space: O(1)
   def binarySearchCircularArray(self, A):
      l, r = 0, len(A) - 1
      while l < r:
         mid = l + ((r - l) >> 1)
         if A[mid] > A[r]: l = mid + 1
         else: r = mid
      return l

   # Time: O(n)
   # Space: O(n)
   def binarySearchCircularArrayDuplicates(self, A):
      return self.binarySearchCircularArrayDuplicatesHelper(A, 0, len(A) - 1)

   def binarySearchCircularArrayDuplicatesHelper(self, A, l, r):
      if l == r: return l
      mid = l + ((r - l) >> 1)
      if A[mid] > A[r]:
         return self.binarySearchCircularArrayDuplicatesHelper(A, mid + 1, r)
      elif A[mid] < A[r]:
         return self.binarySearchCircularArrayDuplicatesHelper(A, l, mid)
      else:
         l_res = self.binarySearchCircularArrayDuplicatesHelper(A, l, mid)
         r_res = self.binarySearchCircularArrayDuplicatesHelper(A, mid + 1, r)
         return r_res if A[r_res] < A[l_res] else l_res

if __name__ == "__main__":
   A = [4, 5, 6, 1, 2, 3]
   B = [4, 4, 5, 6, 1, 1, 2, 3]
   t = Solution()
   print t.binarySearchCircularArray(A)
   print t.binarySearchCircularArrayDuplicates(B)
