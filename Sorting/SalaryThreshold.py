class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def computeSalaryThreshold(self, A, budget):
      A.sort()
      prefixSum, costs = [], []
      val = 0.0
      for a in A:
         val += a
         prefixSum.append(val)
      for i in range(len(prefixSum)):
         costs.append(prefixSum[i] + (len(A) - i - 1) * A[i])
      idx = -1
      for i in range(len(costs)):
         if costs[i] > budget:
            idx = i
            break
      if idx == -1: return -1.0
      elif idx == 0: return budget / len(A)
      return A[idx - 1] + (budget - costs[idx - 1]) / (len(A) - idx)

if __name__ == "__main__":
   A = [90, 60, 100, 40, 20]
   budget = 260
   t = Solution()
   print t.computeSalaryThreshold(A, budget)
