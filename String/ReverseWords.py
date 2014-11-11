class Solution:
   # Time: O(len(s))
   # Space: O(1)
   def reverseWords(self, s):
      word, res = "", ""
      for i in range(len(s)):
         if s[i] != " ": word += s[i]
         else:
            if len(word) != 0:
               if len(res) != 0: res = " " + res
               res = word + res
               word = ""
      if len(word) != 0:
         if len(res) != 0: res = " " + res
         res = word + res
      return res

if __name__ == "__main__":
   s1 = "Elements of Programming Interviews"
   s2 = "Hello"
   t = Solution()
   print t.reverseWords(s2)
