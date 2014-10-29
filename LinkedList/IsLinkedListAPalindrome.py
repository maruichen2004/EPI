from Util.LinkedList import ListNode
from Util.LinkedList import LinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def isLinkedListAPalindrome(self, head):
      if head is None or head.next is None:
         return True
      fast, slow, prev = head, head, None
      while fast and fast.next:
         fast = fast.next.next
         prev = slow
         slow = slow.next
      prev.next = None
      prev, cur = None, slow
      while cur:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
      while prev and head:
         if prev.val != head.val:
            return False
         head = head.next
         prev = prev.next
      return True

if __name__ == "__main__":
   l1 = LinkedList(4, 1, 2)
   l1.display()
   t = Solution()
   print t.isLinkedListAPalindrome(l1.getHead())
