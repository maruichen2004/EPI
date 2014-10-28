from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def reverseLinkedList(self, head):
      if head is None or head.next is None:
         return head
      prev, cur = None, head
      while cur:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
      return prev

if __name__ == "__main__":
   l1 = LinkedList(10)
   l1.display()
   t = Solution()
   l2 = t.reverseLinkedList(l1.getHead())
   cur = l2
   while cur:
      print cur.val, 
      cur = cur.next
   print "\n"
