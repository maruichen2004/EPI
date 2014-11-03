class Solution:
   # Time: O(n)
   # Space: O(1)
   def jumpGame(self, A):
      reachable = 0
      for i in range(len(A)):
         if reachable < i: return False
         reachable = max(reachable, i + A[i])
      return True

   def minJumpNumber(self, A):
      maxCanReach, jumpNum = 0, 0
      while True:
         jumpNum += 1
         for i in range(maxCanReach + 1):
            maxCanReach = max(maxCanReach, i + A[i])
            if maxCanReach >= len(A) - 1: return jumpNum

if __name__ == "__main__":
   A = [2, 3, 1, 1, 4]
   t = Solution()
   print t.jumpGame(A)
   print t.minJumpNumber(A)
