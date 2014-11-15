class Solution:
   # Time: O(2^n)
   # Space: O(n)
   def hanoi(self, n, p1, p2, p3):
      return self.hanoiHelper(n, p1, p2, p3)

   def hanoiHelper(self, n, src, dst, use):
      if n == 1:
         dst.append(src.pop())
         return 1
      else:
         count = self.hanoiHelper(n-1, src, use, dst)
         dst.append(src.pop())
         count += 1
         count += self.hanoiHelper(n-1, use, dst, src)
         return count

if __name__ == "__main__":
   t = Solution()
   n = 4
   p1, p2, p3 = [i+1 for i in range(n)], [], []
   print p1, p2, p3
   print t.hanoi(n, p1, p2, p3)
   print p1, p2, p3
