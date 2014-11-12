import heapq

class Solution:
   # Time: O(n + mlogk)
   # Space: O(c + k) c is the number of distinct strings
   def kFrequentestStrs(self, strsi, k):
      map, heap, res = {}, [], []
      for s in strs:
         if s not in map: map[s] = 1
         else: map[s] += 1
      for i in range(k):
         heap.append((-map[strs[i]],strs[i]))
      heapq.heapify(heap)
      for item in map:
         if -map[item] < heapq.nsmallest(1, heap)[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (-map[item], item))
      for item in heap:
         res.append(item[1])
      return res

if __name__ == "__main__":
   strs = ["abc", "def", "abc", "ghi", "abc", "def"]
   t = Solution()
   print t.kFrequentestStrs(strs, 2)
