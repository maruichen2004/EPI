from Util.LinkedList import LinkedList
from Util.LinkedList import ListNode

class Solution:
   # Time: O(len(F) + len(L))
   # Space: O(1)
   def mergeTwoSortedLists(self, F, L):
      dummy = ListNode(0)
      cur, l1, l2 = dummy, F, L
      while l1 and l2:
         if l1.val < l2.val:
            cur.next = l1
            cur, l1 = cur.next, l1.next
         else:
            cur.next = l2
            cur, l2 = cur.next, l2.next
      if l1 is None: cur.next = l2
      else: cur.next = l1
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(5, True)
   l2 = LinkedList(5, True)
   l1.display()
   l2.display()
   t = Solution()
   l3 = t.mergeTwoSortedLists(l1.getHead(), l2.getHead())
   cur = l3
   while cur:
      print cur.val, 
      cur = cur.next
   print "\n"
