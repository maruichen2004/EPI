class Solution:
   # Time: O(m)
   # Space: O(l)
   def anonymousLetter(self, L, M):
      map = {}
      for ch in L:
         if ch not in map: map[ch] = 1
         else: map[ch] += 1
      for ch in M:
         if ch in map:
            map[ch] -= 1
            if map[ch] == 0: 
               del map[ch]
               if len(map) == 0: return True
      return len(map) == 0

if __name__ == "__main__":
   L, M = "abc", "defbgcia"
   t = Solution()
   print t.anonymousLetter(L, M)
