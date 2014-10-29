from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def findMedianSortedCircularLinkedList(self, node):
      cur, start, length = node.next, node, 1
      while cur != node:
         if start.val <= cur.val:
            start = cur
         cur = cur.next
         length += 1
      start = start.next
      for i in range((length - 1)/2): start = start.next
      if length % 2 == 1: return start.val
      return 0.5 * (start.val + start.next.val)

if __name__ == "__main__":
   l1 = LinkedList(12, 1, 9, True)
   l1.display()
   l1.createCycle(0)
   t = Solution()
   print t.findMedianSortedCircularLinkedList(l1.getHead())
