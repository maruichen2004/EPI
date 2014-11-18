import sys

class Solution:
   # Time: O(nlogk)
   # Space: O(k)
   def findMinDistanceSortedArrays(self, arrays):
      idx = [0] * len(arrays)
      minDis = sys.maxint
      currentHeads = []
      for i in range(len(arrays)):
         if idx[i] >= len(arrays[i]):
            return minDis
         if (i, arrays[i][idx[i]]) not in currentHeads:
            currentHeads.append((i, arrays[i][idx[i]]))
      while True:
         minDis = min(minDis, currentHeads[-1][1] - currentHeads[0][1])
         tar = currentHeads[0][0]
         idx[tar] += 1
         if idx[tar] >= len(arrays[tar]):
            return minDis
         currentHeads = currentHeads[1:]
         if (tar, arrays[tar][idx[tar]]) not in currentHeads:
            currentHeads.append((tar, arrays[tar][idx[tar]]))

if __name__ == "__main__":
   arrays = [[1, 2, 3, 4, 5, 8], [3, 4, 5, 6, 7], [5, 6, 6, 7, 8, 9, 11]]
   t = Solution()
   print t.findMinDistanceSortedArrays(arrays)
