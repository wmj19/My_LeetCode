class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.table[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.table[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return any(val == key for val in self.table[index])

    def hash(self, key: int) -> int:
        return key % self.size
