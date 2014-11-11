class Solution:
   # Time: O(len(s))
   # Space: O(1)
   def replaceAndRemove(self, s):
      i, count_a = -1, 0
      for j in range(len(s)):
         if s[j] != "b":
            i += 1
            s[i] = s[j]
            if s[j] == "a": count_a += 1
      for j in range(i + 1, len(s)): s[j] = ""
      end = i + count_a
      while i >= 0:
         if s[i] != "a":
            s[end] = s[i]
            i, end = i - 1, end - 1
         else:
            s[end] = "b"
            end -= 1
            s[end] = "b"
            i, end = i - 1, end - 1

if __name__ == "__main__":
   s = ["a", "b", "c", "d", "b", "a"]
   t = Solution()
   t.replaceAndRemove(s)
   print s
