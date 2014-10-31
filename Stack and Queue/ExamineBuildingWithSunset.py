class Solution:
   # Time: O(n)
   # Space: O(n)
   def examineBuildingWithSunset(self, heights):
      stack = []
      for height in heights:
         if len(stack) == 0: stack.append(height)
         elif height < stack[-1]: stack.append(height)
         else:
            while len(stack) > 0 and stack[-1] <= height:
               stack.pop()
            stack.append(height)
      return stack

if __name__ == "__main__":
   heights = [1, 2, 5, 3, 4]
   t = Solution()
   print t.examineBuildingWithSunset(heights)
