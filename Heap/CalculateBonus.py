class Solution:
   # Time: O(n)
   # Space: O(n)
   def calculateBonus(self, ratings):
      bonus = [1] * len(ratings)
      for i in range(1, len(ratings)):
         if ratings[i-1] < ratings[i]:
            bonus[i] = bonus[i-1] + 1
      for i in reversed(range(len(ratings) - 1)):
         if ratings[i] > ratings[i+1]:
            bonus[i] = max(bonus[i], bonus[i+1] + 1)
      return sum(bonus)

if __name__ == "__main__":
   ratings = [200, 300, 400, 500, 100]
   t = Solution()
   print t.calculateBonus(ratings)
