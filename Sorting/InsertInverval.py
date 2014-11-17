class Solution:
   # Time: O(n)
   # Space: O(1)
   def insertInterval(self, intervals, newInterval):
      i = 0
      while i < len(intervals):
         if newInterval[0] > intervals[i][1]:
            i += 1
         elif newInterval[1] < intervals[i][0]:
            intervals.insert(i, newInterval)
            return
         else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            intervals.remove(intervals[i])
      intervals.append(newInterval)

if __name__ == "__main__":
   intervals = [[0, 2], [3, 6], [7, 7], [9, 12]]
   newInterval = [1, 8]
   t = Solution()
   t.insertInterval(intervals, newInterval)
   print intervals
