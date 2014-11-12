import collections

class LRUCache:
   def __init__(self, capacity):
      self.cache = collections.OrderedDict()
      self.capacity = capacity

   # Time: O(1)
   # Space: O(1)
   def get(self, key):
      if key not in self.cache:
         return -1
      val = self.cache[key]
      del self.cache[key]
      self.cache[key] = val
      return val

   # Time: O(1)
   # Space: O(1)
   def set(self, key, val):
      if key in self.cache:
         del self.cache[key]
      elif len(self.cache) == self.capacity:
         self.cache.popitem(last=False)
      self.cache[key] = val

if __name__ == "__main__":
   cache = LRUCache(3)
   for i in range(5):
      cache.set(i, i * i)
   cache.get(3)
   cache.set(4, 2)
   print cache.cache
