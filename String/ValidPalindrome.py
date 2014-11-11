class Solution:
   # Time: O(len(s))
   # Space: O(1)
   def validPalindrome(self, s):
      i, j = 0, len(s) - 1
      while i < j:
         while i < j and not (s[i].isalpha() or s[i].isdigit()):
            i += 1
         while i < j and not (s[j].isalpha() or s[j].isdigit()):
            j -= 1
         if s[i].lower() != s[j].lower():
            return False
         i, j = i + 1, j - 1
      return True

if __name__ == "__main__":
   s = "abc1 d1c b a"
   t = Solution()
   print t.validPalindrome(s)
