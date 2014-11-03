class Solution:
   # Time:
   # Space:
   def applyPermutation(self, A, perm):
      for i in range(len(perm)):
         if perm[i] >= 0:
            a, tmp = i, A[i]
            while True:
               nextA = perm[a]
               nextTmp = A[nextA]
               A[nextA] = tmp
               perm[a] -= len(perm)
               a, tmp = nextA, nextTmp
               if a == i: break
      for i in range(len(perm)):
         perm[i] += len(perm)

if __name__ == "__main__":
   A = [0, 1, 2, 3]
   perm = [2, 0, 1, 3]
   t = Solution()
   t.applyPermutation(A, perm)
   print A
