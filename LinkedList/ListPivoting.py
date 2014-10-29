from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def listPivoting(self, head, k):
      if head is None or head.next is None:
         return head
      larger_head, equal_head, smaller_head = ListNode(0), ListNode(0), ListNode(0)
      larger, equal, smaller, cur = larger_head, equal_head, smaller_head, head
      while cur:
         if cur.val > k:
            larger.next = cur
            larger = larger.next
         elif cur.val == k:
            equal.next = cur
            equal = equal.next
         else:
            smaller.next = cur
            smaller = smaller.next
         cur = cur.next
      smaller.next = equal_head.next
      equal.next = larger_head.next
      larger.next = None
      return smaller_head.next

if __name__ == "__main__":
   l1 = LinkedList(10, 1, 6)
   l1.display()
   t = Solution()
   l2 = t.listPivoting(l1.getHead(), 4)
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
