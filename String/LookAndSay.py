class Solution:
   # Time:
   # Space:
   def lookAndSay(self, n):
      res = "1"
      for i in range(1, n):
         j, next = 0, ""
         while j < len(res):
            count = 1
            while j + 1 < len(res) and res[j] == res[j+1]:
               j, count = j + 1, count + 1
            next += "{0}{1}".format(count, res[j])
            j += 1
         res = next
      return res

if __name__ == "__main__":
   n = 5
   t = Solution()
   print t.lookAndSay(n)
