from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(len(l1) + len(l2))
   # Space: O(1)
   def overlappingNoCycleLists(self, l1, l2):
      h1, h2, len1, len2 = l1, l2, 0, 0
      while h1: h1, len1 = h1.next, len1 + 1
      while h2: h2, len2 = h2.next, len2 + 1
      h1, h2 = l1, l2
      if len1 > len2:
         for i in range(len1 - len2): h1 = h1.next
      else:
         for i in range(len2 - len1): h2 = h2.next
      while h1 and h2 and h1 != h2:
         h1, h2 = h1.next, h2.next
      return h1

if __name__ == "__main__":
   l1 = LinkedList(5)
   l2 = LinkedList(3)
   cur = l2.getHead()
   while cur.next: cur = cur.next
   cur.next = l1.getHead().next.next
   l1.display()
   l2.display()
   t = Solution()
   node = t.overlappingNoCycleLists(l1.getHead(), l2.getHead())
   print node.val if node else -1
