from collections import deque
class QueueWithMax:
   def __init__(self):
      self.Q = deque()
      self.D = deque()

   # Time: O(1)
   def enQueue(self, x):
      self.Q.append(x)
      if self.D:
         while self.D and self.D[-1] < x:
            self.D.pop()
      self.D.append(x)

   # Time: O(1)
   def deQueue(self):
      if len(self.Q) != 0:
         val = self.Q.popleft()
         if val == self.D[0]:
            self.D.popleft()
         return val
      print "empty queue"

   # Time: O(1)
   def maxval(self):
      return self.D[0]

if __name__ == "__main__":
   queue = QueueWithMax()
   queue.enQueue(1)
   print queue.maxval()
   queue.enQueue(3)
   print queue.maxval()
   queue.enQueue(2)
   print queue.maxval()
   queue.enQueue(4)
   print queue.maxval()

   queue.deQueue()
   print queue.maxval()
   queue.deQueue()
   print queue.maxval()
   queue.deQueue()
   print queue.maxval()
