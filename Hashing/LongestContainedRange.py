class Solution:
   # Time: O(n^2)
   # Space: O(n)
   def longestContainedRange(self, A):
      dict = {x:False for x in A}
      maxlen, res = -1, [0, 0]
      for i in dict:
         if dict[i] == False:
            start, end = i, i
            cur, len1 = i + 1, 1
            while cur in dict:
               dict[cur] = True
               end = cur
               cur, len1 = cur + 1, len1 - 1
            cur, len2 = i - 1, 1
            while cur in dict:
               dict[cur] = True
               start = cur
               cur, len2 = cur - 1, len2 + 1
            if end - start + 1 > maxlen:
               maxlen = end - start + 1
               res = [start, end]
      return res

if __name__ == "__main__":
   A = [-3, -2, 9, 0, 2, 3, -1]
   t = Solution()
   print t.longestContainedRange(A)
