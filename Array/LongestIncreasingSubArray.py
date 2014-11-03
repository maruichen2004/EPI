class Solution:
   # Time: worst O(n), best O(max(n/L, L)) L is the length of longest increasing subarray
   # Space: O(1)
   def longestIncreasingSubArray(self, A):
      i, maxlen, res = 0, 1, (0, 0)
      while i < len(A):
         skippable = False
         for j in reversed(range(i, i + maxlen)):
            if j + 1 >= len(A) or A[j] >= A[j+1]:
               i = j + 1
               skippable = True
               break
         if skippable == False:
            i += maxlen - 1
            while i + 1 < len(A) and A[i] < A[i+1]:
               i, maxlen = i + 1, maxlen + 1
            res = (i - maxlen + 1, i)
      return res

if __name__ == "__main__":
   A = [4, 2, 1, 3, 5]
   t = Solution()
   print t.longestIncreasingSubArray(A)
