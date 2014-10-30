from Util.LinkedList import RandomLinkedList
from Util.LinkedList import RandomListNode

class Solution:
   # Time: O(n)
   # Space: O(n)
   def searchPostingsList(self, head):
      self.order = 0
      self.searchPostingsListRec(head)

   def searchPostingsListRec(self, head):
      if head and head.order == -1:
         head.order = self.order
         self.order += 1
         self.searchPostingsListRec(head.random)
         self.searchPostingsListRec(head.next)

   def searchPostingsListIterative(self, head):
      stack, order = [head], 0
      while stack:
         cur = stack[-1]
         stack.pop()
         if cur and cur.order == -1:
            cur.order = order
            order += 1
            stack.append(cur.next)
            stack.append(cur.random)

if __name__ == "__main__":
   l1 = RandomLinkedList(7, 1, 9)
   l1.connect(2, 4)
   l1.connect(0, 6)
   l1.display()
   t = Solution()

   #t.searchPostingsList(l1.getHead())
   #l1.display()
   
   t.searchPostingsListIterative(l1.getHead())
   l1.display()
