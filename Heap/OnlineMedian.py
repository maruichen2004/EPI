import heapq

class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def onlineMedian(self, A):
      minHeap, maxHeap, res, median = [], [], [], 0
      for i in range(len(A)):
         if maxHeap and -A[i] < heapq.nsmallest(1, maxHeap)[0]:
            heapq.heappush(minHeap, A[i])
         else:
            heapq.heappush(maxHeap, -A[i])
         if len(maxHeap) > len(minHeap) + 1:
            tmp = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -tmp)
         elif len(minHeap) > len(maxHeap) + 1:
            tmp = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -tmp)
         if len(maxHeap) == len(minHeap):
            median = 0.5 * (heapq.nsmallest(1, minHeap)[0] - heapq.nsmallest(1, maxHeap)[0])
         else:
            median = heapq.nsmallest(1, minHeap)[0] if len(minHeap) > len(maxHeap) else -heapq.nsmallest(1, maxHeap)[0]
         res.append(median)
      return res

if __name__ == "__main__":
   A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   t = Solution()
   print t.onlineMedian(A)
