class Solution:
   # Time: O(n)
   # Space: O(1)
   def dutchNationalFlag(self, A, pivotIdx):
      pivot = A[pivotIdx]
      smaller, equal, larger = -1, 0, len(A)
      while equal < larger:
         if A[equal] < pivot:
            smaller += 1
            A[equal], A[smaller] = A[smaller], A[equal]
         elif A[equal] > pivot:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
            equal -= 1
         equal += 1

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
   pivot = 2
   t = Solution()
   t.dutchNationalFlag(A, pivot)
   print A
