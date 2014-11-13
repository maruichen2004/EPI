class Solution:
   # Time: O(len(s) * len(L) * len(L[0]))
   # Space: O(len(L) * len(L[0]))
   def substrWithConcatenationOfAllWords(self, s, L):
      res = []
      lenS, lenL, lenW = len(s), len(L), len(L[0])
      for start in range(lenS - lenL * lenW + 1):
         listL = [s[i:i+lenW] for i in range(start, start + lenL * lenW, lenW)]
         found = True
         for item in L:
            if item in listL: listL.remove(item)
            else:
               found = False
               break
         if found == True: res.append(start)
      return res

if __name__ == "__main__":
   s = "barfoothefoobarman"
   L = ["foo", "bar"]
   t = Solution()
   print t.substrWithConcatenationOfAllWords(s, L)
