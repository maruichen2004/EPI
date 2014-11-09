class Solution:
   # Time: O(logn)
   # Space: O(1)
   def searchInTwoSortedArrays(self, A, B, k):
      b = max(0, k - len(B))
      t = min(len(A), k)
      while b < t:
         x = b + ((t - b) >> 1)
         A_x_1 = sys.minint if x <= 0 else A[x - 1]
         A_x = sys.maxint if x >= len(A) else A[x]
         B_k_x_1 = sys.minint if k - x <= 0 else B[k - 1 - x]
         B_k_x = sys.maxint if k - x >= len(B) else B[k - x]
         if A_x < B_k_x_1: b = x + 1
         elif A_x_1 > B_k_x: t = x - 1
         else: return max(A_x_1, B_k_x_1)
      A_b_1 = sys.minint if b <= 0 else A[b - 1]
      B_k_b_1 = sys.minint if k - b - 1 < 0 else B[k - b - 1]
      return max(A_b_1, B_k_b_1)

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9]
   B = [2, 4, 6, 8, 10]
   k = 3
   t = Solution()
   print t.searchInTwoSortedArrays(A, B, k)
