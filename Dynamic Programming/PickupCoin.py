class Solution:
   # Time: O(n^2)
   # Space: O(n^2)
   def pickupCoin(self, C):
      T = [[-1 for i in range(len(C))] for j in range(len(C))]
      return self.pickupCoinHelper(C, 0, len(C) - 1, T)

   def pickupCoinHelper(self, C, a, b, T):
      if a > b: return 0
      if T[a][b] == -1:
         T[a][b] = max(min(self.pickupCoinHelper(C, a+2, b, T), \
                           self.pickupCoinHelper(C, a+1, b-1, T)) + C[a],\
                       min(self.pickupCoinHelper(C, a, b-2, T), \
                           self.pickupCoinHelper(C, a+1, b-1, T)) + C[b])
      return T[a][b]

if __name__ == "__main__":
   C = [1, 3, 5, 7, 9, 7, 5, 3, 1]
   t = Solution()
   print t.pickupCoin(C)
