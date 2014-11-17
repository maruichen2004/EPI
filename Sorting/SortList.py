class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None

class Solution:
   # Time: O(nlogn)
   # Space: O(logn)
   def sortList(self, head):
      if head is None or head.next is None:
         return head
      slow, fast, prev = head, head, None
      while fast and fast.next:
         prev = slow
         slow = slow.next
         fast = fast.next.next
      prev.next = None
      l1 = self.sortList(head)
      l2 = self.sortList(slow)
      return self.mergeTwoSortedLists(l1, l2)

   def mergeTwoSortedLists(self, l1, l2):
      dummy = ListNode(0)
      cur = dummy
      while l1 and l2:
         if l1.val < l2.val:
            cur.next = l1
            l1, cur = l1.next, cur.next
         else:
            cur.next = l2
            l2, cur = l2.next, cur.next
      if l1 is not None: cur.next = l1
      elif l2 is not None: cur.next = l2
      return dummy.next

if __name__ == "__main__":
   nodes = [ListNode(2*i+1) for i in range(5)]
   nodes += [ListNode(2*i) for i in range(5)]
   for i in range(len(nodes) - 1):
      nodes[i].next = nodes[i+1]
   t = Solution()
   t.sortList(nodes[0])
   cur = nodes[0]
   while cur:
      print cur.val,
      cur = cur.next
