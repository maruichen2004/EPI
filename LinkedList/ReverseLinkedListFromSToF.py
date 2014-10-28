from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(f)
   # Space: O(1)
   def reverseSublistSF(self, head, s, f):
      dummy = ListNode(0)
      dummy.next = head
      lastUnSwap, cur, diff = dummy, head, f - s
      while cur and s > 1:
         cur = cur.next
         lastUnSwap = lastUnSwap.next
         s -= 1
      firstSwap, prev = cur, lastUnSwap
      while cur and diff >= 0:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
         diff -= 1
      lastUnSwap.next = prev
      firstSwap.next = cur
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(5)
   l1.display()
   t = Solution()
   l2 = t.reverseSublistSF(l1.getHead(), 2, 4)
   cur = l2
   while cur:
      print cur.val, 
      cur = cur.next
   print "\n"
