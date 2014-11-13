class Solution:
   # Time: O(min(P^2 * U, U^2))
   # Space: O(len(A))
   def highestAffinityPairs(self, A):
      pageUserMap = {}
      for page, user in A:
         users = pageUserMap.get(page)
         if users is None:
            users = set()
         users.add(user)
         pageUserMap[page] = users
      res, maxcount = [], 0
      for i in range(len(pageUserMap.keys())):
         for j in range(i + 1, len(pageUserMap.keys())):
            commonUsers = pageUserMap[pageUserMap.keys()[i]].intersection(pageUserMap[pageUserMap.keys()[j]])
            if len(commonUsers) > maxcount:
               maxcount = len(commonUsers)
               res = [pageUserMap.keys()[i], pageUserMap.keys()[j]]
      return res

if __name__ == "__main__":
   A = [("a", 1), ("b", 1), ("b", 2), ("b", 3), ("c", 2), ("c", 3)]
   t = Solution()
   print t.highestAffinityPairs(A)
