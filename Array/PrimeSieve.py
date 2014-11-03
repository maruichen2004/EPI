import math
class Solution:
   # Time: O(nloglogn)
   # Space: O(n)
   def primeSieve(self, n):
      size = int(math.floor(0.5 * (n - 3))) + 1
      primes = [2]
      is_prime = [True] * size
      for i in range(size):
         if is_prime[i]:
            p = (i << 1) + 3
            primes.append(p)
            for j in range(((i * i) << 1) + 6 * i + 3, size, p): is_prime[j] = False
      return primes

if __name__ == "__main__":
   n = 100
   t = Solution()
   print t.primeSieve(n)
