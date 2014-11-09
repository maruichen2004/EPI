class Solution:
   # Time: O(logn)
   # Search: O(1)
   def binarySearchAiEqI(self, A):
      l, r = 0, len(A) - 1
      while l <= r:
         mid = l + ((r - l) >> 1)
         val = A[mid] - mid
         if val == 0: return mid
         elif val > 0: r = mid - 1
         else: l = mid + 1
      return -1

if __name__ == "__main__":
   A = [-2, -1, 0, 3, 7, 8]
   t = Solution()
   print t.binarySearchAiEqI(A)
