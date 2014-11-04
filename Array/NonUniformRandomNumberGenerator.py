import random
class Solution:
   # Time: O(n) use binary search to reduce to O(logn)
   # Space: O(n)
   def nonUniformRandomNumberGenerator(self, T, P):
      prefixP = [0.0] * (len(P) + 1)
      sum = 0.0
      for i in range(len(P)):
         sum += P[i]
         prefixP[i + 1] = sum
      tar = random.uniform(0.0, 1.0)
      l, r = 0, len(prefixP) - 1
      while l < r:
         mid = (l + r) / 2
         if prefixP[mid] < tar:   l = mid + 1
         else: r = mid
      return T[r - 1]

if __name__ == "__main__":
   T = [1, 2, 3, 4]
   P = [0.1, 0.3, 0.4, 0.2]
   t = Solution()
   print t.nonUniformRandomNumberGenerator(T, P)
