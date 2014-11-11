class Solution:
   # Time: O(len(s))
   # Space: O(1)
   def romanToInt(self, s):
      singleTable = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
      doubleTable = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
      res, i = 0, 0
      while i < len(s):
         if i + 1 < len(s) and s[i:i+2] in doubleTable:
            res += doubleTable[s[i:i+2]]
            i += 2
         elif i < len(s) and s[i] in singleTable:
            res += singleTable[s[i]]
            i += 1
         else:
            return -1
      return res

   def intToRoman(self, x):
      transTable = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
      res = ""
      for trans in sorted(transTable.keys())[::-1]:
         while x >= trans:
            res += transTable[trans]
            x -= trans
         if x == 0: break
      simplifyTable = {"DCCCC":"CM", "CCCC":"CD", "LXXXX":"XC", "XXXX":"XL", "VIIII":"IX", "IIII":"IV"}
      simplifyContent = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]
      for item in simplifyContent:
         if item in res:
            res = res.replace(item, simplifyTable[item])
      return res

if __name__ == "__main__":
   s = "CLXXXIV"
   t = Solution()
   x = t.romanToInt(s)
   print x, t.intToRoman(x)
