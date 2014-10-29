from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def removeDuplicates(self, head):
      if head is None or head.next is None:
         return head
      cur = head
      while cur and cur.next:
         if cur.val == cur.next.val:
            cur.next = cur.next.next
         else:
            cur = cur.next
      return head

if __name__ == "__main__":
   l1 = LinkedList(10, 1, 5, True)
   l1.display()
   t = Solution()
   l2 = t.removeDuplicates(l1.getHead())
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
