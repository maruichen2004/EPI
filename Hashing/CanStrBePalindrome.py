class Solution:
   # Time: O(n) n is the length of s
   # Space: O(c) c is number distinct numbers in s
   def palindromePermutation(self, s):
      map, odd_count = {}, 0
      for ch in s:
         if ch not in map: map[ch] = 1
         else: map[ch] += 1
      for item in map:
         if map[item] & 1 == 1:
            odd_count += 1
      return odd_count <= 1

   # Time: O(nlogn)
   # Space: O(1)
   def palindromePermutationSorting(self, s):
      s = "".join(sorted(s))
      odd_count, count, i = 0, 1, 1
      while i < len(s) and odd_count <= 1:
         if s[i] != s[i-1]:
            if count & 1 == 1: odd_count += 1
            count = 1
         else: count += 1
         i += 1
      return odd_count <= 1

if __name__ == "__main__":
   s = "levelta"
   t = Solution()
   print t.palindromePermutation(s)
   print t.palindromePermutationSorting(s)
