class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def renderCalendar(self, A):
      endpoints = []
      for start, end in A:
         endpoints.append((start, True))
         endpoints.append((end, False))
      endpoints.sort(key=lambda x: x[0])
      max_count, count = 0, 0
      for time, isStart in endpoints:
         if isStart:
            count += 1
            max_count = max(count, max_count)
         else:
            count -= 1
      return max_count

if __name__ == "__main__":
   A = [[1, 5], [6, 10], [11, 13], [14, 15], [2, 7], [8, 9], [12, 15], [4, 5], [9, 17]]
   t = Solution()
   print t.renderCalendar(A)
