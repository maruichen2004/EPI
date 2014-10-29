from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(len(L1) + len(L2))
   # Space: O(len(L1) + len(L2))
   def addTwoNumbers(self, l1, l2):
      dummy = ListNode(0)
      carry, cur = 0, dummy
      while l1 or l2:
         sum = carry
         if l1:
            sum += l1.val 
            l1 = l1.next
         if l2:
            sum += l2.val
            l2 = l2.next
         carry = sum / 10
         sum %= 10
         cur.next = ListNode(sum)
         cur =  cur.next
      if carry == 1: cur.next = ListNode(1)
      return dummy.next

if __name__ == "__main__":
   l1 = LinkedList(4, 1, 9)
   l1.display()
   l2 = LinkedList(4, 1, 9)
   l2.display()
   t = Solution()
   l3 = t.addTwoNumbers(l1.getHead(), l2.getHead())
   cur = l3
   while cur:
      print cur.val,
      cur = cur.next
   print "\n"
