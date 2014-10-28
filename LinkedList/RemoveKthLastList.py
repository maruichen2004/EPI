from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n):
   # Space: O(1):
   def removeKthLastList(self, head, k):
      dummy = ListNode(0)
      dummy.next = head
      fast = dummy
      for i in range(k): fast = fast.next
      slow = dummy
      while fast and fast.next:
         fast, slow = fast.next, slow.next
      slow.next = slow.next.next
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(5)
   l1.display()
   t = Solution()
   l2 = t.removeKthLastList(l1.getHead(), 3)
   cur = l2
   while cur:
      print cur.val, 
      cur = cur.next
   print "\n"
