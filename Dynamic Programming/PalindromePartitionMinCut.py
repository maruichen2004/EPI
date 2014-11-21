class Solution:
   # Time: O(n^2)
   # Space: O(n^2)
   def minCut(self, s):
      isPalindrome = [[False for i in range(len(s))] for j in range(len(s))]
      T = [len(s) - 1 - i for i in range(len(s) + 1)]
      for i in reversed(range(len(s))):
         for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 2 or isPalindrome[i+1][j-1]):
               isPalindrome[i][j] = True
               T[i] = min(T[i], 1 + T[j+1])
      return T[0]

if __name__ == "__main__":
   t = Solution()
   print t.minCut("aab")
   print t.minCut("bb")
   print t.minCut("cabababcbc")
   print t.minCut("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj")
