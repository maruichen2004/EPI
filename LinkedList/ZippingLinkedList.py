from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def zippingLinkedList(self, head):
      if head is None or head.next is None: return head
      fast, slow = head, head
      while fast and fast.next:
         fast = fast.next.next
         slow = slow.next
      prev, cur = None, slow.next
      slow.next = None
      while cur:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
      dummy = ListNode(0)
      cur = dummy
      while head or prev:
         if head:
            cur.next = head
            head = head.next
            cur = cur.next
         if prev:
            cur.next = prev
            prev = prev.next
            cur = cur.next
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(10, 1, 100)
   l1.display()
   t = Solution()
   l2 = t.zippingLinkedList(l1.getHead())
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
