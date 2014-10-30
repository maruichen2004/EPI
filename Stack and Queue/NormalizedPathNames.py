class Solution:
   # Time: O(n)
   # Space: O(n)
   def normalizedPathNames(self, s):
      stack, tokens = [], s.lstrip("/").split("/")
      for token in tokens:
         if token == ".." and len(stack) > 0: stack.pop()
         elif token != "." and token != ".." and len(token) > 0: stack.append(token)
      return "/" + "/".join(stack)

if __name__ == "__main__":
   tests = ["/a/../b/c", "/./a/b/../c"]
   t = Solution()
   for test in tests:
      print test, t.normalizedPathNames(test)
