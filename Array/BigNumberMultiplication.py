class Solution:
   # Time: O(len(A) * len(B))
   # Space: O(len(A) + len(B))
   def bigNumberMultiplication(self, A, B):
      sign = "" if (A[0] == "-" and B[0] == "-") or (A[0] != "-" and B[0] != "-") else "-"
      if A[0] in "+-": A = A[1:]
      if B[0] in "+-": B = B[1:]
      n1 = [int(i) for i in A]
      n2 = [int(i) for i in B]
      res = [0] * (len(n1) + len(n2))
      for i in range(len(n1)):
         tmp = [k * n1[i] for k in n2]
         tmp += [0] * (len(n1) - 1 - i)
         for j in range(len(tmp)):
            res[-(j+1)] += tmp[-(j+1)]
      for i in reversed(range(1, len(res))):
         res[i-1] += res[i] / 10
         res[i] %= 10
      return sign + "".join([str(i) for i in res]).lstrip("0")

if __name__ == "__main__":
   A = "-11"
   B = "11"
   t = Solution()
   print t.bigNumberMultiplication(A, B)
