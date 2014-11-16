class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def countInversions(self, A):
      return self.countInversionsHelper(A, 0, len(A))

   def countInversionsHelper(self, A, start, end):
      if end - start <= 1: return 0
      mid = start + ((end - start) >> 1)
      return self.countInversionsHelper(A, start, mid) + self.countInversionsHelper(A, mid, end) + self.merge(A, start, mid, end)

   def merge(self, A, start, mid, end):
      sortedA = []
      left, right, count = start, mid, 0
      while left < mid and right < end:
         if A[left] < A[right]:
            sortedA.append(A[left])
            left += 1
         else:
            sortedA.append(A[right])
            right += 1
            count += mid - left
      sortedA += A[left:mid]
      sortedA += A[right:end]
      for x in sortedA:
         A[start] = x
         start += 1
      return count

if __name__ == "__main__":
   A = [1, 3, 2, 5, 4, 3]
   t = Solution()
   print t.countInversions(A)
