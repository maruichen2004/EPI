from random import randint
class Solution:
   # Time: O(k)
   # Space: O(k)
   def randomSubset(self, A, k):
      map = {}
      for i in range(k):
         l = len(A) - 1 - i
         r = randint(0, l)
         if r not in map and l not in map:
            map[r] = l
            map[l] = r
         elif r in map and l not in map:
            map[l] = map[r]
            map[r] = l
         elif r not in map and l in map:
            map[r] = map[l]
            map[l] = r
         else:
            map[l], map[r] = map[r], map[l]
      res = []
      for i in range(k):
         res.append(map[len(A) - 1 - i])
      return res

if __name__ == "__main__":
   A = [1, 2, 3, 4]
   k = 2
   t = Solution()
   print t.randomSubset(A, k)
