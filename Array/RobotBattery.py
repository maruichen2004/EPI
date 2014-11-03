import sys
class Solution:
   # Time: O(n)
   # Space: O(1)
   def robotBattery(self, heights):
      min_height, capacity = sys.maxint, 0
      for height in heights:
         min_height = min(min_height, height)
         capacity = max(capacity, height - min_height)
      return capacity

if __name__ == "__main__":
   heights = [1, 2, 3, 4, 5, 6, 7]
   t = Solution()
   print t.robotBattery(heights)
