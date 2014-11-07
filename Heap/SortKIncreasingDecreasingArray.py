import heapq

class Solution:
   # Time: O(nlogk)
   # Space: O(n)
   def sortKIncreasingDecresingArray(self, A):
      arrays, start, increasing = [], 0, 1
      for i in range(1, len(A)):
         if (A[i-1] < A[i] and increasing == 0) or (A[i-1] >= A[i] and increasing == 1):
            if increasing == 1: arrays.append(A[start:i])
            else: arrays.append(A[i-1:start-1:-1])
            start, increasing = i, 1 - increasing
      if start < len(A):
         if increasing == 1: arrays.append(A[start:])
         else: arrays.append(A[:start-1:-1])
      indices, res, heap = [1] * len(arrays), [], []
      for i in range(len(arrays)):
         heap.append((arrays[i][0], i))
      heapq.heapify(heap)
      while heap:
         cur = heapq.heappop(heap)
         res.append(cur[0])
         idx = cur[1]
         if indices[idx] < len(arrays[idx]):
            heapq.heappush(heap, (arrays[idx][indices[idx]], idx))
            indices[idx] += 1
      return res

if __name__ == "__main__":
   A = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 7, 8, 9, 8, 7]
   t = Solution()
   print t.sortKIncreasingDecresingArray(A)
