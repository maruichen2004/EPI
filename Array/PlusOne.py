class Solution:
   # Time: O(n)
   # Space: O(1)
   def plusOne(self, A):
      carry = 0
      for i in reversed(range(len(A))):
         A[i] = A[i] + 1 if i == len(A) - 1 else A[i] + carry
         carry = 1 if A[i] == 10 else 0
         A[i] %= 10
      if carry == 1: A.insert(0, 1)

if __name__ == "__main__":
   A = [9, 9, 9]
   t = Solution()
   t.plusOne(A)
   print A
