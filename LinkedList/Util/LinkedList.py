from random import randint

class ListNode:
   def __init__(self, value):
      self.val = value
      self.next = None

class LinkedList:
   def __init__(self, num, sorted=False):
      if num <= 0: self.head = None
      else:
         vals = [randint(1, 100) for i in range(num)]
         if sorted == True: vals.sort()
         nodes = [ListNode(vals[i]) for i in range(num)]
         for i in range(num - 1): nodes[i].next = nodes[i+1]
         self.head = nodes[0]

   def display(self):
      cur = self.head
      while cur:
         print cur.val, 
         cur = cur.next
      print "\n"

   def getHead(self):
      return self.head

   def createCycle(self, n):
      head = self.head
      for i in range(n - 1): head = head.next
      print head.val, 
      cur = head
      while cur.next: cur = cur.next
      cur.next = head
