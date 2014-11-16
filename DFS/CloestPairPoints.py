import sys

class Point:
   def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

class Solution:
   # Time: O(nlogn)
   # Space: O(logn)
   def cloestPairPoints(self, points):
      res = self.cloestPairPointsHelper(points.sort(key=lambda f:f.x), 0, len(points))
      return (res[0], res[1])

   def cloestPairPointsHelper(self, points, l, r):
      if r - l <= 3: return self.bruteForce(points, l, r)
      mid = l + ((r - l) >> 1)
      lres = self.cloestPairPointsHelper(points, l, mid)
      rres = self.cloestPairPointsHelper(points, mid, r)
      minlr = lres if lres[2] < rres[2] else rres
      remain = []
      for p in points:
         if abs(p.x - points[mid].x) < minlr[2]: remain.append(p)
      midres = self.cloestPairPointsInRemain(remain, minlr[2])
      return midres if midres[2] < minlr[2] else minlr

   def bruteForce(self, points, l, r):
      res = (Point(), Point(), sys.float_info.max)
      for i in range(l, r):
         for j in range(i+1, r):
            dis = self.distance(points[i], points[j])
            if dis < res[2]: res = (points[i], points[j], dis)
      return res

   def cloestPairPointsInRemain(self, points, d):
      points.sort(key=lambda f: f.x)
      res = (Point(), Point(), sys.float_info.max)
      for i in range(len(points)):
         for j in range(i+1, len(points)):
            dis = self.distance(points[i], points[j])
            if dis < res[2]: res = (points[i], points[j], dis)
      return res

   def distance(self, a, b):
      return math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))
