from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time:
   # Space:
   def overlappingLists(self, l1, l2):
      c1, c2 = self.hasCycle(l1), self.hasCycle(l2)
      if c1 is None and c2 is None:
         return self.overlappingNoCycleLists(l1, l2)
      elif c1 and c2:
         if c1 == c2: return c1
         cur = c1.next
         while cur != c1:
            if cur == c2: return c1, c2
            cur = cur.next
         return None
      else: return None

   def hasCycle(self, head):
      if head is None: return None
      fast, slow = head, head
      while fast and fast.next:
         fast = fast.next.next
         slow = slow.next
         if fast == slow:
            slow = head
            while slow != fast:
               fast, slow = fast.next, slow.next
            return slow
      return None

   def overlappingNoCycleLists(self, l1, l2):
      h1, h2, len1, len2 = l1, l2, 0, 0
      while h1: h1, len1 = h1.next, len1 + 1
      while h2: h2, len2 = h2.next, len2 + 1
      h1, h2 = l1, l2
      if len1 > len2:
         for i in range(len1 - len2): h1 = h1.next
      else:
         for i in range(len2 - len1): h2 = h2.next
      while h1 and h2 and h1 != h2:
         h1, h2 = h1.next, h2.next
      return h1

if __name__ == "__main__":
   l1 = LinkedList(8)
   l1.createCycle(3)
   l2 = LinkedList(4)
   cur = l2.getHead()
   while cur.next: cur = cur.next
   cur.next = l1.getHead().next
   t = Solution()
   print t.overlappingLists(l1.getHead(), l2.getHead())
