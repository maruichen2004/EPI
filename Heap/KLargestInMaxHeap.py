import heapq

class Solution:
   # Time: O(klogk)
   # Space: O(k)
   def kLargestInMaxHeap(self, A, k):
      maxHeap, res = [(-A[0], 0)], []
      for i in range(k):
         tmp = heapq.heappop(maxHeap)
         res.append(-tmp[0])
         left, right = (tmp[1] << 1) + 1, (tmp[1] << 1) + 2
         if left < len(A):
            heapq.heappush(maxHeap, (-A[left], left))
         if right < len(A):
            heapq.heappush(maxHeap, (-A[right], right))
      return res

if __name__ == "__main__":
   A = [9, 7, 8, 3, 2, 6, 5]
   k = 5
   t = Solution()
   print t.kLargestInMaxHeap(A, k)
