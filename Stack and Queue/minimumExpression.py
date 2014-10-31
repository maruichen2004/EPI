from collections import deque

class Solution:
   def minimumExpression(self, n):
      if n == 1: return [1]
      queue = deque()
      queue.append([1])
      res = [1] * n
      while queue:
         cur = queue.popleft()
         for num in cur:
            sum = num + cur[-1]
            if sum > n: break
            next = cur + [sum]
            if sum == n and len(next) < len(res):
               res = next
            queue.append(next)
      return res

if __name__ == "__main__":
   t = Solution()
   print t.minimumExpression(15)
