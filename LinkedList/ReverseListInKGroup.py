from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def reverseK(self, head, k):
      if head is None or head.next is None:
         return head
      dummy = ListNode(0)
      dummy.next = head
      prev = dummy
      while True:
         begin, end = prev.next, prev
         for i in range(k):
            end = end.next
            if end is None: return dummy.next
         newStart = end.next
         self.reverse(begin, end)
         prev.next = end
         begin.next = newStart
         prev = begin

   def reverse(self, start, end):
      prev, cur = start, start
      next = start.next
      while cur is not end:
         cur = next
         next = next.next
         cur.next = prev
         prev = cur

if __name__ == "__main__":
   l1 = LinkedList(10)
   l1.display()
   t = Solution()
   l2 = t.reverseK(l1.getHead(), 4)
   cur = l2
   while cur:
      print cur.val, 
      cur = cur.next
   print "\n"
