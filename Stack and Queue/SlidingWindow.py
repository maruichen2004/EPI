from collections import deque

class QueueWithMax:
   def __init__(self):
      self.Q = deque()
      self.D = deque()

   def enQueue(self, x):
      self.Q.append(x)
      while self.D and self.D[-1] < x:
         self.D.pop()
      self.D.append(x)

   def deQueue(self):
      if self.Q:
         val = self.Q.popleft()
         if val == self.D[0]:
            self.D.popleft()
         return val
      print "empty queue"

   def maxval(self):
      if self.Q: return self.D[0]
      print "empty queue"

   def front(self):
      return self.Q[0]

class Solution:
   # Time: O(n)
   # Space: O(n)
   def slidingWindow(self, A, w):
      res, queue = [], QueueWithMax()
      for v, t in A:
         queue.enQueue((v, t))
         while t - queue.front()[1] > w:
            queue.deQueue()
         res.append(queue.maxval())
      return res

if __name__ == "__main__":
   A = [(1, 1), (2, 3), (6, 4), (5, 5), (4, 6)]
   w = 2
   t = Solution()
   print t.slidingWindow(A, w)
