import sys

class Solution:
   # Time: O(n)
   # Space: O(c) c is the number of distinct strings
   def nearestRepetition(self, strs):
      map, cloest = {}, sys.maxint
      for i in range(len(strs)):
         if strs[i] not in map:
            map[strs[i]] = i
         else:
            cloest = min(cloest, i - map[strs[i]])
            map[strs[i]] = i
      return cloest

if __name__ == "__main__":
   strs = ["foo", "bar", "widget", "foo", "xyz", "widget", "bar", "adnan"]
   t = Solution()
   print t.nearestRepetition(strs)
