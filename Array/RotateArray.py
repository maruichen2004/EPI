class Solution:
   # Time: O(n)
   # Space: O(1)
   def rotateArray(self, A, k):
      self.reverse(A, 0, len(A) - 1)
      self.reverse(A, 0, k - 1)
      self.reverse(A, k, len(A) - 1)

   def reverse(self, A, start, end):
      while start < end:
         A[start], A[end] = A[end], A[start]
         start += 1
         end -= 1

if __name__ == "__main__":
   A = [1, 2, 3, 4, 5]
   k = 4
   t = Solution()
   t.rotateArray(A, k)
   print A
