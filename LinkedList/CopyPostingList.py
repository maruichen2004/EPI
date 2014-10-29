from Util.LinkedList import RandomListNode
from Util.LinkedList import RandomLinkedList

class Solution:
   # Time: O(n)
   # Space: O(1)
   def copyPostingList(self, head):
      if head is None or head.next is None:
         return head
      map = {}
      dummy = RandomListNode(0)
      cur = dummy
      while head:
         copy = RandomListNode(head.val)
         cur.next = copy
         map[head] = copy
         cur = cur.next
         head = head.next
      for node in map:
         if node.random:
            map[node].random = map[node.random]
      return dummy.next

if __name__ == "__main__":
   l1 = RandomLinkedList(7, 1, 9)
   l1.connect(1, 3)
   l1.connect(2, 4)
   l1.display()
   t = Solution()
   l2 = t.copyPostingList(l1.getHead())
   cur = l2
   while cur:
      print cur.val,
      if cur.random: print "(" + str(cur.random.val) + ")",
      cur = cur.next
   print "\n" 
