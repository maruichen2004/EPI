class Solution:
   # Time: O(n * sumA)
   # Space: O(sumA)
   def minSubarrayDifference(self, A):
      sumA = sum(A)
      dp = set()
      dp.add(0)
      for a in A:
         for i in reversed(range(a, (sumA >> 1) + 1)):
            if i - a in dp: dp.add(i)
      for i in reversed(range((sumA >> 1) + 1)):
         if i in dp: return (sumA - i) - i
      return sumA

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9, 2, 4, 6, 8, 4]
   t = Solution()
   print t.minSubarrayDifference(A)
