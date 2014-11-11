class Solution:
   # Time: O(len(s))
   # Space: O(1)
   def decode(self, s):
      count = 0
      res = ""
      for ch in s:
         if ch.isdigit(): count = count * 10 + (ord(ch) - ord("0"))
         else:
            for i in range(count): res += ch
            count = 0
      return res

   # Time: O(len(s))
   # Space: O(1)
   def encode(self, s):
      count = 1
      res = ""
      for i in range(1, len(s) + 1):
         if i == len(s) or s[i] != s[i-1]:
            res += str(count)
            res += s[i-1]
            count = 1
         else:
            count += 1
      return res

if __name__ == "__main__":
   s = "aaaaaaaaaaffffee"
   t = Solution()
   x = t.encode(s)
   print x, t.decode(x)
