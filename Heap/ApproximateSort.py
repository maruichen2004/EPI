import heapq

class Solution:
   # Time: O(nlogk)
   # Space: O(k)
   def approximateSort(self, A, k):
      heap, res = [], []
      for i in range(k):
         heap.append(A[i])
      heapq.heapify(heap)
      for i in range(k, len(A)):
         heapq.heappush(heap, A[i])
         cur = heapq.heappop(heap)
         res.append(cur)
      while heap:
         cur = heapq.heappop(heap)
         res.append(cur)
      return res

if __name__ == "__main__":
   A = [3, 2, 1, 5, 4, 6, 8, 7, 9]
   k = 3
   t = Solution()
   print t.approximateSort(A, k)
