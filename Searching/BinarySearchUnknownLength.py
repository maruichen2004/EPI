class Solution:
   # Time: O(logn)
   # Space: O(1)
   def binarySearchUnknowLength(self, A, k):
      p = 0
      while True:
         try:
            val = A[(1 << p) - 1]
            if val == k: return (1 << p) - 1
            elif val > k: break
         except IndexError:
            break
         p += 1
      l, r = max(0, 1 << (p - 1)), (1 << p) - 2
      while l <= r:
         try:
            mid = l + ((r - l) >> 1)
            if A[mid] == k: return mid
            elif A[mid] > k: r = mid - 1
            else: l = mid + 1
         except:
            r = mid - 1
      return -1

if __name__ == "__main__":
   A = [i * 2 + 1 for i in range(35)]
   k = 9
   t = Solution()
   print t.binarySearchUnknowLength(A, k)
