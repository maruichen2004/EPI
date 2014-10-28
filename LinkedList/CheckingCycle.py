from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def checkingCycle(self, head):
      if head is None: return None
      fast, slow = head, head
      while fast and fast.next:
         fast = fast.next.next
         slow = slow.next
         if slow == fast:
            slow = head
            while slow != fast:
               slow = slow.next
               fast = fast.next
            return slow
      return None

if __name__ == "__main__":
   l1 = LinkedList(6)
   l1.createCycle(3)
   t = Solution()
   c = t.checkingCycle(l1.getHead())
   print c.val if c else -1
