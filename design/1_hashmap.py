

class HashTable:
    
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        self.arr[hash] = val
        
    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None
    
hash = HashTable()

# hash.add("sathish", "selvan")
# print(hash.arr)

# print(hash.get("sathish"))

hash["s"] = "s"

print(hash["s"])

del hash["s"]
  


