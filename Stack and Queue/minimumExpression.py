from collections import deque

class Solution:
   def minimumExpression(self, n):
      if n == 1: return [1]
      queue = deque()
      queue.append([1])
      while queue:
         cur = queue.popleft()
         for num in cur:
            sum = num + cur[-1]
            if sum > n: break
            next = cur
            next.append(sum)
            if sum == n: return next
            queue.append(next)

if __name__ == "__main__":
   t = Solution()
   print t.minimumExpression(15)
