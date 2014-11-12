class Solution:
   # Time: O(nmlogm)
   # Space: O(nm)
   def anagrams(self, words):
      map, res = {}, []
      for word in words:
         sortedword = "".join(sorted(word))
         if sortedword not in map:
            map[sortedword] = [word]
         else:
            map[sortedword].append(word)
      for item in map:
         if len(map[item]) > 1:
            res.append(map[item])
      return res

if __name__ == "__main__":
   words = ["abc", "cbs", "bca", "sbc", "def"]
   t = Solution()
   print t.anagrams(words)
