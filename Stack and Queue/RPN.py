import operator

class Solution:
   # Time: O(n)
   # Space: O(n)
   def eval(self, s):
      tokens = s.split(",")
      stack = []
      operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
      for token in tokens:
         if token.isdigit() or token[1:].isdigit():
            stack.append(int(token))
         else:
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(operators[token](n2 * 1.0, n1))
      return stack[-1]

if __name__ == "__main__":
   s = "3,4,+,11,6,-,*"
   t = Solution()
   print t.eval(s)
