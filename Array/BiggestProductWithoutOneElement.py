class Solution:
   # Time: O(n)
   # Space: O(1)
   def biggestProduct(self, A):
      zero_count, pos_count, neg_count = 0, 0, 0
      zero_idx, s_neg_idx, b_neg_idx, s_pos_idx = -1, -1, -1, -1
      for i in range(len(A)):
         if A[i] < 0:
            neg_count += 1
            if s_neg_idx == -1 or A[i] < A[s_neg_idx]: s_neg_idx = i
            if b_neg_idx == -1 or A[i] > A[b_neg_idx]: b_neg_idx = i
         elif A[i] == 0:
            zero_count += 1
            zero_idx = i
         else:
            pos_count += 1
            if s_pos_idx == -1 or A[i] < A[s_pos_idx]: s_pos_idx = i
      if zero_count >= 2: return 0
      elif zero_count == 1:
         if neg_count % 2 == 1: return 0
         else: x = zero_idx
      else:
         if neg_count % 2 == 1: x = b_neg_idx
         elif pos_count > 0: x = s_pos_idx
         else: x = s_neg_idx
      res = 1
      for i in range(len(A)):
         if i != x: res *= A[i]
      return res

if __name__ == "__main__":
   A = [0, -2, 0, 5, 4]
   t = Solution()
   print t.biggestProduct(A)
