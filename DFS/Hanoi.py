class Solution:
   # Time: O(2^n)
   # Space: O(n)
   def hanoi(self, n):
      p1, p2, p3 = [i+1 for i in range(n)], [], []
      return self.hanoiHelper(n, p1, p2, p3)

   def hanoiHelper(self, n, src, dst, use):
      if n > 1:
         count = self.hanoiHelper(n-1, src, use, dst)
         dst.append(src.pop())
         count += 1
         count += self.hanoiHelper(n-1, dst, use, src)
         return count
      return 1

if __name__ == "__main__":
   t = Solution()
   n = 4
   print t.hanoi(n)
