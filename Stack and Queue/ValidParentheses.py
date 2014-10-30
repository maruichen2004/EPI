class Solution:
   # Time: O(n)
   # Space: O(n)
   def validParentheses(self, s):
      stack = []
      for i in s:
         if i in "{[(": stack.append(i)
         else:
            if len(stack) == 0: return False
            elif (i == "(" and stack[-1] != ")") or \
                 (i == "{" and stack[-1] != "}") or \
                 (i == "[" and stack[-1] != "]"):
               return False
            else: stack.pop()
      return len(stack) == 0

if __name__ == "__main__":
   tests = ["(){}[]", "({[]})", "({})[]", "{()[]}", "){}[]", "{})[]"]
   t = Solution()
   for test in tests:
      print test, t.validParentheses(test)
