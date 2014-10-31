class CircularQueue:
   def __init__(self, cap):
      self.cap = cap
      self.data = [0] * self.cap
      self.head = 0
      self.tail = 0
      self.count = 0

   # Time: O(1)
   def enQueue(self, x):
      if self.count == self.cap:
         self.data += [0] * self.cap
         self.cap *= 2
         self.head = 0
         self.tail = self.count
      self.data[self.tail] = x
      self.tail = (self.tail + 1) % len(self.data)
      self.count += 1

   # Time: O(1)
   def deQueue(self):
      if self.count == 0:
         print "empty queue"
      else:
         self.count -= 1
         val = self.data[self.head]
         self.head = (self.head + 1) % len(self.data)
         return val

   # Time: O(1)
   def size(self): return self.count

if __name__ == "__main__":
   queue = CircularQueue(2)
   for i in range(6):
      queue.enQueue(i)
   for i in range(6):
      print queue.deQueue()
