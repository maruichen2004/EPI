class Stack:
   def __init__(self):
      self.s = []

   def pop(self):
      if len(self.s) == 0:
         print "empty stack"
      else:
         val = self.s[-1][0]
         self.s.pop()
         return val

   def push(self, x):
      if len(self.s) == 0:
         self.s.append((x, x))
      else:
         self.s.append((x, max(x, self.s[-1][1])))

   def maxval(self):
      if len(self.s) == 0:
         print "empty stack"
      else:
         return self.s[-1][1]

if __name__ == "__main__":
   stack = Stack()
   stack.push(1)
   print stack.maxval()
   stack.push(2)
   print stack.maxval()
   stack.push(4)
   print stack.maxval()
   stack.push(3)
   print stack.maxval()
   stack.push(5)
   print stack.maxval()

   for i in range(5):
      print stack.pop(), stack.maxval()
