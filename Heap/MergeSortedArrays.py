import heapq

class Solution:
   # Time: O(nlogk)
   # Space: O(k)
   def mergeSortedArrays(self, arrays):
      indices, heap, res = [1] * len(arrays), [], []
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
   arrays = [[1, 5, 9, 13, 17], [2, 6, 10, 14, 21], [3, 7, 11, 15, 22], [4, 8, 12, 16, 23]]
   t = Solution()
   print t.mergeSortedArrays(arrays)
