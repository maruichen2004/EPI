class Solution:
   # Time: O(n^2)
   # Space: O(n) call stack
   def sortStack(self, stack):
      if len(stack) > 0:
         e = stack.pop()
         self.sortStack(stack)
         self.insertStack(stack, e)

   def insertStack(self, stack, e):
      if len(stack) == 0 or stack[-1] < e:
         stack.append(e)
      else:
         f = stack.pop()
         self.insertStack(stack, e)
         stack.append(f)

if __name__ == "__main__":
   stack = [1, 3, 2, 4, 6, 5]
   t = Solution()
   t.sortStack(stack)
   print stack
