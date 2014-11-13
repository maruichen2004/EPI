class Solution:
   # Time: O(n)
   # Space: O(m) m is the length of result
   def longestSubarrayWithDistinctEntries(self, A):
      maxlen, subarray, end = 0, [], 0
      for start in range(len(A)):
         if A[start] not in subarray: subarray.append(A[start])
         else:
            maxlen = max(maxlen, len(subarray))
            while A[end] != A[start]: end += 1
            end += 1
            subarray = A[end:start+1]
      maxlen = max(maxlen, len(subarray))
      return maxlen

if __name__ == "__main__":
   A = [1, 3, 5, 1, 3, 1, 3, 5, 2, 4, 7]
   t = Solution()
   print t.longestSubarrayWithDistinctEntries(A)
