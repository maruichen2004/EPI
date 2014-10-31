class QueueFromStacks:
   def __init__(self):
      self.A = []
      self.B = []
   # Time: O(1)
   def enQueue(self, x):
      self.A.append(x)

   # Time: O(m) m is elements in queue so far
   def deQueue(self):
      if len(self.B) == 0:
         while self.A:
            self.B.append(self.A.pop())
      if len(self.B) != 0:
         return self.B.pop()
      print "empty queue"

if __name__ == "__main__":
   queue = QueueFromStacks()
   for i in range(5):
      queue.enQueue(i)
   for i in range(5):
      print queue.deQueue()
