import heapq

class Solution:
   # Time: O(nlogk)
   # Space: O(n)
   def cloestToMedian(self, A, k):
      median = self.findMedian(A)
      return heapq.nsmallest(k, A, key=lambda x: abs(x - median))

   def findMedian(self, A):
      half = len(A) / 2
      if len(A) & 1 == 1:
         res = heapq.nsmallest(half + 1, A)[-1]
      else:
         res = 0.5 * (heapq.nsmallest(half + 1, A)[-1] + heapq.nsmallest(half, A)[-1])
      return res

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9, 2, 4, 6, 8]
   k = 4
   t = Solution()
   print t.cloestToMedian(A, k)
