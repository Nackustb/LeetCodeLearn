class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        if key not in self.bucket[hash_key]:
            self.bucket[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        if key in self.bucket[hash_key]:
            self.bucket[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        return key in self.bucket[hash_key]

# test
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))  # True
print(hashSet.contains(3))  # False
hashSet.add(2)
print(hashSet.contains(2))  # True
hashSet.remove(2)
print(hashSet.contains(2))  # False

