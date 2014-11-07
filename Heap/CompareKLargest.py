class Solution:
   # Time: O(k)
   # Space: O(k)
   def compareKLargest(self, A, k, x):
      data = [0, 0]
      self.compareKLargestHelper(A, k, x, 0, data)
      if data[0] >= k: return 1
      elif sum(data) >= k: return 0
      else: return -1

   def compareKLargestHelper(self, A, k, x, idx, data):
      if data[0] >= k or idx >= len(A) or A[idx] < x:
         return
      elif A[idx] == x:
         data[1] += 1
         if data[1] >= k: return
      else:
         data[0] += 1
      self.compareKLargestHelper(A, k, x, (idx << 1) + 1, data)
      self.compareKLargestHelper(A, k, x, (idx << 1) + 2, data)

if __name__ == "__main__":
   A = [9, 5, 8, 3, 4, 6, 7, 1, 2]
   k = 3
   x = 10
   t = Solution()
   print t.compareKLargest(A, k, x)
