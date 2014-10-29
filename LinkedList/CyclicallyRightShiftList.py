from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def cyclicallyRightShiftList(self, head, k):
      if head is None or head.next is None: return head
      cur = head
      length = 1
      while cur.next:
         cur = cur.next
         length += 1
      k = length - k%length
      cur.next = head
      for i in range(k):
         cur =  cur.next
      newHead = cur.next
      cur.next = None
      return newHead

if __name__ == "__main__":
   l1 = LinkedList(5, 1, 5)
   l1.display()
   t = Solution()
   l2 = t.cyclicallyRightShiftList(l1.getHead(), 3)
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
