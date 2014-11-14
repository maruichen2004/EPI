class Solution:
   # Time:
   # Space:
   def palindromePartition(self, s):
      res = []
      self.palindromePartitionHelper(res, [], s, 0)
      return res

   def palindromePartitionHelper(self, res, cur, s, i):
      if i == len(s): res.append(cur)
      else:
         for j in range(i, len(s)):
            if self.isPalindrome(s[i:j+1]):
               self.palindromePartitionHelper(res, cur + [s[i:j+1]], s, j+1)

   def isPalindrome(self, s):
      for i in range(len(s)/2):
         if s[i] != s[-(i+1)]:
            return False
      return True

if __name__ == "__main__":
   s = "aabccd"
   t = Solution()
   print t.palindromePartition(s)
