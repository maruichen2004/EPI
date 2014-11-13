class Solution:
   # Time:
   # Space:
   def collatzConjecture(self, n):
      table = set()
      for i in range(2, n + 1):
         sequence = set()
         cur = i
         while cur >= i:
            if cur in sequence: return False
            sequence.add(cur)
            if cur & 1 == 1:
               if cur in table: break
               table.add(cur)
               next = cur * 3 + 1
               cur = next
            else: cur >>= 1
         if i in table: table.remove(i)
      return True

if __name__ == "__main__":
   n = 20
   t = Solution()
   print t.collatzConjecture(n)
