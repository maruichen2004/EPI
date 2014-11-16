class Solution:
   # Time: O(nlogn)
   # Space: O(logn)
   def drawSkylines(self, skylines):
      return self.drawSkylinesHelper(skylines, 0, len(skylines))

   def drawSkylinesHelper(self, skylines, l, r):
      if r - l <= 1: return skylines[l:r]
      mid = l + ((r - l) >> 1)
      L = self.drawSkylinesHelper(skylines, l, mid)
      R = self.drawSkylinesHelper(skylines, mid, r)
      return self.mergeSkylines(L, R)

   def mergeSkylines(self, L, R):
      i, j = 0, 0
      res = []
      while i < len(L) and j < len(R):
         if L[i].right < R[j].left:
            res.append(L[i])
            i += 1
         elif R[j].right < L[i].left:
            res.append(R[j])
            j += 1
         elif L[i].left <= R[j].left:
            idxs = [i, j]
            self.mergeIntersectSkylines(res, L[i], R[j], idxs)
            i, j = idxs[0], idxs[1]
         else:
            idxs = [i, j]
            self.mergeIntersectSkylines(res, R[j], L[i], idxs)
            i, j = idxs[0], idxs[1]
      res += L[i:]
      res += R[j:]
      return res

   def mergeIntersectSkylines(merged, a, b, idxs):
      if a.right <= b.right:
         if a.height > b.height:
            if b.right != a.right:
               merged.append(a)
               idxs[0] += 1
               b.left = a.right
            else: idxs[1] += 1
         elif a.height == b.height:
            b.left = a.left
            idxs[0] += 1
         else:
            if a.left != b.left: merged.append(Skyline(a.left, b.left, a.height))
            idxs[0] += 1
      else:
         if a.height >= b.height: idxs[1] += 1
         else:
            if a.left != b.left: merged.append(Skyline(a.left, b.left, a.height))
            a.left = b.right
            merged.append(b)
            idxs[1] += 1
