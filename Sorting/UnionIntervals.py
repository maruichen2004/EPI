class Solution:
   # Time: O(nlogn)
   # Space: O(m)
   def unionIntervals(self, intervals):
      intervals.sort()
      res = [intervals[0]]
      for i in range(1, len(intervals)):
         if intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
         else:
            res[-1][1] = max(res[-1][1], intervals[i][1])
      return res

if __name__ == "__main__":
   A = [[0, 3], [5, 7], [9, 11], [12, 14], [1, 1], [3, 4], [7, 8], [12, 16], [2, 4], [8, 11], [13, 13], [16, 17]]
   t = Solution()
   print t.unionIntervals(A)
