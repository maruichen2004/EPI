class Solution:
   # Time: O(n)
   # Space: O(n)
   def leftJustifiedText(self, words, L):
        res, i = [], 0
        while i < len(words):
            size, begin = 0, i
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size + len(words[i]) + 1
                if newsize <= L: size = newsize
                else: break
                i += 1
            spaceCount = L - size
            if i - begin - 1 > 0 and i < len(words):
                everyCount = spaceCount / (i - begin - 1)
                spaceCount %= i - begin - 1
            else:
                everyCount = 0
            j = begin
            while j < i:
                if j == begin: s = words[j]
                else:
                    s += ' ' * (everyCount + 1)
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                    s += words[j]
                j += 1
            s += ' ' * spaceCount
            res.append(s)
        return res

if __name__ == "__main__":
   words = ["This", "is", "an", "example", "of", "test", "justification"]
   L = 16
   t = Solution()
   print t.leftJustifiedText(words, L)
