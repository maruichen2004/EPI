class Solution:
   # Time: O(n*3^n)
   # Space: O(n)
   def synthesizeExpression(self, s, k):
      operators, operands, res = [], [], []
      self.synthesizeExpressionHelper(s, k, 0, 0, operators, operands, res)
      return res

   def synthesizeExpressionHelper(self, s, k, cur, i, operators, operands, res):
      cur = cur * 10 + int(s[i])
      if i == len(s) - 1:
         if self.evaluate(operands + [cur], operators) == k:
            tmp = ""
            for i in range(len(operators)):
               tmp += str(operands[i]) + operators[i]
            tmp += str(cur)
            res.append(tmp)
      else:
         self.synthesizeExpressionHelper(s, k, cur, i+1, operators, operands, res)
         if k - self.evaluate(operands + [cur], operators) <= int(s[i+1:]):
            self.synthesizeExpressionHelper(s, k, 0, i+1, operators + ["+"], operands + [cur], res)
         self.synthesizeExpressionHelper(s, k, 0, i+1, operators + ["*"], operands + [cur], res)

   def evaluate(self, operands, operators):
      i = 0
      for oper in operators:
         if oper == "*":
            product = operands[i]
            operands.remove(operands[i])
            product *= operands[i]
            operands[i] = product
         else:
            i += 1
      return sum(operands)

if __name__ == "__main__":
   s = "1232537859"
   k = 995
   t = Solution()
   print t.synthesizeExpression(s, k)
