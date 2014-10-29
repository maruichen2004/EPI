from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def evenOddMerge(self, head):
      if head is None or head.next is None: return head
      odd_head, even_head, cur = ListNode(0), ListNode(0), head
      odd, even = odd_head, even_head
      count = 0
      while cur:
         if count == 1:
            odd.next = cur
            odd = odd.next
         else:
            even.next = cur
            even = even.next
         cur = cur.next
         count = 1 - count
      even.next = odd_head.next
      odd.next = None
      return even_head.next

if __name__ == "__main__":
   l1 = LinkedList(10, 1, 100)
   l1.display()
   t = Solution()
   l2 = t.evenOddMerge(l1.getHead())
   cur = l2
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
