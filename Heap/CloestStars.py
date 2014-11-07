import heapq

class Star:
   def __init__(self, id, x, y, z):
      self.x = x
      self.y = y
      self.z = z
      self.id = id

   def distance(self):
      return self.x * self.x + self.y * self.y + self.z * self.z

   def getid(self):
      return self.id

class Solution:
   # Time: O(nlogk)
   # Space: O(k)
   def cloestStars(self, stars, k):
      heap, res = [], []
      for i in range(k):
         heap.append((-stars[i].distance(), stars[i]))
      heapq.heapify(heap)
      for i in range(k, len(stars)):
         if -stars[i].distance() > heapq.nsmallest(1, heap)[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (-stars[i].distance(), stars[i]))
      for item in heap: res.append(item[1].id)
      return res

if __name__ == "__main__":
   stars = [Star(i, i, i, i) for i in range(10)]
   k = 5
   t = Solution()
   print t.cloestStars(stars, k)
