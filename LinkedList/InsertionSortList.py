from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n^2)
   # Space: O(1)
   def insertionSortList(self, head):
      if head is None or head.next is None:
         return head
      dummy = ListNode(0)
      dummy.next = head
      cur = head
      while cur and cur.next:
         if cur.val > cur.next.val:
            prev = dummy
            while prev.next and prev.next.val < cur.next.val:
               prev = prev.next
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
         else:
            cur = cur.next
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(10, 1, 100)
   l1.display()
   t = Solution()
   l2 = t.insertionSortList(l1.getHead())
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
