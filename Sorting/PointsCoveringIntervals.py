class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def pointsCoveringIntervals(self, intervals):
      endpoints = []
      for interval in intervals:
         endpoints.append((interval, True))
         endpoints.append((interval, False))
      endpoints.sort(key=lambda x: x[0])
      S, covered, covering = [], Set(), []
      for interval, isLeft in endpoints:
         if isLeft: covering.append(interval)
         elif interval not in covering:
            S.append(interval.[1])
            for item in covering: covered.add(item)
            covering = []
      return S
