class Solution:
   # Time: O(4^n)
   # Space: O(4^n)
   def phoneMnemonic(self, digits):
      lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
      res = []
      self.phoneMnemonicHelper(res, "", lookup, digits)
      return res

   def phoneMnemonicHelper(self, res, cur, lookup, digits):
      if len(digits) == 0:
         res.append(cur)
      else:
         for letter in lookup[int(digits[0])]:
            self.phoneMnemonicHelper(res, cur + letter, lookup, digits[1:])

if __name__ == "__main__":
   digits = "23"
   t = Solution()
   print t.phoneMnemonic(digits)
