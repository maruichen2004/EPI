from random import randint
class Solution:
   # Time: O(n)
   # Space: O(k)
   def onlineSampling(self, A, k):
      res = []
      for i in range(k):
         res.append(k)
      idx = k + 1
      for i in range(k, len(A)):
         r = randint(0, idx)
         idx += 1
         if r < k: res[r] = A[i]
         print res

if __name__ == "__main__":
   A = [i for i in range(10)]
   k = 3
   t = Solution()
   t.onlineSampling(A, k)   
