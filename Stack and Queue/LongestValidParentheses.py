class Solution:
   # Time: O(n)
   # Space: O(n)
   def longestValidParentheses(self, s):
      stack, longest, last = [], 0, 0
      for i in range(len(s)):
         if s[i] == "(": stack.append(i)
         elif len(stack) == 0: last = i + 1
         else:
            stack.pop()
            if len(stack) == 0: longest = max(longest, i - last + 1)
            else: longest = max(longest, i - stack[-1])
      return longest

if __name__ == "__main__":
   tests = ["((()))(", "()()(",")()()", "()())()", "()((())"]
   t = Solution()
   for test in tests:
      print test, t.longestValidParentheses(test)
