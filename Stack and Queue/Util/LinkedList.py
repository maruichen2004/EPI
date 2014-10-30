from random import randint

class ListNode:
   def __init__(self, value):
      self.val = value
      self.next = None

class LinkedList:
   def __init__(self, num, l=1, r=100, sorted=False):
      if num <= 0: self.head = None
      else:
         vals = [randint(l, r) for i in range(num)]
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

class RandomListNode:
   def __init__(self, value):
      self.val = value
      self.next = None
      self.random = None
      self.order = -1

class RandomLinkedList:
   def __init__(self, num, l=1, r=100, sorted=False):
      if num <= 0: self.head = None
      else:
         vals = [randint(l, r) for i in range(num)]
         if sorted == True: vals.sort()
         nodes = [RandomListNode(vals[i]) for i in range(num)]
         for i in range(num - 1): nodes[i].next = nodes[i+1]
         self.head = nodes[0]

   def display(self):
      cur = self.head
      while cur:
         print cur.val, "[" + str(cur.order) + "]",
         if cur.random: print "(" + str(cur.random.val) + ")", 
         cur = cur.next
      print "\n"

   def getHead(self):
      return self.head

   def connect(self, n1, n2):
      front, end = self.head, self.head
      for i in range(n1): front = front.next
      for i in range(n2): end = end.next
      front.random = end
