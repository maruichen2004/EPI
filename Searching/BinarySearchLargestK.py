class Solution:
   # Time: O(logn)
   # Space: O(1)
   def binarySearchLargestK(self, A, k):
      l, r, res = 0, len(A) - 1, -1
      while l <= r:
         mid = l + ((r - l) >> 1)
         if A[mid] > k: res, r = mid, mid - 1
         else: l = mid + 1
      return res

   def binarySearchForARange(self, A, k):
      l, r, res = 0, len(A) - 1, [-1, -1]
      while l < r:
         mid = l + ((r - l) >> 1)
         if A[mid] > k: r = mid - 1
         elif A[mid] == k: r = mid
         else: l = mid + 1
      if A[l] != k: return res
      res[0] = l
      r = len(A) - 1
      while l < r:
         mid = l + ((r - l) >> 1)
         if A[mid] == k: l = mid
         else: r = mid - 1
      res[1] = l
      return res

if __name__ == "__main__":
   A = [1, 1, 2, 3, 3, 3, 4, 5]
   k = 3
   t = Solution()
   print t.binarySearchLargestK(A, k)
   print t.binarySearchForARange(A, k)
