import sys

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

class Solution:
   # Time: O(n^2)
   # Space: O(n)
   def lineMostPoints(self, points):
      k, b, p, maxsum = 0, 0, Point(0, 0), 0
      for i in range(len(points)):
         slopemap, same, inf, curmax, curs = {}, 1, 0, 0, 0
         start = points[i]
         for j in range(i+1, len(points)):
            end = points[j]
            if start.x == end.x and start.y == end.y:
               same += 1
            elif start.x == end.x:
               inf += 1
            else:
               slope = 1.0 * (start.y - end.y) /  (start.x - end.x)
               if slope not in slopemap:
                  slopemap[slope] = 1
               else:
                  slopemap[slope] += 1
         for slope in slopemap:
            if same + slopemap[slope] > curmax:
               curs, curmax = slope, same + slopemap[slope]
         if same + inf > curmax and same + inf > maxsum:
            k, maxsum = sys.maxint, same + inf
         elif curmax > same + inf and curmax > maxsum:
            k, b, maxsum = curs, start.y - k * start.x, curmax
      return (k, b) if k != sys.maxint else (k, None)

if __name__ == "__main__":
   points = [Point(i, i) for i in range(10)]
   points += [Point(i, 10) for i in range(30)]
   t = Solution()
   print t.lineMostPoints(points)
